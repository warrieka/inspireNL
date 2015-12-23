# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_inspireNL_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        inspireNLdlg.resize(456, 358)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/inspireNL/images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.textEdit.setHtml(_translate("inspireNLdlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">OVER</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In Nederland zijn inmiddels zijn meer dan 350 datasets en bijbehorende services geregistreerd in het Nationaal Georegister (http://www.nationaalgeoregister.nl/)  als INSPIRE dataset of service. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Om het gebruik te vergemakkelijken voor de professionele GIS-gebruikers in Nederland worden voor de twee meest gebruikte GIS software pakketten – te weten QGIS en ArcGIS Desktop – plugins ontwikkeld. Deze plugins maken het gemakkelijk om direct via het Nationaal Georegister de INSPIRE datasets en services te vinden, te raadplegen en te downloaden. Deze plugin is de QGIS-versie.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Auteur: Kay Warrie (kaywarrie@gmail.com) </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In opdracht van Geonovum</p></body></html>", None))

import resources_rc
