@echo off
echo ============================================================
echo 🔧 REPAIRING ENVIRONMENT FOR STUDENT TRACKER PORTAL
echo ============================================================

echo [1/4] Deleting old virtual environment...
if exist venv (
    rmdir /s /q venv
)

echo [2/4] Creating new virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ❌ ERROR: Failed to create venv. Make sure Python is installed.
    pause
    exit /b
)

echo [3/4] Installing dependencies...
.\venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel
.\venv\Scripts\python.exe -m pip install Flask Flask-SQLAlchemy pandas matplotlib numpy scikit-learn beautifulsoup4 requests seaborn lxml

echo [4/4] Verifying installation...
.\venv\Scripts\python.exe -c "import flask, pandas, sklearn, matplotlib, bs4, requests, seaborn, lxml; print('✅ All modules installed successfully!')"

echo ============================================================
echo 🎉 REPAIR COMPLETE!
echo Please restart VS Code to apply changes.
echo Use "START PROJECT (Live Data)" in Debug menu to run.
echo ============================================================
pause
