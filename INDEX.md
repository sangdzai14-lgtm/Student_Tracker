# 🎓 Student Academic Portal - Project Files Index

## 📋 Complete File Structure

```
student-tracker-portal/
│
├── 🐍 PYTHON MODULES (Core Application)
│   ├── app.py                    (Flask web server + routes)
│   ├── models.py                 (OOP: Person, Student, Course, GradeBook)
│   ├── database.py               (SQLite operations)
│   ├── analytics.py              (Data analysis + ML prediction)
│   ├── sample_data.py            (Generate demo data)
│   ├── config.py                 (Configuration & constants)
│   └── requirements.txt          (Python dependencies)
│
├── 🚀 STARTUP SCRIPTS
│   ├── run.bat                   (Windows batch script)
│   └── run.sh                    (Linux/Mac shell script)
│
├── 📖 DOCUMENTATION
│   ├── README.md                 (Full project documentation)
│   ├── SETUP_GUIDE.md            (Setup & run instructions)
│   └── INDEX.md                  (This file)
│
├── 🌐 TEMPLATES (HTML pages - 12 files)
│   ├── base.html                 (Navigation & layout)
│   ├── index.html                (Dashboard)
│   ├── students.html             (Students list)
│   ├── student_detail.html       (Student profile)
│   ├── courses.html              (Courses list)
│   ├── course_detail.html        (Course analytics)
│   ├── analytics.html            (Analytics dashboard)
│   ├── predictions.html          (AI prediction page)
│   ├── reports.html              (Reports & exports)
│   ├── about.html                (Project info)
│   ├── 404.html                  (Error page)
│   └── 500.html                  (Server error)
│
└── 🎨 STATIC FILES (CSS + JS)
    ├── style.css                 (Custom styling)
    └── script.js                 (Client-side functions)

```

---

## 📊 Project Overview

**Project ID:** TEC004/05  
**Title:** University Course Performance Tracker & Grade Prediction System  
**Type:** Full-stack Web Application  
**Status:** ✅ Complete & Ready to Run

---

## 🎯 What's Included

### 1️⃣ Backend (Python)
- **OOP Architecture** with abstract classes and inheritance
- **SQLite Database** with relational schema
- **Data Analytics** using Pandas
- **Machine Learning** grade prediction
- **Flask Web Server** with REST API

### 2️⃣ Frontend (Web)
- **12 HTML Templates** with Bootstrap styling
- **Custom CSS** for modern UI
- **Chart.js** for data visualization
- **JavaScript** utilities for interactivity

### 3️⃣ Core Features
✅ Student management system  
✅ Course management  
✅ Grade tracking & analysis  
✅ GPA calculations  
✅ At-risk student detection  
✅ Grade prediction model  
✅ Real-time analytics  
✅ Performance reports  

---

## 🚀 Getting Started

### Windows Users
```bash
run.bat
```

### macOS/Linux Users
```bash
chmod +x run.sh
./run.sh
```

### Manual Start
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Generate sample data
python sample_data.py

# Run application
python app.py
```

Then open: **http://localhost:5000**

---

## 📖 File Descriptions

### Python Modules

#### `app.py` (350+ lines)
- Flask application server
- 15+ route handlers
- REST API endpoints
- JSON responses
- Error handlers
- Template rendering

#### `models.py` (200+ lines)
- Abstract `Person` class
- `Student` class with GPA calculation
- `Instructor` class
- `Course` class with enrollment
- `WeightedGradeBook` (30/40/30)
- `CurvedGradeBook` (1.05 factor)
- `PassFailGradeBook` (binary)

#### `database.py` (300+ lines)
- SQLite connection management
- Table creation & schema
- CRUD operations (Create, Read, Update, Delete)
- Complex SQL queries
- GPA calculations
- At-risk student identification

#### `analytics.py` (400+ lines)
- Pandas-based analysis
- Statistical calculations
- Grade distributions
- Correlation analysis
- Linear Regression prediction
- Model persistence
- Visualization data preparation

#### `sample_data.py` (100+ lines)
- 4 instructors
- 6 courses
- 10 students
- 40+ grade records
- Realistic data patterns
- Reproducible with seed

#### `config.py` (100+ lines)
- Configuration constants
- Grade thresholds
- Grading weights
- Database settings
- Quick start guide

### HTML Templates

#### `base.html`
Main layout with:
- Navigation bar
- Bootstrap framework
- CSS/JS includes
- Block template structure

#### `index.html`
Dashboard with:
- System statistics
- Top performers
- Quick stats
- Navigation links

#### `students.html`
Students list with:
- Sortable table
- GPA badges
- Student links
- 10 demo students

#### `student_detail.html`
Student profile with:
- Personal info
- Academic stats
- Enrolled courses
- Grade breakdown

#### `courses.html`
Courses list with:
- Course cards
- Enrollment count
- Average grades
- Pass rates

#### `course_detail.html`
Course analytics with:
- Class statistics
- Correlation analysis
- Grade table
- At-risk alerts

#### `analytics.html`
Analytics dashboard with:
- Bar charts
- At-risk students
- Performance metrics
- System insights

#### `predictions.html`
AI prediction form with:
- Midterm input
- Assignment input
- Prediction display
- Risk alerts
- Model explanation

#### `reports.html`
Reports page with:
- Summary statistics
- Export buttons
- At-risk reports
- System overview

#### `about.html`
Project information with:
- Project description
- Technology stack
- Learning outcomes
- Development phases

#### `404.html` & `500.html`
Error pages with links home

### CSS & JavaScript

#### `style.css` (400+ lines)
- Bootstrap integration
- Custom components
- Card styles
- Table styling
- Button themes
- Badge colors
- Responsive design
- Animations

#### `script.js` (300+ lines)
- Chart creation functions
- API calls
- Data formatting
- Toast notifications
- Form validation
- Export functions
- Utility functions

---

## 📊 Database Schema

### Tables (7 total)

1. **students** - Student records with GPA
2. **instructors** - Faculty information
3. **courses** - Course details & grading scheme
4. **enrollments** - Student-course relationships
5. **grades** - Student grades (midterm, final, assignments)
6. **assignments** - Assignment details
7. **assignment_submissions** - Student submissions

---

## 🤖 AI Features

### Prediction Model
- Algorithm: Linear Regression
- Features: Midterm score, Assignment score
- Target: Final grade
- Training: Historical data
- Output: Predicted grade + confidence

### Model File
- Format: Pickle (.pkl)
- Location: `grade_prediction_model.pkl`
- Auto-saved after training

### Prediction API
```
POST /api/predict
{
  "midterm": 85,
  "assignments": 80
}

