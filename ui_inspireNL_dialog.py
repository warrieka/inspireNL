# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_inspireNL_dialog.ui'
#
# Created: Mon Sep 14 22:23:39 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_inspireNLdlg(object):
    def setupUi(self, inspireNLdlg):
        inspireNLdlg.setObjectName(_fromUtf8("inspireNLdlg"))
        inspireNLdlg.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/inspireNL/images/wrench.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        inspireNLdlg.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(inspireNLdlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textEdit = QtGui.QTextEdit(inspireNLdlg)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.button_box = QtGui.QDialogButtonBox(inspireNLdlg)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(inspireNLdlg)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), inspireNLdlg.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), inspireNLdlg.reject)
        QtCore.QMetaObject.connectSlotsByName(inspireNLdlg)

    def retranslateUi(self, inspireNLdlg):
        inspireNLdlg.setWindowTitle(_translate("inspireNLdlg", "INSPIRE Nederland plugin voor QGIS", None))

import resources_rc
