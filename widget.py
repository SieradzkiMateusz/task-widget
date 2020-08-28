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
        MainWindow.resize(335, 80)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.task_name = QLabel(self.frame)
        self.task_name.setObjectName(u"task_name")

        self.gridLayout_2.addWidget(self.task_name, 0, 0, 3, 2)

        self.add_task = QPushButton(self.frame)
        self.add_task.setObjectName(u"add_task")
        font = QFont()
        font.setPointSize(7)
        self.add_task.setFont(font)

        self.gridLayout_2.addWidget(self.add_task, 0, 2, 2, 1)

        self.horizontalSpacer = QSpacerItem(202, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 1, 2, 1)

        self.completed = QPushButton(self.frame)
        self.completed.setObjectName(u"completed")
        self.completed.setFont(font)

        self.gridLayout_2.addWidget(self.completed, 2, 2, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.task_name.setText(QCoreApplication.translate("MainWindow", u"No task", None))
        self.add_task.setText(QCoreApplication.translate("MainWindow", u"Add task", None))
        self.completed.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
    # retranslateUi

