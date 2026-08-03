@echo off
TITLE ACADEMIC AI PUBLIC DEPLOYER
:: v10.7 Stable Wrapper
powershell -ExecutionPolicy Bypass -File "%~dp0start_public.ps1"
if %errorlevel% neq 0 pause
