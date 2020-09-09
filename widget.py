# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(275, 72)
        MainWindow.setMaximumSize(QSize(16777215, 100))
        MainWindow.setStyleSheet(u"")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: white;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.task_name = QLabel(self.frame)
        self.task_name.setObjectName(u"task_name")

        self.gridLayout_2.addWidget(self.task_name, 0, 0, 3, 2)

        self.add_task = QPushButton(self.frame)
        self.add_task.setObjectName(u"add_task")
        font = QFont()
        font.setFamily(u"Arial")
        font.setBold(True)
        font.setWeight(75)
        self.add_task.setFont(font)
        self.add_task.setStyleSheet(u"*{\n"
"	background-color:#45adc7;\n"
"	border-radius:14px;\n"
"	border:1px solid #198eab;\n"
"	color:#ffffff;\n"
"	font-family:Arial;\n"
"	font-size:9px;\n"
"	font-weight:bold;\n"
"	padding:4px 6px;\n"
"}\n"
"*:hover{\n"
"	background-color:#2aa0bd;\n"
"}\n"
"	")

        self.gridLayout_2.addWidget(self.add_task, 0, 3, 2, 1)

        self.horizontalSpacer = QSpacerItem(202, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 1, 2, 1)

        self.completed = QPushButton(self.frame)
        self.completed.setObjectName(u"completed")
        self.completed.setFont(font)
        self.completed.setStyleSheet(u"*{\n"
"	background-color:#44c767;\n"
"	border-radius:14px;\n"
"	border:1px solid #18ab29;\n"
"	color:#ffffff;\n"
"	font-family:Arial;\n"
"	font-size:9px;\n"
"	font-weight:bold;\n"
"	padding:4px 6px;\n"
"}\n"
"*:hover{\n"
"	background-color:#5cbf2a;\n"
"}\n"
"	")

        self.gridLayout_2.addWidget(self.completed, 2, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 3, 1, 1)

        self.show_categories = QPushButton(self.frame)
        self.show_categories.setObjectName(u"show_categories")
        self.show_categories.setMaximumSize(QSize(15, 15))
        self.show_categories.setStyleSheet(u"*{\n"
"	background-color:#29272b;\n"
"	color:#ffffff;\n"
"}\n"
"*:hover{\n"
"	background-color:#3d3a40;\n"
"}\n"
"	")

        self.gridLayout_2.addWidget(self.show_categories, 2, 2, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.task_name.setText(QCoreApplication.translate("MainWindow", u"No task", None))
        self.add_task.setText(QCoreApplication.translate("MainWindow", u"Add task", None))
        self.completed.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.show_categories.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
    # retranslateUi

