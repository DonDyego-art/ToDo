# To-Do List App (PyQt6)

This is a simple graphical To-Do List application built with **Python** and **PyQt6**.  
It automatically creates and saves tasks into a `tasks.txt` file in the same folder.  
The file is generated during usage, so it does not need to be shipped with the installer.

---

## 🚀 Features
- ➕ Add new tasks (using **Enter** or the **"Add Task"** button)
- 🗑️ Delete tasks (using the **Delete key** or the **"Delete Selected Task"** button)
- 🎨 Highlight tasks with colors:
  - 🟢 Green (**"Food"** button)
  - 🔴 Red (**"Work"** button)
- 💾 Automatically saves tasks to `tasks.txt`
- 📂 Loads saved tasks on startup

---

## 🖥️ How to Run (Executable Version)
1. Download `todo.exe` from the release folder (or from `dist/todo.exe` if built manually).
2. Double-click to start the app.
3. The `tasks.txt` file will be created automatically in the same directory.

---

## ⚙️ How to Build the Executable Yourself
1. Install Python 3 → [Download here](https://www.python.org/downloads/)  
2. Install PyQt6 and PyInstaller:
   ```bash
   pip install PyQt6 pyinstaller

Created by DonDyego
