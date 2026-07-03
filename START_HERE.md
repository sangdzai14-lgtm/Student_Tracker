# 🎓 START HERE - VS Code Live Development

## ⚡ 60-Second Quick Start

### Step 1: Open Folder (10 seconds)
```
File → Open Folder → student-tracker-portal
```

### Step 2: Press Debug Button (5 seconds)
```
Ctrl+Shift+D
```

### Step 3: Select Configuration (5 seconds)
```
Click dropdown → Select "🚀 Flask - Run Portal"
```

### Step 4: Click Play (5 seconds)
```
Press F5 or click Play button
```

### Step 5: Open Browser (10 seconds)
```
http://localhost:5000
```

### Step 6: Explore! (20 seconds)
- Click on Students
- View course details
- Test grade prediction
- Check analytics

---

## 🎯 What Happens When You Click Play

1. **Python Environment** - Loads Flask
2. **Database** - Loads student/course data
3. **Server Starts** - Runs on port 5000
4. **Browser Ready** - Connects to http://localhost:5000
5. **Debugging Enabled** - Can set breakpoints

---

## 📊 The Portal Opens With:

- 10 Sample Students
- 6 Different Courses
- 4 Instructors
- 45+ Grade Records
- AI Grade Prediction Model
- Real-time Analytics

---

## 🔧 What's Configured for You

### ✅ VS Code is Ready With:

- **Debug Configurations** - 6 different run options
- **Tasks** - Run setup, server, generate data
- **Python Support** - IntelliSense, formatting
- **Extensions** - Recommended plugins
- **Settings** - Optimized for this project

### ✅ Project is Ready With:

- **OOP Classes** - Person, Student, Course, GradeBook
- **SQLite Database** - Relational schema
- **Analytics Engine** - Grade prediction
- **Web Interface** - Bootstrap + Chart.js
- **Sample Data** - Real demo students

---

## 🎮 Key Shortcuts to Know

| What | Shortcut |
|------|----------|
| Run the app | `Ctrl+Shift+D` then `F5` |
| Stop the app | `Ctrl+Shift+F5` |
| Open terminal | ``Ctrl+` `` |
| Open command palette | `Ctrl+Shift+P` |
| Debug console | `Ctrl+Shift+Y` |
| Set breakpoint | Click line number |

---

## 📋 First Things to Try

### 1. View Student Performance
1. Go to http://localhost:5000/students
2. Click "Alice Johnson" (top student)
3. See her courses and grades

### 2. Analyze a Course
1. Go to http://localhost:5000/courses
2. Click "CS101: Introduction to Programming"
3. View all student grades in course

### 3. Predict a Grade
1. Go to http://localhost:5000/predictions
2. Enter Midterm: 85
3. Enter Assignments: 80
4. See predicted final grade

### 4. Check At-Risk Students
1. Go to http://localhost:5000/analytics
2. Scroll down to see at-risk list
3. Click student name to see details

---

## 🐛 Debugging During Development

### To Debug Code:

1. **Set Breakpoint**
   - Click on line number in editor
   - Red dot appears

2. **Run App**
   - Press F5 (or Ctrl+Shift+D → Flask → Play)

3. **Trigger Code**
   - Click link in browser
   - Debugger pauses at breakpoint

4. **Inspect Variables**
   - Look at Variables panel (left sidebar)
   - Hover over variables in code
   - Type in Debug Console

5. **Step Through Code**
   - F10 = next line
   - F11 = go into function
   - Shift+F11 = exit function

### Example: Debug Student Grades
1. Open `models.py`
2. Find `add_grade()` method
3. Click line number to set breakpoint
4. Press F5 to start debugging
5. Go to student page in browser
6. Debugger pauses - inspect grades!

---

## 🌐 Available Pages

Click these links once server is running:

- [Dashboard](http://localhost:5000/) - Overview
- [Students](http://localhost:5000/students) - All students
- [Courses](http://localhost:5000/courses) - All courses
- [Analytics](http://localhost:5000/analytics) - Performance metrics
- [Predictions](http://localhost:5000/predictions) - AI grade prediction
- [Reports](http://localhost:5000/reports) - System reports
- [About](http://localhost:5000/about) - Project info

---

## 📂 File Organization

```
Root Files:
├── app.py              ← Main server (edit here for new features)
├── models.py           ← OOP classes (edit here for logic)
├── database.py         ← Database queries (edit here for data)
├── analytics.py        ← Data analysis (edit here for ML)
└── requirements.txt    ← Python packages

