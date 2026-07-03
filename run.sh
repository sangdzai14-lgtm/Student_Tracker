#!/bin/bash

# Student Academic Portal - Startup Script for macOS/Linux

echo ""
echo "========================================"
echo "  Student Academic Portal"
echo "  TEC004/05"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "✓ Python found: $(python3 --version)"
echo ""

# Check if venv exists, if not create it
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

echo ""
echo "Activating virtual environment..."
source venv/bin/activate

echo ""
echo "Checking dependencies..."
pip install -q -r requirements.txt

echo "✓ Dependencies installed"
echo ""

# Check if database exists, if not generate sample data
if [ ! -f "student_tracker.db" ]; then
    echo "Generating sample data..."
    python3 sample_data.py
    echo "✓ Sample data generated"
    echo ""
fi

echo ""
echo "========================================"
echo "Starting Flask Server..."
echo "========================================"
echo ""
echo "🌐 Open your browser at: http://localhost:5000"
echo "📚 Dashboard: http://localhost:5000/"
echo "👥 Students: http://localhost:5000/students"
echo "📖 Courses: http://localhost:5000/courses"
echo "📊 Analytics: http://localhost:5000/analytics"
echo "🧠 Predictions: http://localhost:5000/predictions"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py
