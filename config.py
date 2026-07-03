"""
Configuration and Setup Guide for Student Academic Portal

Quick Start Guide
"""

QUICK_START = """
╔═══════════════════════════════════════════════════════════════╗
║         🎓 Student Academic Portal - Quick Start              ║
║              Project: TEC004/05                               ║
╚═══════════════════════════════════════════════════════════════╝

1. INSTALL DEPENDENCIES
   └─ pip install -r requirements.txt

2. GENERATE SAMPLE DATA
   └─ python sample_data.py

3. RUN THE APPLICATION
   └─ python app.py
   
4. OPEN BROWSER
   └─ http://localhost:5000

═══════════════════════════════════════════════════════════════

FEATURES AVAILABLE:

📚 Dashboard
   → Overview of system statistics
   → Quick links to main features
   → Top performers display

👥 Students Management
   → View all students
   → Student detailed view
   → GPA and performance metrics
   → Course enrollment details

📖 Course Management
   → Browse all courses
   → Course statistics
   → Enrolled students list
   → Grade analysis

📊 Analytics Dashboard
   → Real-time performance metrics
   → At-risk student identification
   → Grade distribution analysis
   → Correlation studies

🧠 AI Grade Prediction
   → Predict final grades
   → Input midterm and assignments
   → Risk assessment
   → Model insights

📈 Reports & Export
   → Generate reports
   → System statistics
   → At-risk student alerts

═══════════════════════════════════════════════════════════════

TECHNOLOGIES USED:

Backend:
  • Python 3.8+
  • Flask Web Framework
  • SQLite Database
  • Pandas Data Analysis
  • Scikit-learn ML
  • NumPy

Frontend:
  • HTML5
  • Bootstrap 5 CSS
  • Chart.js Visualization
  • JavaScript

═══════════════════════════════════════════════════════════════

PROJECT STRUCTURE:

├── app.py                    Main Flask application
├── models.py                 OOP classes
├── database.py               Database management
├── analytics.py              Data analysis & prediction
├── sample_data.py            Demo data generator
├── requirements.txt          Python dependencies
├── run.bat                   Windows startup script
├── run.sh                    Linux/Mac startup script
├── README.md                 Full documentation
├── templates/                HTML templates
│   ├── base.html
│   ├── index.html
│   ├── students.html
│   ├── courses.html
│   ├── analytics.html
│   ├── predictions.html
│   ├── reports.html
│   ├── about.html
│   ├── 404.html
│   └── 500.html
└── static/                   CSS and JavaScript
    ├── style.css
    └── script.js

═══════════════════════════════════════════════════════════════

DATABASE SCHEMA:

Tables:
  • students       Student records with GPAs
  • instructors    Instructor information
  • courses        Course details
  • enrollments    Student-course relationships
  • grades         Grade records for all courses
  • assignments    Assignment details
  • assignment_submissions  Student submissions

═══════════════════════════════════════════════════════════════

SAMPLE DATA INCLUDES:

  ✓ 4 Instructors from different departments
  ✓ 6 Courses across Computer Science, Math, Physics, Chemistry
  ✓ 10 Students from various majors
  ✓ Multiple enrollments per student
  ✓ Realistic grade data with correlations
  ✓ Some at-risk students for demonstration
  ✓ Top performers for analytics showcase

═══════════════════════════════════════════════════════════════

KEY OOP CONCEPTS IMPLEMENTED:

1. Abstraction
   └─ Abstract base class: Person
   └─ Abstract methods for polymorphism

2. Inheritance
   └─ Student and Instructor inherit from Person
   └─ Different GradeBook implementations

3. Polymorphism
   └─ Multiple grading schemes:
      • WeightedGradeBook (30/40/30)
      • CurvedGradeBook (Curve factor: 1.05)
      • PassFailGradeBook (Binary pass/fail)

4. Encapsulation
   └─ Private attributes with getters
   └─ Database abstraction layer
   └─ Analytics module encapsulation

═══════════════════════════════════════════════════════════════

ADVANCED FEATURES:

🤖 Machine Learning
   └─ Linear Regression for grade prediction
   └─ Model persistence with pickle
   └─ At-risk student classification

📊 Data Analysis
   └─ Pandas DataFrames for analysis
   └─ Statistical calculations
   └─ Correlation analysis (Midterm vs Final)

🔄 Multi-Phased Architecture
   └─ Phase 1: System Design & Database
   └─ Phase 2: Analytics & Visualization
   └─ Phase 3: AI & Final Integration

═══════════════════════════════════════════════════════════════

API ENDPOINTS:

GET /                          Dashboard
GET /students                  Students list
GET /student/<id>              Student details
GET /courses                   Courses list
GET /course/<id>               Course details
GET /analytics                 Analytics dashboard
GET /predictions               Grade prediction
GET /reports                   Reports page
GET /about                     About page

API Routes:
POST /api/predict              Grade prediction model
GET  /api/grade-distribution   Grade stats
GET  /api/student-trend        Student trends
GET  /api/course-stats         Course statistics
GET  /api/at-risk-students     At-risk list
GET  /api/top-performers       Top performers

═══════════════════════════════════════════════════════════════

TROUBLESHOOTING:

Issue: Port 5000 already in use
Solution: Modify port in app.py: app.run(port=5001)

Issue: Database errors
Solution: Delete student_tracker.db and run sample_data.py again

Issue: Missing dependencies
Solution: pip install -r requirements.txt --force-reinstall

Issue: Virtual environment issues
Solution: Delete venv folder and recreate it

═══════════════════════════════════════════════════════════════

NEXT STEPS:

1. Run the application
2. Explore the dashboard
3. Review student and course details
4. Test grade prediction with different values
5. Check analytics for insights
6. Review the code structure
7. Experiment with sample data modifications
8. Deploy to production (with security updates)

═══════════════════════════════════════════════════════════════

For complete documentation, see README.md

Happy Learning! 🚀
"""

if __name__ == '__main__':
    print(QUICK_START)

# Configuration constants
DATABASE_PATH = 'student_tracker.db'
FLASK_PORT = 5000
FLASK_HOST = '0.0.0.0'
DEBUG_MODE = True

# Grade thresholds
GRADE_THRESHOLDS = {
    'A': 90,
    'B': 80,
    'C': 70,
    'D': 60,
    'F': 0
}

# Risk threshold
AT_RISK_THRESHOLD = 70  # Students below this percentage are considered at-risk

# Grading weights (Weighted GradeBook)
GRADING_WEIGHTS = {
    'midterm': 0.30,
    'final': 0.40,
    'assignments': 0.30
}

# Curve factor for curved grading
CURVE_FACTOR = 1.05

# Passing score for pass/fail grading
PASSING_SCORE = 70
