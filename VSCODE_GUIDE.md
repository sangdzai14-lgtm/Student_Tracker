# 🚀 VS Code Quick Start Guide

## ⚡ Running the Portal in VS Code

### Method 1: Using Run & Debug (Easiest)

1. **Open the project folder** in VS Code
   ```
   File → Open Folder → student-tracker-portal
   ```

2. **Open the Command Palette** (Ctrl+Shift+P)
   ```
   Ctrl+Shift+P
   ```

3. **Run the Flask server**
   ```
   Type: Run and Debug
   Select: 🚀 Flask - Run Portal
   ```

4. **Open browser**
   ```
   http://localhost:5000
   ```

---

## 📋 Available VS Code Tasks

Open Command Palette: **Ctrl+Shift+P** and type "Run Task"

### Task Options:

1. **🚀 Run Portal (Full Setup)**
   - Generates sample data
   - Use this first time

2. **🌐 Start Flask Server**
   - Starts the web server
   - Runs in background
   - Shows server output

3. **📊 Generate Sample Data**
   - Creates demo students/courses
   - Use if database is empty

4. **🔄 Reset Database & Regenerate**
   - Deletes old database
   - Creates fresh data
   - Use to reset everything

5. **📦 Install Dependencies**
   - Installs Python packages
   - Use if pip install not done

---

## 🔧 Available Debug Configurations

Open Run and Debug: **Ctrl+Shift+D** or click the Run icon in left sidebar

### Available Launches:

1. **🚀 Flask - Run Portal**
   - Recommended for production
   - Full Flask debugging
   - Breakpoints work

2. **🐍 Python - Run app.py**
   - Direct Python execution
   - Simple debugging
   - Shows all output

3. **📊 Generate Sample Data**
   - Test data generation
   - Debug sample_data.py

4. **🧪 Test Models**
   - Debug OOP models
   - Test class definitions

5. **💾 Test Database**
   - Debug database operations
   - Test SQL queries

6. **📈 Test Analytics**
   - Debug analytics functions
   - Test predictions

---

## 🎯 Step-by-Step: First Run

### Step 1: Open Project
```
File → Open Folder → student-tracker-portal
```

### Step 2: Install Dependencies
```
Ctrl+Shift+P → Run Task → 📦 Install Dependencies
```
Wait for completion (~2 minutes)

### Step 3: Generate Sample Data
```
Ctrl+Shift+P → Run Task → 📊 Generate Sample Data
```
Wait for completion (should show ✓)

### Step 4: Start the Server
```
Ctrl+Shift+D → Select 🚀 Flask - Run Portal → Click Play
```

### Step 5: Open Browser
```
http://localhost:5000
```

You should see the Student Portal dashboard! 🎓

---

## 🖥️ Terminal Commands (Alternative)

If you prefer to use the terminal directly:

### Open Integrated Terminal
```
Ctrl+` (backtick)
```

### Run commands:
```bash
# Install dependencies
pip install -r requirements.txt

# Generate sample data
python sample_data.py

# Start Flask server
python app.py
```

The server will start on `http://localhost:5000`

---

## 🐛 Debugging Features

### Setting Breakpoints
1. Click on line number to set breakpoint (red dot appears)
2. Run debug configuration
3. Click "Continue" when breakpoint hit

### Debug Panel (Ctrl+Shift+D)
- Variables view (see all variables)
- Watch expressions (monitor values)
- Call stack (see function calls)
- Debug console (run Python code)

### Example: Debug Grade Calculation
1. Open `models.py`
2. Find `calculate_final_grade()` method
3. Click line number to set breakpoint
4. Run Flask debugger
5. Access a student page in browser
6. Debugger will pause at breakpoint

---

## 🔌 Stopping the Server

### Method 1: Click Stop Button
- Click red stop button in toolbar (Ctrl+Shift+F5)

### Method 2: Terminal
```
Ctrl+C in the terminal
```

### Method 3: Terminal Tab
- Click X on the terminal tab

---

## 📊 Useful VS Code Extensions

When VS Code opens, you'll see a recommendation popup. Click "Install" on:

- **Python** (ms-python.python) - Python support
- **Pylance** (ms-python.vscode-pylance) - IntelliSense
- **Live Server** (ritwickdey.LiveServer) - Preview HTML files
- **REST Client** - Test API endpoints

---

## 💡 Pro Tips

### Tip 1: Multi-Window Terminal
Use multiple terminal tabs:
```
Ctrl+Shift+` → Opens new terminal tab
```

### Tip 2: Debug Console
Use the Debug Console to test code:
```python
# In Debug Console, type:
db.get_all_students()
analytics.get_course_statistics('CS101')
```

### Tip 3: Watch Variables
Add variables to watch:
1. Open Debug → Variables panel
2. Right-click variable
3. Select "Add to Watch"

### Tip 4: Conditional Breakpoints
Right-click breakpoint → "Add Conditional Breakpoint"
```
student.gpa > 3.5
```

### Tip 5: Python Interactive
Open Python Interactive:
```
Ctrl+Shift+P → Python: Start REPL
```

Then test code directly:
```python
from models import Student
s = Student('001', 'Test', 'test@test.com')
print(s.name)
```

---

## 🆘 Troubleshooting

### Issue: "Python not found"
**Solution:** Select Python interpreter
```
Ctrl+Shift+P → Python: Select Interpreter
Choose your Python version
```

### Issue: "Module not found"
**Solution:** Install dependencies
```
Run Task → 📦 Install Dependencies
```

### Issue: Port 5000 in use
**Solution:** Edit app.py, change port:
```python
app.run(debug=True, port=5001)
```

### Issue: Database locked
**Solution:** Reset database
```
Run Task → 🔄 Reset Database & Regenerate
```

### Issue: Flask not starting
**Solution:** Check Python version
```
Ctrl+` → python --version
Should be 3.8 or higher
```

---

## 🎓 Learning Path

### Day 1: Setup & Explore
1. Run the portal
2. Explore all pages
3. Review student data
4. Check course analytics

### Day 2: Debug Code
1. Set breakpoint in `models.py`
2. Debug a prediction
3. Watch variables
4. Use debug console

### Day 3: Modify & Extend
1. Add new route in `app.py`
2. Modify database query in `database.py`
3. Run tests with debugger
4. See changes live

---

## 🚀 Next Steps

1. **Explore Code Structure**
   - Open `app.py` to see routes
   - Open `models.py` to see OOP
   - Open `analytics.py` to see ML

2. **Customize Data**
   - Edit `sample_data.py`
   - Add more students
   - Modify grades
   - Run `📊 Generate Sample Data` task

3. **Add Features**
   - Create new route in `app.py`
   - Add new template in `templates/`
   - Test with debugger
   - See live in browser

4. **Deploy**
   - Set `debug=False` in app.py
   - Use gunicorn for production
   - Deploy to cloud platform

---

**Enjoy developing! 🎉**
