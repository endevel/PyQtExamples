#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import sys
from PyQt5.QtGui import QIcon
 
from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt,
        QTime)
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
        QGroupBox, QHBoxLayout, QLabel, QLineEdit, QTreeView, QVBoxLayout,
        QWidget)
 
class TreeView(QWidget):
    """
    Пример с использованием QTreeView
    """

    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Examples"
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 240

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.dataGroupBox = QGroupBox("Inbox")
        self.dataGroupBox = QGroupBox("Inbox")
        self.dataView = QTreeView()
        self.dataView.setRootIsDecorated(False)
        self.dataView.setAlternatingRowColors(True)
 
        dataLayout = QHBoxLayout()
        dataLayout.addWidget(self.dataView)
        self.dataGroupBox.setLayout(dataLayout)
 
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.dataGroupBox)
        self.setLayout(mainLayout)

       
##########################################

app = QApplication(sys.argv)

screen = TreeView()
screen.show()

sys.exit(app.exec_())
