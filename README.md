# 🎓 Student Academic Portal
## University Course Performance Tracker & Grade Prediction System

### Project ID: TEC004/05

A comprehensive Python web application for managing student academic records, analyzing grade data, and predicting final grades using machine learning.

---

## 📋 Features

### ✅ Core Functionality
- **OOP Grade Management System** - Abstract class hierarchy with Students, Instructors, and Courses
- **Multiple Grading Schemes** - Weighted, curved, and pass/fail grading systems
- **SQLite Database** - Relational database with Students, Courses, Grades, Enrollments tables
- **File I/O Operations** - Import/export grades from CSV and JSON
- **Data Analytics** - Pandas-based statistical analysis
- **Data Visualization** - Chart.js for grade distributions and trends
- **AI Grade Prediction** - Linear Regression model for predicting final grades
- **At-Risk Student Alerts** - Automatic identification of struggling students
- **Web Portal** - Flask-based responsive web interface

### 🕷️ Live Data Pipeline (New!)
- **Web Scraping (Week 6)** - Automated extraction of exam results from Bac Duy University Portal
- **Data Cleaning** - Regex-based normalization of academic metadata
- **Data Persistence** - Structured storage in JSON and CSV formats
- **Advanced Analysis (Week 7)** - Pandas-based market descriptive statistics and segmentation
- **Automated Visualization** - Real-time generation of score distribution and performance graphs

### 📊 Analytics Dashboard
- Real-time grade statistics
- Course performance metrics
- Student GPA calculations
- At-risk student detection
- Top performer rankings
- Correlation analysis

### 🤖 AI Features
- Grade prediction based on midterm and assignment scores
- Historical pattern analysis
- Risk assessment models
- Student intervention recommendations

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser

### Step 1: Clone/Download Project
```bash
cd student-tracker-portal
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Generate Sample Data
```bash
python sample_data.py
```

### Step 5: Run the Application
```bash
python app.py
```

The application will start at `http://localhost:5000`

---

## 🚀 Usage

### Accessing the Portal
1. Open your web browser
2. Navigate to `http://localhost:5000`
3. Explore the dashboard and available features

### Main Features

#### 📚 Students Page
- View all students
- Filter by major or GPA
- Click on student name to view detailed performance

#### 📖 Courses Page
- Browse all courses
- View course statistics
- Check enrollment and pass rates

#### 📊 Analytics Dashboard
- Real-time performance metrics
- Identify at-risk students
- Analyze grade distributions
- Course difficulty comparison

#### 🧠 Grade Prediction
- Input midterm score and assignment completion
- Get AI-powered final grade prediction
- Receive at-risk alerts

#### 📈 Reports
- Generate comprehensive reports
- Export student and course data
- System-wide performance analysis

---

## 📂 Project Structure

```
student-tracker-portal/
├── app.py                    # Flask application
├── models.py                 # OOP classes (Person, Student, Course, GradeBook)
├── scraper.py                # Web scraper for PTIT exam data (Week 6)
├── data_processor.py         # Data cleaning and processing (Week 6)
├── data_persistence.py       # JSON/CSV storage operations (Week 6)
├── pipeline.py               # Complete scraper-to-analysis orchestrator (Week 6/7)
├── analysis.py               # Pandas DataFrame analysis portal (Week 7)
├── database.py               # SQLite database operations
├── analytics.py              # Data analysis and predictions
├── sample_data.py            # Demo data generator
├── requirements.txt          # Python dependencies
├── templates/
│   ├── base.html            # Base template
│   ├── index.html           # Dashboard (updated with pipeline info)
│   ├── scraper.html         # Live scraper interface
│   ├── analysis.html        # Pandas analysis portal
│   ├── students.html        # Students list
│   ├── student_detail.html  # Student details
│   ├── courses.html         # Courses list
│   ├── course_detail.html   # Course details
│   ├── analytics.html       # Analytics dashboard
│   ├── predictions.html     # Grade prediction
│   ├── reports.html         # Reports
│   ├── about.html           # About page
│   ├── 404.html             # Not found
│   └── 500.html             # Server error
├── static/
│   ├── style.css            # Custom CSS
│   └── script.js            # JavaScript utilities
└── README.md                # This file
```

