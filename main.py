import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QDialog
from PySide2.QtCore import Qt
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
            tasksFile = open("tasks.txt", "a") 
        except:
            print("Couldn't open file")
            return 0

        task = self.ui.taskName.toPlainText()
        task = task.split('\n', 1)[0]

        if task:
            print("Task name: {}".format(task))
            tasksFile.write(task + '\n')
        else:
            print("Enter task name!")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # UI setup
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Task Widget")
        
        # Set position on screen
        self.move(900, 0)

        # Show task dialog
        self.ui.add_task.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = taskDialog(self)
        dialog.exec_()
        self.updateTask()

    def updateTask(self):
        taskFile = open("tasks.txt", "r")
        firstTask = taskFile.read()
        firstTask = firstTask.split('\n', 1)[0]
        self.ui.task_name.setText(firstTask)

        # DEBUG
        print("Current task name: {}".format(self.ui.task_name.text()))


        


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
