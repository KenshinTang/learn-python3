#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *

import sys

class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()

        button = QPushButton('button')
        button.clicked.connect(self.slot_method)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button)

        self.setLayout(mainLayout)
        self.setWindowTitle('dialog')

    def slot_method(self):
        # self.statusBar.showMessage('slot_method')
        print('slot_method')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()

sys.exit(dialog.exec_())
