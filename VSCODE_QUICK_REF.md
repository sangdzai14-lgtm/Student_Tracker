# 🎯 VS Code Quick Reference Card

## ⚡ FASTEST WAY TO RUN

1. **Open Folder** in VS Code
   ```
   File → Open Folder → student-tracker-portal
   ```

2. **Press** `Ctrl+Shift+D` (Run & Debug)

3. **Select** `🚀 Flask - Run Portal`

4. **Click** Play button (or press F5)

5. **Open Browser**
   ```
   http://localhost:5000
   ```

---

## 🎮 Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Open Command Palette | `Ctrl+Shift+P` |
| Run & Debug | `Ctrl+Shift+D` |
| Run Task | `Ctrl+Shift+P` then type "Run Task" |
| Stop Debugging | `Ctrl+Shift+F5` |
| Open Terminal | ``Ctrl+` `` |
| New Terminal Tab | `Ctrl+Shift+` `` |
| Go to File | `Ctrl+P` |
| Find | `Ctrl+F` |
| Replace | `Ctrl+H` |
| Debug Console | `Ctrl+Shift+Y` |

---

## 📋 Available VS Code Tasks

Open: `Ctrl+Shift+P` → "Run Task"

- **🚀 Run Portal (Full Setup)** - Generate data + start
- **🌐 Start Flask Server** - Just start server
- **📊 Generate Sample Data** - Create demo data
- **🔄 Reset Database** - Delete and recreate
- **📦 Install Dependencies** - pip install
- **🆚 Run with Debugger** - Python debugger

---

## 🔧 Available Debug Configurations

Open: `Ctrl+Shift+D`

- **🚀 Flask - Run Portal** (Recommended)
- **🐍 Python - Run app.py**
- **📊 Generate Sample Data**
- **🧪 Test Models**
- **💾 Test Database**
- **📈 Test Analytics**

---

## 🌐 Access Points

Once running:

| Page | URL |
|------|-----|
| Dashboard | http://localhost:5000/ |
| Students | http://localhost:5000/students |
| Courses | http://localhost:5000/courses |
| Analytics | http://localhost:5000/analytics |
| Predictions | http://localhost:5000/predictions |
| Reports | http://localhost:5000/reports |

---

## 🐛 Quick Debug Tips

### Set Breakpoint
Click on line number in editor → Red dot appears

### Step Through Code
- F10: Step over
- F11: Step into
- Shift+F11: Step out

### Watch Variables
Debug panel → Variables → Right-click → "Add to Watch"

### Use Debug Console
Bottom panel → Type Python code → Press Enter

---

## 🔌 Recommended Extensions

When prompted, click "Install All" or install individually:

- **Python** - Python support
- **Pylance** - IntelliSense
- **REST Client** - Test APIs
- **Live Server** - Preview files

---

## 📂 Project Structure

```
📁 student-tracker-portal/
├── 🐍 app.py              Main Flask app
├── models.py              OOP classes
├── database.py            SQLite DB
├── analytics.py           Data analysis
├── sample_data.py         Generate demo
├── 🌐 templates/          HTML pages
├── 🎨 static/             CSS + JS
├── 🚀 .vscode/            VS Code config
│   ├── launch.json        Debug configs
│   ├── tasks.json         Task configs
│   ├── settings.json      VS Code settings
│   └── extensions.json    Recommended extensions
├── 📚 README.md           Full docs
├── VSCODE_GUIDE.md        VS Code guide
└── .gitignore             Git ignore rules
```

---

## ⚙️ Settings

All settings are in `.vscode/settings.json`:
- Python formatting: Black
- Linting: Flake8
- Type checking: Basic
- Rulers at: 80, 120 columns

---

## 🆘 Common Issues

### Python not found
```
Ctrl+Shift+P → Python: Select Interpreter
```

### Port 5000 in use
Edit `app.py`: Change `port=5000` to `port=5001`

### Database errors
```
Ctrl+Shift+P → Run Task → 🔄 Reset Database
```

### Dependencies missing
```
Ctrl+Shift+P → Run Task → 📦 Install Dependencies
```

---

## 🎯 Workflow

### Development
1. Run Flask server (`Ctrl+Shift+D` → Flask)
2. Edit code in editor
3. Browser auto-refreshes (if debug enabled)
4. Check debug console for errors

### Debugging
1. Set breakpoint (click line number)
2. Run action in browser (click button, navigate page)
3. Debugger pauses at breakpoint
4. Inspect variables in Variables panel
5. Step through code (F10/F11)

### Testing
1. Run specific test config (`Ctrl+Shift+D`)
2. Check output in terminal
3. View results in debug console

---

## 💾 Saving & Auto-Format

- **Auto-save:** Enabled by default
- **Format on save:** Enabled for Python
- **Format shortcut:** `Ctrl+Shift+I`

---

## 🚀 Pro Tips

1. **Multiple Terminals**
   - `Ctrl+Shift+`` `` opens new terminal tab
   - Use different tabs for server, database, debugging

2. **Search Across Files**
   - `Ctrl+Shift+F` - Find in all files
   - `Ctrl+H` - Replace in all files

3. **Git Integration**
   - Click "Source Control" sidebar
   - Commit, push, pull, view history

4. **Problems Panel**
   - `Ctrl+Shift+M` - Show problems/errors
   - Jump to problems in code

5. **Zen Mode**
   - `Ctrl+K Z` - Full focus mode
   - `Esc Esc` - Exit zen mode

---

## 📖 Full Documentation

- **VSCODE_GUIDE.md** - Detailed VS Code setup
- **README.md** - Project documentation
- **SETUP_GUIDE.md** - Installation guide

---

**Happy Coding! 🎉**
