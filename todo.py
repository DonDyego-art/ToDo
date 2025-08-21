import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt

# --- Fájl név ---
FILENAME = "tasks.txt"

# --- Alkalmazás és ablak ---
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("To-Do List")
window.setGeometry(100, 100, 800, 600)
window.setStyleSheet("background-color: #827672;")

# --- Layout ---
main_layout = QVBoxLayout(window)

# --- Felső rész: input ---
input_section = QWidget()
input_section.setStyleSheet("background-color: #d9d9d9;")
input_layout = QVBoxLayout(input_section)

input_task = QLineEdit()
input_task.setPlaceholderText("Enter your task here...")
input_layout.addWidget(input_task)

input_button = QPushButton("Add Task")
input_button.setStyleSheet("font-weight: bold; color: #1E4D1C;")
input_layout.addWidget(input_button)

main_layout.addWidget(input_section)

# --- Középső rész ---
middle_section = QWidget()
middle_layout = QHBoxLayout(middle_section)
main_layout.addWidget(middle_section)

# bal oldal - lista
list_section = QWidget()
list_section.setStyleSheet("background-color: #9E8F8B;")
list_layout = QVBoxLayout(list_section)

todo_list = QListWidget()
list_layout.addWidget(todo_list)

delete_button = QPushButton("Delete Selected Task")
delete_button.setStyleSheet("font-weight: bold; color: #8F1E1E;")
list_layout.addWidget(delete_button)

middle_layout.addWidget(list_section)

# jobb oldal - extra gombok
right_side = QWidget()
right_side.setStyleSheet("background-color: #d9d9d9;")
right_layout = QVBoxLayout(right_side)

extra_button1 = QPushButton("Food")
extra_button1.setStyleSheet("font-weight: bold; color: #1E4D1C;")
extra_button2 = QPushButton("Work")
extra_button2.setStyleSheet("font-weight: bold; color: #8F1E1E;")
right_layout.addWidget(extra_button1)
right_layout.addWidget(extra_button2)
right_layout.addStretch()

middle_layout.addWidget(right_side)

# arányok
middle_layout.setStretch(0, 3)
middle_layout.setStretch(1, 1)

# --- Funkciók ---
def save_tasks():
    with open(FILENAME, "w", encoding="utf-8") as file:
        for i in range(todo_list.count()):
            file.write(todo_list.item(i).text() + "\n")

def add_task():
    task = input_task.text().strip()
    if task:
        todo_list.addItem(task)
        input_task.clear()
        save_tasks()

def delete_task():
    for item in todo_list.selectedItems():
        todo_list.takeItem(todo_list.row(item))
    save_tasks()

def colorize_task(color):
    for item in todo_list.selectedItems():
        item.setBackground(QColor(color))

def delete_task_key(event):
    if event.key() == Qt.Key.Key_Delete:
        delete_task()
    else:
        QListWidget.keyPressEvent(todo_list, event)  # továbbadjuk az eredeti eseménynek

# --- Betöltés fájlból ---
if os.path.exists(FILENAME):
    with open(FILENAME, "r", encoding="utf-8") as file:
        for line in file:
            todo_list.addItem(line.strip())

# --- Kapcsolatok ---
input_button.clicked.connect(add_task)
input_task.returnPressed.connect(add_task)
delete_button.clicked.connect(delete_task)
extra_button1.clicked.connect(lambda: colorize_task("#00FD0D"))
extra_button2.clicked.connect(lambda: colorize_task("#FD0000"))
todo_list.keyPressEvent = delete_task_key

# --- Ablak megjelenítése ---
window.show()
sys.exit(app.exec())
