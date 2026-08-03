@echo off
setlocal enabledelayedexpansion

echo 🚀 INITIATING PUBLIC DEPLOYMENT SEQUENCE...

:: 1. Environment Check
if not exist venv (
    echo 📦 Creating Virtual Environment...
    python -m venv venv
)
call venv\Scripts\activate
pip install -r requirements.txt flask-cors python-dotenv > nul

:: 2. Cloudflare Tunnel Setup
echo ☁️ Checking Cloudflare Tunnel...
where cloudflared >nul 2>nul
if %errorlevel% neq 0 (
    echo 📥 cloudflared not found. Downloading...
    powershell -Command "Invoke-WebRequest -Uri 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.msi' -OutFile 'cloudflared_installer.msi'"
    echo ⚙️ Installing cloudflared...
    msiexec /i cloudflared_installer.msi /quiet /qn /norestart
    del cloudflared_installer.msi
    set PATH=%PATH%;C:\Program Files (x86)\cloudflared
)

:: 3. Start Flask Server in background
echo 🐍 Starting Academic AI Backend...
start /B venv\Scripts\python.exe app.py

:: Wait for Flask to stabilize
timeout /t 5 /nobreak > nul

:: 4. Launch Cloudflare Tunnel and Capture URL
echo 🛡️ Establishing Secure Tunnel...
:: We use a temporary file to capture the URL
if exist tunnel.log del tunnel.log
start /B cloudflared tunnel --url http://localhost:5000 > tunnel.log 2>&1

:: Wait for URL to be generated
echo ⏳ Awaiting Public HTTPS Link...
:wait_url
timeout /t 2 /nobreak > nul
findstr /C:"trycloudflare.com" tunnel.log > nul
if %errorlevel% neq 0 goto wait_url

:: Extract the URL
for /f "tokens=4" %%a in ('findstr /C:"trycloudflare.com" tunnel.log') do (
    set PUBLIC_URL=%%a
)
:: Clean the URL (remove possible ANSI escape codes or extra chars)
set PUBLIC_URL=%PUBLIC_URL: =%

echo.
echo ========================================================
echo ✅ SYSTEM IS NOW PUBLICLY ACCESSIBLE!
echo 🔗 URL: !PUBLIC_URL!
echo ========================================================
echo.

:: Save to .env for persistence
echo API_BASE_URL=!PUBLIC_URL! > .env

:: 5. Open Browser
start !PUBLIC_URL!/analysis

echo Press Ctrl+C in this window to terminate the session.
pause
