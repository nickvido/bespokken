#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import *
from PyQt5.QtCore import Qt
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtWidgets import QMessageBox
import PyQt5.QtGui as QtGui
from edit_tab import EditTab
from review_tab import ReviewTab
from time import sleep

class WaveChopperApp(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.update_status('Ready')
        self.setup_menu()
        self.setGeometry(0, 0, 850, 600)
        self.setWindowTitle('WaveChopper')
        self.setWindowIcon(QtGui.QIcon('wc_icon.png'))
        self.center()

        edit_tab = EditTab()
        review_tab = ReviewTab()

        tabs = QtWidgets.QTabWidget()
        tabs.addTab(edit_tab, 'Edit')
        tabs.addTab(review_tab, 'Review')

        self.setCentralWidget(tabs)

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        resp = QMessageBox.question(self, 'Message', 'Really quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if resp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def update_status(self, message):
        self.statusBar().showMessage(message)

    def setup_menu(self):
        exit_action = QtWidgets.QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_action)
        edit_menu = menu_bar.addMenu('&Edit')
        view_menu = menu_bar.addMenu('&View')


def main():
    app = QtWidgets.QApplication(sys.argv)

    # Splash screen
    pixmap = QtGui.QPixmap("wc_icon.png")
    splash = QtWidgets.QSplashScreen(pixmap.scaled(500,500))
    splash.show()
    splash.showMessage("Initializing the audio subsystem")
    app.processEvents()

    # TODO: setup logger
    #logger = Logger()

    wca = WaveChopperApp()
    splash.finish(wca)
    sys.exit(app.exec_())
