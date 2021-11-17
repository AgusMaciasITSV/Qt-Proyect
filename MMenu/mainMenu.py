# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMenuKdrYeb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(181, 162)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 160, 101))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formBtn = QPushButton(self.verticalLayoutWidget)
        self.formBtn.setObjectName(u"formBtn")

        self.verticalLayout.addWidget(self.formBtn)

        self.listaBtn = QPushButton(self.verticalLayoutWidget)
        self.listaBtn.setObjectName(u"listaBtn")

        self.verticalLayout.addWidget(self.listaBtn)

        self.exitBtn = QPushButton(self.verticalLayoutWidget)
        self.exitBtn.setObjectName(u"exitBtn")

        self.verticalLayout.addWidget(self.exitBtn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 181, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exitBtn.clicked.connect(MainWindow.confirmEx)
        self.listaBtn.clicked.connect(MainWindow.openList)
        self.formBtn.clicked.connect(MainWindow.openForm)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.formBtn.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir ciudadano", None))
        self.listaBtn.setText(QCoreApplication.translate("MainWindow", u"Registros", None))
        self.exitBtn.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi