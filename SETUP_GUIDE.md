# 🚀 Student Academic Portal - Setup & Run Guide

## ⚡ Quick Start (Windows)

### Option 1: Automatic Setup (Easiest)
```bash
run.bat
```
The batch file will automatically:
- Create virtual environment
- Install dependencies
- Generate sample data
- Start the Flask server

### Option 2: Manual Setup

1. **Open Command Prompt** in the project folder

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate Sample Data**
   ```bash
   python sample_data.py
   ```

5. **Run Application**
   ```bash
   python app.py
   ```

---

## ⚡ Quick Start (macOS/Linux)

### Option 1: Automatic Setup
```bash
chmod +x run.sh
./run.sh
```

### Option 2: Manual Setup
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Generate sample data
python3 sample_data.py

# Run application
python3 app.py
```

---

## 🌐 Access the Portal

Once the server is running, open your browser and navigate to:

```
http://localhost:5000
```

### Available Pages:
- **Dashboard** - http://localhost:5000/
- **Students** - http://localhost:5000/students
- **Courses** - http://localhost:5000/courses
- **Analytics** - http://localhost:5000/analytics
- **Predictions** - http://localhost:5000/predictions
- **Reports** - http://localhost:5000/reports
- **About** - http://localhost:5000/about

---

## 📊 Using the Portal

### 1. Dashboard
- View system overview
- Check total students and courses
- See at-risk student count
- View top performers

### 2. Students Page
- Browse all students
- View GPA and major
- Click on student name for detailed view
- Check enrolled courses and grades

### 3. Student Detail Page
- View complete academic record
- See all enrolled courses
- Check grade breakdown (Midterm, Assignments, Final)
- View individual course performance

### 4. Courses Page
- Browse all courses
- View enrollment statistics
- Check average grades
- See pass rates

### 5. Course Detail Page
- View enrolled students
- Check grade statistics
- Analyze midterm-final correlation
- Review individual student grades

### 6. Analytics Dashboard
- Course performance overview (chart)
- At-risk students list
- Real-time statistics
- Performance insights

### 7. Grade Prediction
- Input midterm score (0-100)
- Input assignment score (0-100)
- Get predicted final grade
- View at-risk alerts
- Check model weights

### 8. Reports
- System summary statistics
- At-risk student report
- Export functionality

---

## 🧪 Testing the Application

### Try These Actions:

1. **View Student Performance**
   - Go to Students page
   - Click on "Alice Johnson" (top student, ~90 GPA)
   - Compare with "Frank Davis" (at-risk student)

2. **Analyze Course Difficulty**
   - Go to Courses page
   - Compare average grades across courses
   - Note which courses are most challenging

3. **Predict Grades**
   - Go to Predictions page
   - Try different scenarios:
     - Midterm: 75, Assignments: 75 → ~Expected C range
     - Midterm: 85, Assignments: 85 → ~Expected B range
     - Midterm: 95, Assignments: 95 → ~Expected A range

4. **Identify At-Risk Students**
   - Go to Analytics
   - Check at-risk students list
   - Review intervention recommendations

---

## 🔧 Troubleshooting

### Issue 1: "Port 5000 already in use"
**Solution:** Edit `app.py` line near end:
```python
# Change from:
app.run(debug=True, port=5000)
# To:
app.run(debug=True, port=5001)
```

### Issue 2: "ModuleNotFoundError: No module named 'flask'"
**Solution:** Make sure virtual environment is activated:
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

Then reinstall dependencies:
```bash
pip install -r requirements.txt
```

### Issue 3: Database errors or missing data
**Solution:** Regenerate sample data:
```bash
# Delete old database
rm student_tracker.db

# Generate new data
python sample_data.py
```

### Issue 4: Module import errors
**Solution:** Verify you're in the project directory:
```bash
cd student-tracker-portal
python app.py
```

### Issue 5: Permission denied (macOS/Linux)
**Solution:** Make run script executable:
```bash
chmod +x run.sh
./run.sh
```

---

## 📝 Project Files Overview

| File | Purpose |
|------|---------|
| `app.py` | Main Flask application with all routes |
| `models.py` | OOP classes: Person, Student, Instructor, Course, GradeBook |
| `database.py` | SQLite database operations |
| `analytics.py` | Data analysis and grade prediction model |
| `sample_data.py` | Generates demo data for testing |
| `config.py` | Configuration constants and quick start guide |
| `requirements.txt` | Python package dependencies |
| `run.bat` | Windows startup script |
| `run.sh` | Linux/Mac startup script |
| `README.md` | Full project documentation |

---

## 🎓 Learning Paths

### Learn OOP Concepts
1. Open `models.py`
2. Study the `Person` abstract class
3. Review `Student`, `Instructor`, and `Course` classes
4. Analyze the three `GradeBook` implementations

### Learn Database Design
1. Open `database.py`
2. Review the SQLite schema
3. Study the CRUD operations
4. Check complex queries (GPA calculation, at-risk students)

### Learn Web Development
1. Open `app.py`
2. Study Flask routes
3. Review template rendering
4. Check JSON API endpoints

### Learn Data Science
1. Open `analytics.py`
2. Review statistical functions
3. Study prediction model
4. Check data visualization preparation

---

## 🌟 Sample Data Details

**Students:**
- Alice Johnson (90+ GPA, top performer)
- Bob Smith, Carol White, David Lee, Emma Brown
- Frank Davis (at-risk, <70 average)
- Grace Miller, Henry Wilson, Ivy Moore
- Jack Taylor

**Courses:**
- CS101: Introduction to Programming
- CS201: Data Structures
- MATH101: Calculus I
- MATH201: Linear Algebra
- PHY101: Physics I
- CHEM101: Chemistry Fundamentals

**Instructors:**
- Dr. John Smith (Computer Science)
- Prof. Sarah Johnson (Mathematics)
- Dr. Michael Chen (Physics)
- Dr. Emily Davis (Chemistry)

---

## 🔄 Stopping the Server

Press **Ctrl+C** in the terminal/command prompt where the server is running.

---

## 📚 Next Steps

1. **Explore the Code**
   - Read through each Python module
   - Understand the OOP architecture
   - Review the database design

2. **Experiment**
   - Modify sample data in `sample_data.py`
   - Add new grading schemes in `models.py`
   - Create new analytics functions in `analytics.py`

3. **Extend Features**
   - Add student authentication
   - Create export to PDF
   - Add email notifications
   - Implement real-time updates

4. **Production Deployment**
   - Add security measures
   - Implement user authentication
   - Use environment variables
   - Set up HTTPS/SSL
   - Deploy to cloud platform

---

## 🆘 Need Help?

1. Check `README.md` for detailed documentation
2. Review `config.py` for quick start guide
3. Read inline code comments
4. Check Flask and Pandas documentation online

---

**Enjoy using the Student Academic Portal! 🎓📊**
