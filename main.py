import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import QRegExpValidator 
from PySide2.QtCore import QRegExp, QSize
from widget import Ui_MainWindow
from taskDialog import Ui_Dialog
from categoryWindow import Ui_Form
import sqlHelper


class taskDialog(Ui_Dialog, QDialog):
    def __init__(self, *args, **kwargs):
        super(taskDialog, self).__init__(*args, **kwargs)
        
        # UI setup
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Add a task")

        self.ui.buttonBox.accepted.connect(self.addTask)

    def addTask(self):
        # Input validation
        rx = QRegExp("^[A-Za-z0-9 _]*[A-Za-z0-9][A-Za-z0-9 _]*$")
        validator = QRegExpValidator(rx, self)
        self.ui.taskName.setValidator(validator)

        if self.ui.taskName.hasAcceptableInput():
            task = self.ui.taskName.text()
            task = task.split('\n', 1)[0]

            # Database code
            data = {'title': task}

            sql_task_model.insert(data)
        else:
            flags = QMessageBox.Close
            result = QMessageBox.warning(self, "Error", "Invalid input!", flags)

class categoryWindow(Ui_Form, QWidget):
    def __init__(self):
        super(categoryWindow, self).__init__()

        # UI setup
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Categories")

        # Show categories
        self.showCategories()

    def showCategories(self):
        categories = sql_category_model.getCategories()

        # Dynamically create category button and add it to the layout
        self.ui.categories = []
        lastPos = 1
        for i, category in enumerate(categories):
            title = categories[i]['title']
            color = categories[i]['color']
            self.ui.categories.append(QPushButton(self.ui.frame))
            self.ui.categories[i].setObjectName(f"{title}")
            self.ui.categories[i].setMinimumSize(QSize(160, 40))
            self.ui.categories[i].setStyleSheet(f"background-color: {color};")
            self.ui.categories[i].setText(f"{title}")
            self.ui.gridLayout_2.addWidget(self.ui.categories[i], i+1, 0, 1, 1)

            # Save free position for 'add new task' button
            lastPos += 1

        self.ui.gridLayout_2.addWidget(self.ui.add_category, lastPos, 0, 1, 1)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # UI setup
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Task Widget")
        self.updateTaskLabel()
        
        # Set position on screen
        self.move(900, 0)

        # Show task dialog
        self.ui.add_task.clicked.connect(self.showDialog)

        # Complete task
        self.ui.completed.clicked.connect(self.completeTask)

        # Show categories window
        self.catWindow = categoryWindow()
        self.ui.show_categories.clicked.connect(self.catWindow.show)

    def showDialog(self):
        dialog = taskDialog(self)
        dialog.exec_()
        self.updateTaskLabel()

    def updateTaskLabel(self):
        _, firstTask = sql_task_model.getTask()
        if firstTask:
            self.ui.task_name.setText(firstTask)
        else:
            self.ui.task_name.setText("No task")

    def completeTask(self):
        taskID, _ = sql_task_model.getTask()
        sql_task_model.updateTaskStatus(taskID)
        self.updateTaskLabel()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Database setup
    sqlHelper.connectToDatabase()
    sql_category_model = sqlHelper.SqlCategoryModel()
    sql_task_model = sqlHelper.SqlTaskModel()

    # Window setup
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

