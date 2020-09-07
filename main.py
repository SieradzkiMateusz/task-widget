import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import QRegExpValidator 
from PySide2.QtCore import QRegExp, QSize
from widget import Ui_MainWindow
from taskDialog import Ui_AddTask
from categoryWindow import Ui_Categories
from categoryEdit import Ui_CategoryEdit
from categoryAdd import Ui_CategoryAdd
import sqlHelper
from functools import partial


class taskDialog(Ui_AddTask, QDialog):
    def __init__(self, *args, **kwargs):
        super(taskDialog, self).__init__(*args, **kwargs)
        
        # UI setup
        self.ui = Ui_AddTask()
        self.ui.setupUi(self)

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


class categoryEdit(Ui_CategoryEdit, QDialog):
    def __init__(self, catID, title, color):
        super(categoryEdit, self).__init__()

        # UI Setup
        self.ui = Ui_CategoryEdit()
        self.ui.setupUi(self)

        self.catID = catID
        self.title = title
        self.color = color

        self.ui.buttonBox.accepted.connect(self.updateCategory)
        self.ui.catDelete.clicked.connect(self.deleteCategory)

    def updateCategory(self):
        self.title = self.ui.catName.text()
        sql_category_model.updateCategory(self.catID, self.title, self.color)

    def pickColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.ui.selectColor.setStyleSheet(f"background-color: {color.name()};")
            self.color = color.name()

    def deleteCategory(self):
        flags = QMessageBox.Cancel
        flags |= QMessageBox.Ok
        result = QMessageBox.warning(self, "Confirm", "Do you really want to delete this category?", flags)
        if result == 1024:
            sql_category_model.deleteCategory(self.catID)
            self.close()


class categoryAdd(Ui_CategoryAdd, QDialog):
    def __init__(self):
        super(categoryAdd, self).__init__()

        # UI Setup
        self.ui = Ui_CategoryAdd()
        self.ui.setupUi(self)

        self.color = "#eeeeee"

        self.ui.buttonBox.accepted.connect(self.addCategory)

    def addCategory(self):
        title = self.ui.catName.text()
        data = {
            'title': title,
            'color': self.color
        }
        print(f"DEBUG: {data['title']} {data['color']}")
        if title:
            sql_category_model.insert(data)
    
    def pickColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.ui.selectColor.setStyleSheet(f"background-color: {color.name()};")
            self.color = color.name()


class categoryWindow(Ui_Categories, QWidget):
    def __init__(self):
        super(categoryWindow, self).__init__()

        # UI setup
        self.ui = Ui_Categories()
        self.ui.setupUi(self)
        self.showCategories()
        
        self.ui.add_category.clicked.connect(self.showAddCategory)

    def showAddCategory(self):
        dialog = categoryAdd()
        dialog.ui.selectColor.clicked.connect(dialog.pickColor)
        dialog.exec_()
        self.showCategories()

    def showEditCategory(self, catID, catTitle, catColor):
        dialog = categoryEdit(catID, catTitle, catColor)
        dialog.ui.catName.setText(str(catTitle))
        dialog.ui.selectColor.setStyleSheet(f"background-color: {catColor};")
        dialog.ui.selectColor.clicked.connect(dialog.pickColor)
        dialog.exec_()
        self.showCategories()

    def showCategories(self):
        categories = sql_category_model.getCategories()
        # Clear layout
        for i in reversed(range(self.ui.gridLayout_2.count())):
            self.ui.gridLayout_2.itemAt(i).widget().setParent(None)

        # Dynamically create category button and add it to the layout
        self.ui.categories = []
        lastPos = 1
        for i, category in enumerate(categories):
            title = categories[i]['title']
            color = categories[i]['color']
            catID = categories[i]['catID']

            self.ui.categories.append(QPushButton(self.ui.frame))
            self.ui.categories[i].setObjectName(f"cat_{title}")
            self.ui.categories[i].setMinimumSize(QSize(160, 40))
            self.ui.categories[i].setStyleSheet(f"background-color: {color};")
            self.ui.categories[i].setText(f"{title}")

            # Using partial to pass extra arguments
            self.ui.categories[i].clicked.connect(partial(self.showEditCategory, catID, title, color))
            self.ui.gridLayout_2.addWidget(self.ui.categories[i], i+1, 0, 1, 1)

            # Save free position for 'add new category' button
            lastPos += 1

        # 'Add new category' button
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
        self.ui.add_task.clicked.connect(self.showTaskDialog)

        # Complete task
        self.ui.completed.clicked.connect(self.completeTask)

        # Show categories window
        self.catWindow = categoryWindow()
        self.ui.show_categories.clicked.connect(self.catWindow.show)

    def showTaskDialog(self):
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

