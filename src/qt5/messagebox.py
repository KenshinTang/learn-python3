#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'kenshin'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        buttonReply = QMessageBox.question(self, 'message box', 'pyQt5?',
                                           QMessageBox.Yes | QMessageBox.No | QMessageBox.RestoreDefaults , QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            # self.statusBar().showMessage('yes clicked')
            print('yes clicked')
        elif buttonReply == QMessageBox.No:
            # self.statusBar().showMessage('no clicked')
            print('no clicked')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
