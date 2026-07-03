@echo off
REM Student Academic Portal - Startup Script for Windows

echo.
echo ========================================
echo  Student Academic Portal
echo  TEC004/05
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

echo ✓ Python found
echo.

REM Check if venv exists, if not create it
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo ✓ Virtual environment created
)

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Checking dependencies...
pip install -q -r requirements.txt

echo ✓ Dependencies installed
echo.

REM Check if database exists, if not generate sample data
if not exist "student_tracker.db" (
    echo Generating sample data...
    python sample_data.py
    echo ✓ Sample data generated
    echo.
)

echo.
echo ========================================
echo Starting Flask Server...
echo ========================================
echo.
echo 🌐 Open your browser at: http://localhost:5000
echo 📚 Dashboard: http://localhost:5000/
echo 👥 Students: http://localhost:5000/students
echo 📖 Courses: http://localhost:5000/courses
echo 📊 Analytics: http://localhost:5000/analytics
echo 🧠 Predictions: http://localhost:5000/predictions
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py

pause
