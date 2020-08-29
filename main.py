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
            taskFile = open("tasks.txt", "a") 
        except:
            print("Couldn't open file")
            return 0

        task = self.ui.taskName.toPlainText()
        task = task.split('\n', 1)[0]

        if task:
            print("Task name: {}".format(task))
            taskFile.write(task + '\n')
        else:
            print("Enter task name!")

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
        taskFile = open("tasks.txt", "r")

        firstTask = taskFile.read()
        firstTask = firstTask.split('\n', 1)[0]
        self.ui.task_name.setText(firstTask)

        taskFile.close()

        # DEBUG
        # print("Current task name: {}".format(self.ui.task_name.text()))

    def completeTask(self):
        # Read tasks currently in file and append them to empty list
        taskFile = open("tasks.txt", "r")
        tasks = taskFile.read()
        newTasks = []
        for task in tasks.split('\n')[1:-1]:
            print("Appending task: {}".format(task))
            newTasks.append(task)

        taskFile.close()

        # Rewrite file without the completed task
        taskFile = open("tasks.txt", "w")
        for task in newTasks:
            print("Adding task: {}".format(task))
            taskFile.write(task + '\n')

        taskFile.close()
        self.updateTask()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

