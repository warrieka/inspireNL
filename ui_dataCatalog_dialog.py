# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dataCatalog_dialog.ui'
#
# Created: Wed Sep 02 16:55:44 2015
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

class Ui_dataCatalogDlg(object):
    def setupUi(self, dataCatalogDlg):
        dataCatalogDlg.setObjectName(_fromUtf8("dataCatalogDlg"))
        dataCatalogDlg.resize(571, 534)
        dataCatalogDlg.setMinimumSize(QtCore.QSize(360, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/inspireNL/images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dataCatalogDlg.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(dataCatalogDlg)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.zoekTxt = QtGui.QComboBox(dataCatalogDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoekTxt.sizePolicy().hasHeightForWidth())
        self.zoekTxt.setSizePolicy(sizePolicy)
        self.zoekTxt.setEditable(True)
        self.zoekTxt.setObjectName(_fromUtf8("zoekTxt"))
        self.horizontalLayout.addWidget(self.zoekTxt)
        self.zoekBtn = QtGui.QPushButton(dataCatalogDlg)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/magnifyingGlass.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoekBtn.setIcon(icon1)
        self.zoekBtn.setCheckable(False)
        self.zoekBtn.setAutoDefault(True)
        self.zoekBtn.setDefault(True)
        self.zoekBtn.setFlat(False)
        self.zoekBtn.setObjectName(_fromUtf8("zoekBtn"))
        self.horizontalLayout.addWidget(self.zoekBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.filterBox = QtGui.QGroupBox(dataCatalogDlg)
        self.filterBox.setCheckable(True)
        self.filterBox.setChecked(False)
        self.filterBox.setObjectName(_fromUtf8("filterBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.filterBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.filterWgt = QtGui.QWidget(self.filterBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterWgt.sizePolicy().hasHeightForWidth())
        self.filterWgt.setSizePolicy(sizePolicy)
        self.filterWgt.setObjectName(_fromUtf8("filterWgt"))
        self.gridLayout = QtGui.QGridLayout(self.filterWgt)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.INSPIREthemaCbx = QtGui.QComboBox(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INSPIREthemaCbx.sizePolicy().hasHeightForWidth())
        self.INSPIREthemaCbx.setSizePolicy(sizePolicy)
        self.INSPIREthemaCbx.setSizeIncrement(QtCore.QSize(0, 0))
        self.INSPIREthemaCbx.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.INSPIREthemaCbx.setFrame(True)
        self.INSPIREthemaCbx.setObjectName(_fromUtf8("INSPIREthemaCbx"))
        self.gridLayout.addWidget(self.INSPIREthemaCbx, 5, 3, 1, 1)
        self.INSPIREthemaLbl = QtGui.QLabel(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INSPIREthemaLbl.sizePolicy().hasHeightForWidth())
        self.INSPIREthemaLbl.setSizePolicy(sizePolicy)
        self.INSPIREthemaLbl.setObjectName(_fromUtf8("INSPIREthemaLbl"))
        self.gridLayout.addWidget(self.INSPIREthemaLbl, 5, 2, 1, 1)
        self.INSPIREannexLbl = QtGui.QLabel(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INSPIREannexLbl.sizePolicy().hasHeightForWidth())
        self.INSPIREannexLbl.setSizePolicy(sizePolicy)
        self.INSPIREannexLbl.setObjectName(_fromUtf8("INSPIREannexLbl"))
        self.gridLayout.addWidget(self.INSPIREannexLbl, 4, 2, 1, 1)
        self.INSPIREannexCbx = QtGui.QComboBox(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INSPIREannexCbx.sizePolicy().hasHeightForWidth())
        self.INSPIREannexCbx.setSizePolicy(sizePolicy)
        self.INSPIREannexCbx.setSizeIncrement(QtCore.QSize(0, 0))
        self.INSPIREannexCbx.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.INSPIREannexCbx.setFrame(True)
        self.INSPIREannexCbx.setObjectName(_fromUtf8("INSPIREannexCbx"))
        self.gridLayout.addWidget(self.INSPIREannexCbx, 4, 3, 1, 1)
        self.INSPIREserviceLbl = QtGui.QLabel(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INSPIREserviceLbl.sizePolicy().hasHeightForWidth())
        self.INSPIREserviceLbl.setSizePolicy(sizePolicy)
        self.INSPIREserviceLbl.setObjectName(_fromUtf8("INSPIREserviceLbl"))
        self.gridLayout.addWidget(self.INSPIREserviceLbl, 6, 2, 1, 1)
        self.INSPIREserviceCbx = QtGui.QComboBox(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INSPIREserviceCbx.sizePolicy().hasHeightForWidth())
        self.INSPIREserviceCbx.setSizePolicy(sizePolicy)
        self.INSPIREserviceCbx.setSizeIncrement(QtCore.QSize(0, 0))
        self.INSPIREserviceCbx.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.INSPIREserviceCbx.setFrame(True)
        self.INSPIREserviceCbx.setObjectName(_fromUtf8("INSPIREserviceCbx"))
        self.gridLayout.addWidget(self.INSPIREserviceCbx, 6, 3, 1, 1)
        self.organisatiesCbx = QtGui.QComboBox(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.organisatiesCbx.sizePolicy().hasHeightForWidth())
        self.organisatiesCbx.setSizePolicy(sizePolicy)
        self.organisatiesCbx.setSizeIncrement(QtCore.QSize(0, 0))
        self.organisatiesCbx.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.organisatiesCbx.setFrame(True)
        self.organisatiesCbx.setObjectName(_fromUtf8("organisatiesCbx"))
        self.gridLayout.addWidget(self.organisatiesCbx, 4, 1, 1, 1)
        self.organisatiesLbl = QtGui.QLabel(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.organisatiesLbl.sizePolicy().hasHeightForWidth())
        self.organisatiesLbl.setSizePolicy(sizePolicy)
        self.organisatiesLbl.setObjectName(_fromUtf8("organisatiesLbl"))
        self.gridLayout.addWidget(self.organisatiesLbl, 4, 0, 1, 1)
        self.bronLbl = QtGui.QLabel(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bronLbl.sizePolicy().hasHeightForWidth())
        self.bronLbl.setSizePolicy(sizePolicy)
        self.bronLbl.setObjectName(_fromUtf8("bronLbl"))
        self.gridLayout.addWidget(self.bronLbl, 5, 0, 1, 1)
        self.bronCbx = QtGui.QComboBox(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bronCbx.sizePolicy().hasHeightForWidth())
        self.bronCbx.setSizePolicy(sizePolicy)
        self.bronCbx.setSizeIncrement(QtCore.QSize(0, 0))
        self.bronCbx.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bronCbx.setFrame(True)
        self.bronCbx.setObjectName(_fromUtf8("bronCbx"))
        self.gridLayout.addWidget(self.bronCbx, 5, 1, 1, 1)
        self.typeLbl = QtGui.QLabel(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeLbl.sizePolicy().hasHeightForWidth())
        self.typeLbl.setSizePolicy(sizePolicy)
        self.typeLbl.setObjectName(_fromUtf8("typeLbl"))
        self.gridLayout.addWidget(self.typeLbl, 6, 0, 1, 1)
        self.typeCbx = QtGui.QComboBox(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeCbx.sizePolicy().hasHeightForWidth())
        self.typeCbx.setSizePolicy(sizePolicy)
        self.typeCbx.setSizeIncrement(QtCore.QSize(0, 0))
        self.typeCbx.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.typeCbx.setFrame(True)
        self.typeCbx.setObjectName(_fromUtf8("typeCbx"))
        self.gridLayout.addWidget(self.typeCbx, 6, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.filterWgt)
        self.verticalLayout.addWidget(self.filterBox)
        self.splitter = QtGui.QSplitter(dataCatalogDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.resultWgt = QtGui.QFrame(self.splitter)
        self.resultWgt.setMinimumSize(QtCore.QSize(120, 0))
        self.resultWgt.setBaseSize(QtCore.QSize(200, 0))
        self.resultWgt.setFrameShape(QtGui.QFrame.Panel)
        self.resultWgt.setFrameShadow(QtGui.QFrame.Sunken)
        self.resultWgt.setObjectName(_fromUtf8("resultWgt"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.resultWgt)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.resultView = QtGui.QListView(self.resultWgt)
        self.resultView.setMinimumSize(QtCore.QSize(100, 0))
        self.resultView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.resultView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.resultView.setAlternatingRowColors(True)
        self.resultView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.resultView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.resultView.setObjectName(_fromUtf8("resultView"))
        self.verticalLayout_2.addWidget(self.resultView)
        self.countLbl = QtGui.QLabel(self.resultWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.countLbl.sizePolicy().hasHeightForWidth())
        self.countLbl.setSizePolicy(sizePolicy)
        self.countLbl.setText(_fromUtf8(""))
        self.countLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.countLbl.setObjectName(_fromUtf8("countLbl"))
        self.verticalLayout_2.addWidget(self.countLbl)
        self.modelFilter = QtGui.QFrame(self.resultWgt)
        self.modelFilter.setFrameShape(QtGui.QFrame.NoFrame)
        self.modelFilter.setFrameShadow(QtGui.QFrame.Sunken)
        self.modelFilter.setObjectName(_fromUtf8("modelFilter"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.modelFilter)
        self.horizontalLayout_6.setMargin(1)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label = QtGui.QLabel(self.modelFilter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.modelFilterCbx = QtGui.QComboBox(self.modelFilter)
        self.modelFilterCbx.setObjectName(_fromUtf8("modelFilterCbx"))
        self.modelFilterCbx.addItem(_fromUtf8(""))
        self.modelFilterCbx.addItem(_fromUtf8(""))
        self.modelFilterCbx.addItem(_fromUtf8(""))
        self.modelFilterCbx.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.modelFilterCbx)
        self.verticalLayout_2.addWidget(self.modelFilter)
        self.descriptionText = QtGui.QTextBrowser(self.splitter)
        self.descriptionText.setFrameShape(QtGui.QFrame.StyledPanel)
        self.descriptionText.setFrameShadow(QtGui.QFrame.Sunken)
        self.descriptionText.setOpenExternalLinks(True)
        self.descriptionText.setObjectName(_fromUtf8("descriptionText"))
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.addWMSbtn = QtGui.QPushButton(dataCatalogDlg)
        self.addWMSbtn.setEnabled(False)
        self.addWMSbtn.setMinimumSize(QtCore.QSize(0, 0))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/Wms.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addWMSbtn.setIcon(icon2)
        self.addWMSbtn.setAutoDefault(False)
        self.addWMSbtn.setObjectName(_fromUtf8("addWMSbtn"))
        self.horizontalLayout_2.addWidget(self.addWMSbtn)
        self.addWFSbtn = QtGui.QPushButton(dataCatalogDlg)
        self.addWFSbtn.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/Wfs.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addWFSbtn.setIcon(icon3)
        self.addWFSbtn.setAutoDefault(False)
        self.addWFSbtn.setObjectName(_fromUtf8("addWFSbtn"))
        self.horizontalLayout_2.addWidget(self.addWFSbtn)
        self.DLbtn = QtGui.QPushButton(dataCatalogDlg)
        self.DLbtn.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/zip.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DLbtn.setIcon(icon4)
        self.DLbtn.setAutoDefault(False)
        self.DLbtn.setObjectName(_fromUtf8("DLbtn"))
        self.horizontalLayout_2.addWidget(self.DLbtn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(dataCatalogDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Help)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_4.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.msgLbl = QtGui.QLabel(dataCatalogDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msgLbl.sizePolicy().hasHeightForWidth())
        self.msgLbl.setSizePolicy(sizePolicy)
        self.msgLbl.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.msgLbl.setOpenExternalLinks(True)
        self.msgLbl.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.msgLbl.setObjectName(_fromUtf8("msgLbl"))
        self.verticalLayout.addWidget(self.msgLbl)
        self.addWMSaction = QtGui.QAction(dataCatalogDlg)
        self.addWMSaction.setObjectName(_fromUtf8("addWMSaction"))
        self.Download_action = QtGui.QAction(dataCatalogDlg)
        self.Download_action.setObjectName(_fromUtf8("Download_action"))
        self.addWFSaction = QtGui.QAction(dataCatalogDlg)
        self.addWFSaction.setObjectName(_fromUtf8("addWFSaction"))

        self.retranslateUi(dataCatalogDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), dataCatalogDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), dataCatalogDlg.reject)
        QtCore.QObject.connect(self.filterBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.filterWgt.setVisible)
        QtCore.QMetaObject.connectSlotsByName(dataCatalogDlg)

    def retranslateUi(self, dataCatalogDlg):
        dataCatalogDlg.setWindowTitle(_translate("dataCatalogDlg", "Nationaal Georegister", None))
        self.zoekBtn.setText(_translate("dataCatalogDlg", "Zoek", None))
        self.filterBox.setTitle(_translate("dataCatalogDlg", "Uitgebreide zoekcriteria", None))
        self.INSPIREthemaLbl.setText(_translate("dataCatalogDlg", "INSPIRE-thema:", None))
        self.INSPIREannexLbl.setText(_translate("dataCatalogDlg", "INSPIRE-annex:", None))
        self.INSPIREserviceLbl.setText(_translate("dataCatalogDlg", "INSPIRE-servicetype:", None))
        self.organisatiesLbl.setText(_translate("dataCatalogDlg", "Organisatie:", None))
        self.bronLbl.setText(_translate("dataCatalogDlg", "Bron catalogus:", None))
        self.typeLbl.setText(_translate("dataCatalogDlg", "Type:", None))
        self.label.setText(_translate("dataCatalogDlg", "Enkel resultaten met:", None))
        self.modelFilterCbx.setItemText(0, _translate("dataCatalogDlg", "Alle lagen", None))
        self.modelFilterCbx.setItemText(1, _translate("dataCatalogDlg", "WMS", None))
        self.modelFilterCbx.setItemText(2, _translate("dataCatalogDlg", "WFS", None))
        self.modelFilterCbx.setItemText(3, _translate("dataCatalogDlg", "Download", None))
        self.addWMSbtn.setText(_translate("dataCatalogDlg", "WMS toevoegen", None))
        self.addWFSbtn.setText(_translate("dataCatalogDlg", "WFS toevoegen", None))
        self.DLbtn.setText(_translate("dataCatalogDlg", "Downloaden", None))
        self.msgLbl.setText(_translate("dataCatalogDlg", "<html><head/><body><p><a href=\"http://www.nationaalgeoregister.nl/\"><span style=\" text-decoration: underline; color:#0000ff;\">http://www.nationaalgeoregister.nl/</span></a></p></body></html>", None))
        self.addWMSaction.setText(_translate("dataCatalogDlg", "WMS toevoegen", None))
        self.Download_action.setText(_translate("dataCatalogDlg", "Downloadpagina openen", None))
        self.addWFSaction.setText(_translate("dataCatalogDlg", "WFS toevoegen", None))

import resources_rc
