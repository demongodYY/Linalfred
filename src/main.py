#!/usr/bin/python3
# coding=utf-8
import sys

from globalhotkey import initGlobalHotKey
from singleton import SingletonApp
from ui.maindlg import MainDlg

__author__ = 'peter'

if __name__ == "__main__":
    app = SingletonApp(sys.argv)
    if app.is_running:
        app.send_message(sys.argv)
    else:
        dlg = MainDlg()
        initGlobalHotKey(dlg)
        dlg.show()
        app.setDlg(dlg)
        sys.exit(app.exec_())
