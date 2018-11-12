# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_inspireNL_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_inspireNLdlg(object):
    def setupUi(self, inspireNLdlg):
        inspireNLdlg.setObjectName("inspireNLdlg")
        inspireNLdlg.resize(521, 396)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/inspireNL/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        inspireNLdlg.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(inspireNLdlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(inspireNLdlg)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.button_box = QtWidgets.QDialogButtonBox(inspireNLdlg)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.button_box.setObjectName("button_box")
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(inspireNLdlg)
        self.button_box.accepted.connect(inspireNLdlg.accept)
        self.button_box.rejected.connect(inspireNLdlg.reject)
        QtCore.QMetaObject.connectSlotsByName(inspireNLdlg)

    def retranslateUi(self, inspireNLdlg):
        _translate = QtCore.QCoreApplication.translate
        inspireNLdlg.setWindowTitle(_translate("inspireNLdlg", "INSPIRE Nederland plugin voor QGIS"))
        self.textEdit.setHtml(_translate("inspireNLdlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:600;\">OVER</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">In Nederland zijn inmiddels zijn meer dan 350 datasets en bijbehorende services geregistreerd in het Nationaal Georegister (http://www.nationaalgeoregister.nl/)  als INSPIRE dataset of service. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">Om het gebruik te vergemakkelijken voor de professionele GIS-gebruikers in Nederland worden voor de twee meest gebruikte GIS software pakketten – te weten QGIS en ArcGIS Desktop – plugins ontwikkeld. Deze plugins maken het gemakkelijk om direct via het Nationaal Georegister de INSPIRE datasets en services te vinden, te raadplegen en te downloaden. Deze plugin is de QGIS-versie.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">Auteur: Kay Warrie (kaywarrie@gmail.com) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">In opdracht van Geonovum</span></p></body></html>"))

from . import resources_rc
