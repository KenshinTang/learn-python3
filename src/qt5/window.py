#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'kenshin'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('this is a message')
        button = QPushButton('button', self)
        button.setToolTip('this is a button')
        button.move(100, 70)
        button.clicked.connect(self.onClick)
        self.show()

    @pyqtSlot()
    def onClick(self):
        self.statusBar().showMessage('button clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
