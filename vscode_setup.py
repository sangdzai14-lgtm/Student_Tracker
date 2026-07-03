"""
VS Code Auto-Setup Script
Run this to prepare VS Code environment
"""

import os
import sys
import subprocess

def setup_vscode_env():
    """Setup VS Code environment"""
    
    print("=" * 60)
    print("🚀 Student Portal - VS Code Setup")
    print("=" * 60)
    print()
    
    # Check Python version
    print("✓ Checking Python version...")
    python_version = sys.version_info
    print(f"  Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("❌ Python 3.8 or higher required")
        return False
    
    # Check if venv exists
    print("\n✓ Checking virtual environment...")
    if not os.path.exists('venv'):
        print("  Creating virtual environment...")
        subprocess.run([sys.executable, '-m', 'venv', 'venv'], check=True)
        print("  ✓ Virtual environment created")
    else:
        print("  ✓ Virtual environment already exists")
    
    # Check if dependencies installed
    print("\n✓ Checking dependencies...")
    try:
        import flask
        import pandas
        import sklearn
        print("  ✓ All dependencies installed")
    except ImportError:
        print("  Installing dependencies...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
        print("  ✓ Dependencies installed")
    
    # Check database
    print("\n✓ Checking database...")
    if not os.path.exists('student_tracker.db'):
        print("  Generating sample data...")
        exec(open('sample_data.py').read())
        print("  ✓ Sample data generated")
    else:
        print("  ✓ Database already exists")
    
    print("\n" + "=" * 60)
    print("✅ VS Code Setup Complete!")
    print("=" * 60)
    print("\n📖 Next Steps:")
    print("  1. Press Ctrl+Shift+D to open Run and Debug")
    print("  2. Select '🚀 Flask - Run Portal'")
    print("  3. Click the Play button")
    print("  4. Open http://localhost:5000 in browser")
    print()
    
    return True

if __name__ == '__main__':
    try:
        setup_vscode_env()
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        sys.exit(1)