Response:
{
  "predicted_grade": 82.5,
  "confidence": 0.85,
  "midterm_weight": 0.45,
  "assignments_weight": 0.55
}
```

---

## 📱 Web Interface

### Pages & Routes
- `/` - Dashboard
- `/students` - Student list
- `/student/<id>` - Student profile
- `/courses` - Course list
- `/course/<id>` - Course detail
- `/analytics` - Analytics dashboard
- `/predictions` - Prediction tool
- `/reports` - Reports page
- `/about` - About project

### API Endpoints
- `POST /api/predict` - Grade prediction
- `GET /api/grade-distribution/<course_id>`
- `GET /api/student-trend/<student_id>`
- `GET /api/course-stats/<course_id>`
- `GET /api/at-risk-students`
- `GET /api/top-performers`

---

## 🎓 Learning Outcomes

By exploring this project, you'll learn:

✅ **Object-Oriented Programming**
- Abstract classes & inheritance
- Polymorphism & method overriding
- Encapsulation principles

✅ **Database Design**
- Relational database schema
- Foreign keys & relationships
- SQL queries & joins
- CRUD operations

✅ **Web Development**
- Flask framework
- MVC architecture
- Template rendering
- REST APIs

✅ **Data Science**
- Pandas DataFrames
- Statistical analysis
- Machine learning basics
- Data visualization

✅ **Full-Stack Development**
- Backend server logic
- Frontend UI/UX
- Client-server communication
- Responsive design

---

## 🛠️ Technology Stack

### Backend
- Python 3.8+
- Flask 2.3.3
- SQLite 3
- Pandas 2.0.3
- Scikit-learn 1.3.0
- NumPy 1.24.3

### Frontend
- HTML5
- Bootstrap 5.1.3
- Chart.js 3.7.0
- JavaScript (Vanilla)
- Font Awesome 6.0.0

---

## 💾 Database Size

- **Students**: 10 records
- **Courses**: 6 records
- **Instructors**: 4 records
- **Enrollments**: ~45 records
- **Grades**: ~45 records
- **Total**: ~115 records
- **File Size**: ~50-100 KB

---

## 🧪 Demo Data Highlights

### Realistic Grades
- Correlations between midterm and final
- Assignment completion patterns
- Course difficulty variations
- Some at-risk students
- Clear top performers

### Ready to Test
- Prediction model pre-trained
- Analytics fully functional
- All reports generated
- Search & filter ready

---

## 🔒 Security Notes

⚠️ **Current Status**: Educational/Demonstration

### For Production:
- Implement user authentication
- Add password hashing (bcrypt)
- Enable HTTPS/SSL
- Validate all inputs
- Implement rate limiting
- Use environment variables
- Add CSRF protection
- Enable CORS properly

---

## 📋 Deployment Checklist

- [ ] Set `debug=False` in app.py
- [ ] Use environment variables for secrets
- [ ] Enable HTTPS
- [ ] Add authentication system
- [ ] Implement rate limiting
- [ ] Add error logging
- [ ] Optimize database queries
- [ ] Minify CSS/JS
- [ ] Set up backups
- [ ] Configure monitoring

---

## 🆘 Support

### Common Issues & Solutions
See **SETUP_GUIDE.md** for troubleshooting

### Documentation
- **README.md** - Complete overview
- **SETUP_GUIDE.md** - Installation & setup
- **INDEX.md** - This file
- Code comments throughout

---

## 🎉 Ready to Start?

### Quick Run:
```bash
run.bat          # Windows
./run.sh         # macOS/Linux
```

### Then Open:
```
http://localhost:5000
```

---

**Created for Project TEC004/05**  
**Happy Learning! 🚀**
