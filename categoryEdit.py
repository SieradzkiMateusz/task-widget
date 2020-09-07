# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'categoryEditDialog.ui'
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


class Ui_CategoryEdit(object):
    def setupUi(self, CategoryEdit):
        if not CategoryEdit.objectName():
            CategoryEdit.setObjectName(u"CategoryEdit")
        CategoryEdit.resize(289, 209)
        self.gridLayout = QGridLayout(CategoryEdit)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(CategoryEdit)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.catDelete = QPushButton(self.frame)
        self.catDelete.setObjectName(u"catDelete")
        self.catDelete.setStyleSheet(u"background-color: red;\n"
"")

        self.gridLayout_2.addWidget(self.catDelete, 5, 0, 1, 2)

        self.catName = QLineEdit(self.frame)
        self.catName.setObjectName(u"catName")

        self.gridLayout_2.addWidget(self.catName, 1, 0, 1, 2)

        self.catNameLabel = QLabel(self.frame)
        self.catNameLabel.setObjectName(u"catNameLabel")

        self.gridLayout_2.addWidget(self.catNameLabel, 0, 0, 1, 2)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 7, 0, 1, 2)

        self.catColorLabel = QLabel(self.frame)
        self.catColorLabel.setObjectName(u"catColorLabel")
        self.catColorLabel.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_2.addWidget(self.catColorLabel, 3, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 6, 0, 1, 1)

        self.selectColor = QPushButton(self.frame)
        self.selectColor.setObjectName(u"selectColor")
        self.selectColor.setStyleSheet(u"background-color: blue;")

        self.gridLayout_2.addWidget(self.selectColor, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(CategoryEdit)
        self.buttonBox.accepted.connect(CategoryEdit.accept)
        self.buttonBox.rejected.connect(CategoryEdit.reject)

        QMetaObject.connectSlotsByName(CategoryEdit)
    # setupUi

    def retranslateUi(self, CategoryEdit):
        CategoryEdit.setWindowTitle(QCoreApplication.translate("CategoryEdit", u"Edit category", None))
        self.catDelete.setText(QCoreApplication.translate("CategoryEdit", u"Delete category", None))
        self.catName.setPlaceholderText(QCoreApplication.translate("CategoryEdit", u"Enter category name", None))
        self.catNameLabel.setText(QCoreApplication.translate("CategoryEdit", u"Category name", None))
        self.catColorLabel.setText(QCoreApplication.translate("CategoryEdit", u"Select color:", None))
        self.selectColor.setText("")
    # retranslateUi

