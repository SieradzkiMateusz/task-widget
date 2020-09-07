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


class Ui_Categories(object):
    def setupUi(self, Categories):
        if not Categories.objectName():
            Categories.setObjectName(u"Categories")
        Categories.resize(225, 300)
        self.gridLayout = QGridLayout(Categories)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.frame = QFrame(Categories)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.add_category = QPushButton(self.frame)
        self.add_category.setObjectName(u"add_category")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.add_category.setFont(font)

        self.gridLayout_2.addWidget(self.add_category, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 2, 1)


        self.retranslateUi(Categories)

        QMetaObject.connectSlotsByName(Categories)
    # setupUi

    def retranslateUi(self, Categories):
        Categories.setWindowTitle(QCoreApplication.translate("Categories", u"Categories", None))
        self.add_category.setText(QCoreApplication.translate("Categories", u"+", None))
    # retranslateUi

