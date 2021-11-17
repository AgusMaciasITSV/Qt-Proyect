# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMenu_dialogGEzdQv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(255, 137)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 221, 81))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.confirmBtn = QPushButton(self.verticalLayoutWidget)
        self.confirmBtn.setObjectName(u"confirmBtn")

        self.horizontalLayout.addWidget(self.confirmBtn)

        self.cancelBtn = QPushButton(self.verticalLayoutWidget)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)
        self.confirmBtn.clicked.connect(Dialog.exit)
        self.cancelBtn.clicked.connect(Dialog.noExit)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u00bfEsta seguro que desea salir?", None))
        self.confirmBtn.setText(QCoreApplication.translate("Dialog", u"Si", None))
        self.cancelBtn.setText(QCoreApplication.translate("Dialog", u"No", None))
    # retranslateUi

