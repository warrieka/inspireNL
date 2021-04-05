# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\work\prj\geonovum\inspireNL\ui_inspireNL_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_inspireNLdlg(object):
    def setupUi(self, inspireNLdlg):
        inspireNLdlg.setObjectName("inspireNLdlg")
        inspireNLdlg.resize(636, 590)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/inspireNL/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        inspireNLdlg.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(inspireNLdlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(inspireNLdlg)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.button_box = QtWidgets.QDialogButtonBox(inspireNLdlg)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.button_box.setObjectName("button_box")
        self.verticalLayout_2.addWidget(self.button_box)

        self.retranslateUi(inspireNLdlg)
        self.button_box.accepted.connect(inspireNLdlg.accept)
        self.button_box.rejected.connect(inspireNLdlg.reject)
        QtCore.QMetaObject.connectSlotsByName(inspireNLdlg)

    def retranslateUi(self, inspireNLdlg):
        _translate = QtCore.QCoreApplication.translate
        inspireNLdlg.setWindowTitle(_translate("inspireNLdlg", "INSPIRE Nederland plugin voor QGIS"))
        self.textBrowser.setDocumentTitle(_translate("inspireNLdlg", "Over"))
        self.textBrowser.setHtml(_translate("inspireNLdlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Over</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">Over de Nederlandse INSPIRE QGIS plugin</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#000000;\">In het kader van INSPIRE realiseren de Europese lidstaten een digitaal netwerk voor het uitwisselen van gegevens over de leefomgeving. INSPIRE zorgt ervoor dat deze geo-informatie van goede kwaliteit is en dat de inhoud ervan, oo</span><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#222222;\">k over de landsgrenzen heen, op elkaar is afgestemd. In Nederland zijn inmiddels beschrijvingen van meer dan 200 INSPIRE datasets en circa 265 bijbehorende services aanwezig in het Nationaal Georeg</span><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#000000;\">ister (</span><a href=\"http://www.nationaalgeoregister.nl/\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; text-decoration: underline; color:#1155cc;\">http://www.nationaalgeoregister.nl/</span></a><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#000000;\">)</span><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; text-decoration: line-through; color:#000000;\">.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#222222;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#222222; background-color:#ffffff;\">Om het gebruik van INSPIRE data te vergemakkelijken voor de professionele GIS-gebruikers in Nederland is voor QGIS een plugin ontwikkeld. Deze plugin maakt het gemakkelijk om direct via het Nationaal Georegister de INSPIRE datasets en services te vinden, te raadplegen en te downloaden. Via de plugin kan een gebruiker INSPIRE-data zoeken op trefwoord, INSPIRE-thema, organisatie of type service en het gevonden resultaat direct toevoegen aan QGIS.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#000000;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#000000;\">De INSPIRE QGIS plugin is tot stand gekomen onder verantwoordelijkheid van Geonovum. Geonovum ondersteunt het ministerie van Binnenlandse Zaken en Koninkrijkrelaties en dataproviders bij de invoering van INSPIRE in Nederland. De plugin is ontwikkeld door KGIS (</span><a href=\"http://kgis.be/\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; text-decoration: underline; color:#1155cc;\">http://kgis.be/</span></a><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#000000;\">).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#000000;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#000000;\">Heeft u vragen over INSPIRE of de plugin, kijk dan op </span><a href=\"https://www.geonovum.nl/geo-standaarden/inspire-europese-leefomgeving/qgis-plugin\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">https://www.geonovum.nl/geo-standaarden/inspire-europese-leefomgeving/qgis-plugin</span></a><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#000000;\"> of stel ze aan de INSPIRE helpdesk (</span><a href=\"mailto:inspire@geonovum.nl\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; text-decoration: underline; color:#1155cc;\">inspire@geonovum.nl</span></a><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#000000;\">).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#000000;\">Auteur: Kay Warrie (</span><a href=\"mailto:kaywarrie@gmail.com\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; text-decoration: underline; color:#1155cc;\">kaywarrie@</span></a><a href=\"http://kgis.be/\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; text-decoration: underline; color:#1155cc;\">kgis.be</span></a><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#000000;\">)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:8pt; color:#000000;\">In opdracht van Geonovum</span></p></body></html>"))
from . import resources_rc
