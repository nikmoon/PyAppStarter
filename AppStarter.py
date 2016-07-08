#!/usr/bin/python
#   coding: utf-8
#

import sys
from os import path
import subprocess
import mygui
from PyQt4.QtGui import QWidget, QLineEdit, QPushButton, QVBoxLayout, QSizePolicy
from PyQt4.QtCore import Qt


if __name__ != '__main__':
    sys.exit()

if len(sys.argv) > 2:
    raise Exception(u'Too many arguments: ' + str(len(sys.argv)))


class AppNameWidget(QLineEdit):
    def __init__(self):
        super(AppNameWidget, self).__init__()
        self.setReadOnly(True)

    def mousePressEvent(self, mouseEvent):
        if mouseEvent.button() == Qt.LeftButton:
            self.parent().select_app()


class StartButton(QPushButton):
    def __init__(self, parent):
        super(StartButton, self).__init__(parent)
        self.sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setSizePolicy(self.sizePolicy)
        self.clicked.connect(parent.start_app)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(u'Запускатор')
        self.resize(300, 200)
        self.appNameWidget = AppNameWidget()
        self.startButton = StartButton(self)
        self.vertLayout = QVBoxLayout(self)
        self.vertLayout.addWidget(self.appNameWidget)
        self.vertLayout.addWidget(self.startButton)
        self.appFile = u''

    def start_app(self):
        if self.appFile:
            self.hide()
            try:
                subprocess.call(['python2', self.appFile])
            except Exception:
                raise
            finally:
                self.show()

    def select_app(self):
        dialog = mygui.Dialog()
        appFile = dialog.select_file(u'Выбор приложения Python', u'', 'Python Files (*.py)')
        if appFile:
            self.appFile = appFile
            self.appNameWidget.setText(appFile)
            self.startButton.setText(path.basename(appFile))

mainWindow = MainWindow()
mainWindow.show()
exitCode = mygui.QApp.exec_()
sys.exit(exitCode)
