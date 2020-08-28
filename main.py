import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QDialog
from PySide2.QtCore import Qt
from widget import Ui_MainWindow
from taskDialog import Ui_Dialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # UI setup
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Task Widget")
        
        # Set position on screen
        self.move(900, 0)

        # Connect function for adding tasks to the button
        self.ui.add_task.clicked.connect(self.addTask)

    def addTask(self):
        if self.ui.task_name != "" and self.ui.task_name != "No task":
            pass

        # Debug
        print("Task added")
        print("Current task name: {}".format(self.ui.task_name.text()))


class TaskForm(Ui_Dialog, QDialog):
    def __init__(self, parent=MainWindow):
        super(TaskForm, self).__init__(parent)
        
        # UI setup
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Add a task")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