---

## 🎯 Project Phases

### Phase 1: System Design & Database (Completed)
- ✅ OOP hierarchy design
- ✅ SQLite schema creation
- ✅ CRUD operations
- ✅ Access control decorators

### Phase 2: Analytics & Visualization (Completed)
- ✅ Pandas data analysis
- ✅ Grade statistics
- ✅ Chart.js visualizations
- ✅ Multi-threaded processing

### Phase 3: AI & Final Integration (Completed)
- ✅ Grade prediction model
- ✅ At-risk alerts
- ✅ Web interface
- ✅ System testing

### Phase 4: Web Scraping & Live Pipeline (New - Week 6 & 7)
- ✅ **Week 6**: Automated Web Scraper for Bac Duy University AI results
- ✅ **Week 6**: Data cleaning and persistence (JSON/CSV)
- ✅ **Week 7**: Pandas DataFrame analysis portal
- ✅ **Week 7**: Advanced statistical visualization

---

## 🔧 Technical Stack

### Backend
- **Python 3.8+** - Core programming language
- **Flask** - Web framework
- **SQLite** - Database
- **Pandas** - Data analysis
- **Scikit-learn** - Machine learning
- **NumPy** - Numerical computing

### Frontend
- **HTML5** - Markup
- **Bootstrap 5** - CSS framework
- **Chart.js** - Data visualization
- **JavaScript** - Client-side logic

---

## 📊 Database Schema

### Students Table
- student_id (PK)
- name
- email
- major
- gpa
- created_at

### Courses Table
- course_id (PK)
- course_name
- credits
- instructor_id (FK)
- grading_scheme
- created_at

### Grades Table
- grade_id (PK)
- student_id (FK)
- course_id (FK)
- midterm
- final
- assignments
- final_grade
- letter_grade
- recorded_date

### Enrollments Table
- enrollment_id (PK)
- student_id (FK)
- course_id (FK)
- enrollment_date

---

## 🎓 Learning Outcomes

After completing this project, students will understand:

✅ **Object-Oriented Programming**
- Abstract classes and inheritance
- Polymorphism and method overriding
- Design patterns

✅ **Database Management**
- Relational database design
- SQL queries and joins
- Transaction management

✅ **Data Science**
- Statistical analysis with Pandas
- Data visualization
- Machine learning basics

✅ **Web Development**
- Flask web framework
- HTML/CSS/JavaScript
- RESTful API design

✅ **Software Engineering**
- Version control
- Documentation
- Testing and debugging

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port in app.py
app.run(debug=True, port=5001)
```

### Database Issues
```bash
# Reset database
rm student_tracker.db
python sample_data.py
```

### Missing Dependencies
```bash
pip install -r requirements.txt --force-reinstall
```

---

## 📝 Sample Data

The system comes with pre-populated demo data:
- 10 students from various majors
- 6 courses across multiple departments
- 4 instructors
- Realistic grade data with correlations
- At-risk students for testing

---

## 🔐 Security Notes

- This is a demonstration/educational system
- For production use:
  - Implement user authentication
  - Add HTTPS/SSL encryption
  - Use environment variables for secrets
  - Implement input validation
  - Add rate limiting

---

## 📞 Support & Documentation

- For questions about OOP concepts, see `models.py`
- For database operations, see `database.py`
- For analytics, see `analytics.py`
- For Flask routing, see `app.py`

---

## 📄 License

This project is created for educational purposes as part of the TEC004/05 curriculum.

---

## ✨ Future Enhancements

- [ ] User authentication system
- [ ] Advanced search filters
- [ ] Export to PDF reports
- [ ] Email notifications
- [ ] Mobile app version
- [ ] Real-time collaboration
- [ ] Advanced ML models
- [ ] Attendance tracking
- [ ] Parent portal access

---

**Happy Learning! 🚀**
