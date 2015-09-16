# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_inspireNL_dialog.ui'
#
# Created: Wed Sep 16 14:33:01 2015
#      by: PyQt4 UI code generator 4.10.2
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
        self.textEdit.setHtml(_translate("inspireNLdlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">OVER</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Het Nationaal Georegister (NGR) is dé centrale voorziening voor het beschrijven en ontsluiten van geo-informatie van Nederland. Het NGR bevat het overzicht van beschikbare datasets en services. Vele van deze datasets beschikken over services die u in QGIS kunt toevoegen. De bedoeling van deze plugin is om het opzoeken en toevoegen aan QGIS als te vergemakkelijken door het aan te bieden geintegreerd QGIS.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">De INSPIRE-implementatie in Nederland komt nu in een fase waarin het niet langer alleen maar gaat om het aanbod en om het tijdig voldoen aan de Europese wettelijke verplichtingen. Nu een toenemend aantal INSPIRE datasets en services ook daadwerkelijk beschikbaar begint te komen, wordt aandacht voor het gebruik en de toepassing ervan geleidelijk aan steeds actueler en belangrijker. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Daarnaast is van belang dat de INSPIRE-implementatie niet op zichzelf staat, maar plaatsvindt in een context waarin ook allerlei andere zaken en ontwikkelingen spelen, waar samenhang mee aanwezig is, afstemming mee dient plaats te vinden en waar actieve aandacht voor het opsporen en waar mogelijk benutten van synergie aan de orde is. Inmiddels zijn meer dan 350 datasets en bijbehorende services geregistreerd in het nationaal georegister geregistreerd als INSPIRE dataset of service. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Om het gebruik te vergemakkelijken voor de professionele GIS-gebruikers in Nederland worden voor twee meest gebruikte GIS software pakketten – te weten QGIS en ArcGIS Desktop – plugins ontwikkeld. Deze plugins maken het makkelijk om direct via het Nationaal Georegister (http://www.nationaalgeoregister.nl/) de INSPIRE datasets en services te vinden, te raadplegen en te downloaden. Deze plugin is de QGIS-versie.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Auteur: Kay Warrie (kaywarrie@gmail.com) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">In opdracht van Geonovum</span></p></body></html>", None))

import resources_rc
