#
# -*- coding: utf-8
#

import sys
from PyQt4.QtGui import QApplication, QFileDialog, QMessageBox
import os.path as path


from PyQt4 import QtGui
try:
    QtGui.QApp
except AttributeError:
    QtGui.QApp = QApplication(sys.argv)
QApp = QtGui.QApp


FILE_FILTERS = {
    'xlsx': 'XLSX (*.xlsx)'
}


class Dialog(object):

    def __init__(self):
        self.dirPath = u''
        self.fileFilter = u''


    def _show_select_dialog(self, title, dirPath, fileFilter, fileMode, option = None):
        if dirPath is not None:
            self.set_dir_path(dirPath)
        if fileFilter is not None:
            self.set_filter(fileFilter)
        dlg = QFileDialog(None, title, self.dirPath, self.fileFilter)
        dlg.setFileMode(fileMode)
        if option is not None:
            dlg.setOption(option, True)
        return dlg.selectedFiles() if dlg.exec_() else []


    def set_dir_path(self, dirPath):
        self.dirPath = dirPath


    def set_filter(self, fileFilter):
        f = FILE_FILTERS.get(fileFilter, fileFilter)
        self.fileFilter = f


    def select_file(self, title = u'Выбор файла', dirPath = None, fileFilter = None):
        result = self._show_select_dialog(title, dirPath, fileFilter, QFileDialog.ExistingFile)
        return unicode(result[0]) if result else None


    def select_files(self, title = u'Выбор файлов', dirPath = None, fileFilter = None):
        result = self._show_select_dialog(title, dirPath, fileFilter, QFileDialog.ExistingFiles)
        return [unicode(s) for s in result] if result else []


    def select_dir(self, title = u'Выбор каталога', dirPath = None):
        result = self._show_select_dialog(title, dirPath, None, QFileDialog.Directory, QFileDialog.ShowDirsOnly)
        return unicode(result[0]) if result else None


    @staticmethod
    def _show_message_box(icon, title, text, stdBtns = QMessageBox.NoButton):
        mbox = QMessageBox(icon, title, text, stdBtns)
        return mbox.exec_()


    @staticmethod
    def show_msg_info(text, title=u'Сообщение'):
        return Dialog._show_message_box(QMessageBox.Information, title, text)


    @staticmethod
    def show_msg_question(text = u'Вы уверены', title = u'Подтвердите'):
        return Dialog._show_message_box(QMessageBox.Question, title, text, QMessageBox.Ok | QMessageBox.Cancel) == QMessageBox.Ok



if __name__ == '__main__':
    dialog = Dialog()
    while 1:
        print dialog.select_dir()
        print dialog.select_files(fileFilter='xlsx')
        if not dialog.show_msg_question(u'Хотите повторить?'):
            break
    print dialog.show_msg_info(u'Программа завершается')