Templates (HTML):
├── templates/index.html           ← Dashboard
├── templates/students.html        ← Students list
├── templates/student_detail.html  ← Student profile
├── templates/courses.html         ← Courses list
├── templates/course_detail.html   ← Course analytics
├── templates/analytics.html       ← Analytics
├── templates/predictions.html     ← AI predictions
└── templates/base.html            ← Base layout

Styling & UI:
├── static/style.css       ← Custom CSS
└── static/script.js       ← JavaScript

VS Code Config:
└── .vscode/
    ├── launch.json        ← Debug configurations
    ├── tasks.json         ← Task definitions
    ├── settings.json      ← VS Code settings
    └── extensions.json    ← Recommended extensions

Documentation:
├── README.md              ← Full documentation
├── VSCODE_GUIDE.md       ← Detailed VS Code setup
├── VSCODE_QUICK_REF.md   ← Quick reference
└── SETUP_GUIDE.md        ← Installation guide
```

---

## 🎓 Learning Path

### Hour 1: Explore
- Run the app
- Click around all pages
- Check out student data
- View course analytics

### Hour 2: Read Code
- Open `app.py` - see Flask routes
- Open `models.py` - see OOP classes
- Open `database.py` - see SQL queries
- Understand architecture

### Hour 3: Debug
- Set breakpoints
- Run app with debugger
- Step through code
- Inspect variables

### Hour 4: Modify
- Add new route in `app.py`
- Edit template
- Create new feature
- Test with debugger

---

## 🚀 Next Steps

1. **Run the app now**
   - `Ctrl+Shift+D` → Select Flask → F5

2. **Explore the interface**
   - Visit all pages
   - Check student profiles
   - Test predictions

3. **Review the code**
   - Read through each file
   - Understand architecture
   - Review patterns

4. **Try debugging**
   - Set a breakpoint
   - Step through code
   - Watch variables

5. **Add a feature**
   - Create new route
   - Add new template
   - Connect to database

---

## 🆘 Troubleshooting

### App won't start?
```
Check: 
1. Python installed? python --version
2. Port free? netstat -ano | findstr :5000
3. Dependencies? Ctrl+Shift+P → Run Task → Install Dependencies
```

### Breakpoints not working?
```
Make sure:
1. Debug configuration is "Flask" not "Python"
2. You pressed F5 to start debugger
3. VS Code shows "Debugging" in bottom bar
```

### Database issues?
```
Reset it:
Ctrl+Shift+P → Run Task → 🔄 Reset Database & Regenerate
```

### Port 5000 in use?
```
Edit app.py:
Change: app.run(debug=True, port=5000)
To:     app.run(debug=True, port=5001)
```

---

## 💡 Pro Tips

1. **Use Multiple Terminals**
   - Press ``Ctrl+Shift+` `` multiple times
   - One for server, one for monitoring

2. **Watch Variables**
   - Debug panel → Variables
   - Right-click → Add to Watch
   - Always see values

3. **Use Debug Console**
   - Type Python directly
   - Test queries
   - Inspect objects

4. **Search in Files**
   - `Ctrl+Shift+F` - Find everywhere
   - Find all references

5. **Git Integration**
   - Side panel → Source Control
   - Commit, push, track changes

---

## 📞 Need Help?

**Quick Reference:** `VSCODE_QUICK_REF.md`  
**Full Guide:** `VSCODE_GUIDE.md`  
**Full Docs:** `README.md`  
**Setup Help:** `SETUP_GUIDE.md`  

---

## ✨ You're All Set!

Everything is configured. Just:

1. Open folder in VS Code
2. Press `Ctrl+Shift+D`
3. Click Play
4. Wait 5 seconds
5. Open `http://localhost:5000`

**Enjoy! 🎉**
