# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'category_window.ui'
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


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(335, 300)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        # Category
        self.category_1 = QPushButton(self.frame)
        self.category_1.setObjectName(u"category_1")
        self.category_1.setMinimumSize(QSize(160, 40))
        self.category_1.setStyleSheet(u"* {\n"
"	background-color: #32a852;\n"
"	text-align: center;\n"
"}")

        self.gridLayout_2.addWidget(self.category_1, 1, 0, 1, 1)

        self.category_2 = QPushButton(self.frame)
        self.category_2.setObjectName(u"category_2")
        self.category_2.setMinimumSize(QSize(160, 40))
        self.category_2.setStyleSheet(u"*{\n"
"	background-color: #9432a8;\n"
"}")

        self.gridLayout_2.addWidget(self.category_2, 2, 0, 1, 1)

        self.add_category = QPushButton(self.frame)
        self.add_category.setObjectName(u"add_category")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.add_category.setFont(font)

        self.gridLayout_2.addWidget(self.add_category, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 2, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.add_category.setText(QCoreApplication.translate("Form", u"+", None))
    # retranslateUi

