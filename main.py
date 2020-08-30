import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
from PySide2.QtGui import QRegExpValidator 
from PySide2.QtCore import QRegExp
from widget import Ui_MainWindow
from taskDialog import Ui_Dialog


class taskDialog(Ui_Dialog, QDialog):
    def __init__(self, *args, **kwargs):
        super(taskDialog, self).__init__(*args, **kwargs)
        
        # UI setup
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Add a task")

        self.ui.buttonBox.accepted.connect(self.addTask)

    def addTask(self):
        try:
            taskFile = open("tasks.txt", "a") 
        except:
            flags = QMessageBox.Abort
            result = QMessageBox.critical(self, "Error", "Could not open a file", flags)
            return 0

        # Input validation
        rx = QRegExp("^[A-Za-z0-9 _]*[A-Za-z0-9][A-Za-z0-9 _]*$")
        validator = QRegExpValidator(rx, self)
        self.ui.taskName.setValidator(validator)

        if self.ui.taskName.hasAcceptableInput():
            task = self.ui.taskName.text()
            task = task.split('\n', 1)[0]
            taskFile.write(task + '\n')
        else:
            flags = QMessageBox.Close
            result = QMessageBox.warning(self, "Error", "Invalid input!", flags)

        taskFile.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # UI setup
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Task Widget")
        self.updateTask()
        
        # Set position on screen
        self.move(900, 0)

        # Show task dialog
        self.ui.add_task.clicked.connect(self.showDialog)

        self.ui.completed.clicked.connect(self.completeTask)

    def showDialog(self):
        dialog = taskDialog(self)
        dialog.exec_()
        self.updateTask()

    def updateTask(self):
        try:
            taskFile = open("tasks.txt", "r") 
        except:
            flags = QMessageBox.Abort
            result = QMessageBox.critical(self, "Error", "Could not open a file", flags)
            return 0

        firstTask = taskFile.read()
        firstTask = firstTask.split('\n', 1)[0]
        if firstTask:
            self.ui.task_name.setText(firstTask)
        else:
            self.ui.task_name.setText("No task")

        taskFile.close()

    def completeTask(self):
        # Read tasks currently in file and append them to empty list
        try:
            taskFile = open("tasks.txt", "r") 
        except:
            flags = QMessageBox.Abort
            result = QMessageBox.critical(self, "Error", "Could not open a file", flags)
            return 0

        tasks = taskFile.read()
        newTasks = []
        for task in tasks.split('\n')[1:-1]:
            newTasks.append(task)

        taskFile.close()

        # Rewrite file without the completed task
        try:
            taskFile = open("tasks.txt", "w") 
        except:
            flags = QMessageBox.Abort
            result = QMessageBox.critical(self, "Error", "Could not open a file", flags)
            return 0
       
        for task in newTasks:
            taskFile.write(task + '\n')

        taskFile.close()
        self.updateTask()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

