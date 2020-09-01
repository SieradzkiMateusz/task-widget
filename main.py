import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
from PySide2.QtGui import QRegExpValidator 
from PySide2.QtCore import QRegExp
from widget import Ui_MainWindow
from taskDialog import Ui_Dialog
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
        _, firstTask = sql_task_model.getTask()
        if firstTask:
            self.ui.task_name.setText(firstTask)
        else:
            self.ui.task_name.setText("No task")

    def completeTask(self):
        taskID, _ = sql_task_model.getTask()
        sql_task_model.updateTaskStatus(taskID)
        self.updateTask()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Database setup
    sqlHelper.connectToDatabase()
    sql_task_model = sqlHelper.SqlTaskModel()

    # Window setup
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

