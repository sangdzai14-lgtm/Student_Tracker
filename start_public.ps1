# START_PUBLIC.PS1 v10.7
# Ultra-robust version for URL capture and absolute path execution

$ErrorActionPreference = "SilentlyContinue"
Write-Host "--- ACADEMIC AI PUBLIC DEPLOYMENT ---" -ForegroundColor Cyan

# 1. Locate/Install Cloudflared
$programFilesX86 = [System.Environment]::GetEnvironmentVariable("ProgramFiles(x86)")
$cfExe = "$programFilesX86\cloudflared\cloudflared.exe"

if (-not (Test-Path $cfExe)) {
    Write-Host "Cloudflared not found. Installing..." -ForegroundColor Yellow
    $url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.msi"
    $msi = "$env:TEMP\cf_install.msi"
    Invoke-WebRequest -Uri $url -OutFile $msi
    Start-Process msiexec.exe -ArgumentList "/i `"$msi`" /quiet /qn" -Wait
    Remove-Item $msi
}

if (-not (Test-Path $cfExe)) {
    Write-Host "ERROR: Installation failed or path unreachable." -ForegroundColor Red
    exit 1
}

Write-Host "Cloudflared confirmed at: $cfExe" -ForegroundColor Gray

# 2. Python Setup
if (-not (Test-Path "venv")) {
    Write-Host "Creating Virtual Environment..."
    python -m venv venv
}
Write-Host "Installing/Updating packages..."
& ".\venv\Scripts\python.exe" -m pip install --upgrade pip setuptools wheel > $null
& ".\venv\Scripts\python.exe" -m pip install -r requirements.txt flask-cors python-dotenv > $null

# 3. Start Backend
Write-Host "Starting Flask server on port 5000..." -ForegroundColor Green
$flask = Start-Process ".\venv\Scripts\python.exe" -ArgumentList "app.py" -PassThru -WindowStyle Hidden
Start-Sleep -Seconds 5

# 4. Start Tunnel and Extract URL
Write-Host "Opening Secure Bridge to Internet..." -ForegroundColor Cyan
$log = "$env:TEMP\cf_tunnel_$(Get-Random).log"
if (Test-Path $log) { Remove-Item $log }

# Use absolute path and redirect error (where CF outputs logs)
Start-Process $cfExe -ArgumentList "tunnel --url http://localhost:5000" -RedirectStandardError $log -WindowStyle Hidden

Write-Host "Capturing Public Neural Link..." -ForegroundColor Gray
$publicUrl = ""
$timer = 0
while ($timer -lt 40) {
    if (Test-Path $log) {
        $content = Get-Content $log -Raw
        # Regex to find the xxxxx.trycloudflare.com URL
        if ($content -match "(https://[a-zA-Z0-9-]+\.trycloudflare\.com)") {
            $publicUrl = $matches[1]
            break
        }
    }
    Start-Sleep -Seconds 1
    $timer++
}

if ($publicUrl) {
    Write-Host "`n========================================================" -ForegroundColor Green
    Write-Host "✅ SYSTEM IS NOW PUBLICLY ACCESSIBLE" -ForegroundColor Green
    Write-Host "🔗 URL: $publicUrl" -ForegroundColor White
    Write-Host "========================================================`n" -ForegroundColor Green

    # Sync environment
    "API_BASE_URL=$publicUrl" | Out-File -FilePath ".env" -Encoding ASCII

    # Verify health
    Write-Host "Verifying node health..." -ForegroundColor Gray
    try {
        $health = Invoke-RestMethod -Uri "$publicUrl/health" -Method Get -TimeoutSec 10
        if ($health.status -eq "healthy") {
            Write-Host "✓ Health Check: PASSED" -ForegroundColor Green
        }
    } catch {
        Write-Host "! Health Check: DELAYED (System still stabilizing)" -ForegroundColor Yellow
    }

    Write-Host "Launching Browser..." -ForegroundColor Gray
    Start-Process "$publicUrl/analysis"
} else {
    Write-Host "❌ CRITICAL ERROR: URL capture timed out." -ForegroundColor Red
    Write-Host "Check tunnel logs: $log"
}

Write-Host "Keep this window open to maintain the link."
Write-Host "Press Ctrl+C to shutdown."
try {
    while($true) { Start-Sleep -Seconds 1 }
} finally {
    Write-Host "`nShutting down nodes..." -ForegroundColor Yellow
    if ($flask) { Stop-Process -Id $flask.Id -Force }
    Get-Process "cloudflared" | Stop-Process -Force
}
