# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabprint.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import QHBoxLayout, QTableView


class Ui_tabprint(object):
    def setupUi(self, tabprint):
        if not tabprint.objectName():
            tabprint.setObjectName("tabprint")
        tabprint.resize(911, 640)
        self.horizontalLayout = QHBoxLayout(tabprint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QTableView(tabprint)
        self.tableView.setObjectName("tableView")

        self.horizontalLayout.addWidget(self.tableView)

        self.retranslateUi(tabprint)

        QMetaObject.connectSlotsByName(tabprint)

    # setupUi

    def retranslateUi(self, tabprint):
        tabprint.setWindowTitle(QCoreApplication.translate("tabprint", "\u8868\u683c\u8f93\u51fa", None))

    # retranslateUi
