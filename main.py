from PySide2.QtWidgets import QWidget, QApplication, QMainWindow
import sys
import ui_mainwindow, widget


class MainWindow(ui_mainwindow.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


class TaskWidget(widget.Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

sys.exit()
