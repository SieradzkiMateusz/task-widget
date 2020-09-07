# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'taskDialog.ui'
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


class Ui_AddTask(object):
    def setupUi(self, AddTask):
        if not AddTask.objectName():
            AddTask.setObjectName(u"AddTask")
        AddTask.resize(255, 141)
        self.gridLayout = QGridLayout(AddTask)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(AddTask)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.taskName = QLineEdit(self.frame)
        self.taskName.setObjectName(u"taskName")

        self.gridLayout_2.addWidget(self.taskName, 0, 0, 1, 1)

        self.selectCategory = QComboBox(self.frame)
        self.selectCategory.setObjectName(u"selectCategory")

        self.gridLayout_2.addWidget(self.selectCategory, 2, 0, 1, 1)

        self.select_category_label = QLabel(self.frame)
        self.select_category_label.setObjectName(u"select_category_label")

        self.gridLayout_2.addWidget(self.select_category_label, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(AddTask)
        self.buttonBox.accepted.connect(AddTask.accept)
        self.buttonBox.rejected.connect(AddTask.reject)

        QMetaObject.connectSlotsByName(AddTask)
    # setupUi

    def retranslateUi(self, AddTask):
        AddTask.setWindowTitle(QCoreApplication.translate("AddTask", u"Add task", None))
        self.taskName.setPlaceholderText(QCoreApplication.translate("AddTask", u"Enter task name", None))
        self.select_category_label.setText(QCoreApplication.translate("AddTask", u"Select category", None))
    # retranslateUi

