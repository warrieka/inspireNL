# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dataCatalog_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dataCatalogDlg(object):
    def setupUi(self, dataCatalogDlg):
        dataCatalogDlg.setObjectName("dataCatalogDlg")
        dataCatalogDlg.resize(711, 623)
        dataCatalogDlg.setMinimumSize(QtCore.QSize(360, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/inspireNL/images/inspireSearch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dataCatalogDlg.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(dataCatalogDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.zoekTxt = QtWidgets.QComboBox(dataCatalogDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoekTxt.sizePolicy().hasHeightForWidth())
        self.zoekTxt.setSizePolicy(sizePolicy)
        self.zoekTxt.setEditable(True)
        self.zoekTxt.setObjectName("zoekTxt")
        self.horizontalLayout.addWidget(self.zoekTxt)
        self.zoekBtn = QtWidgets.QPushButton(dataCatalogDlg)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/plugins/geopunt4Qgis/images/magnifyingGlass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoekBtn.setIcon(icon1)
        self.zoekBtn.setCheckable(False)
        self.zoekBtn.setAutoDefault(True)
        self.zoekBtn.setDefault(True)
        self.zoekBtn.setFlat(False)
        self.zoekBtn.setObjectName("zoekBtn")
        self.horizontalLayout.addWidget(self.zoekBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.filterBox = QtWidgets.QGroupBox(dataCatalogDlg)
        self.filterBox.setCheckable(True)
        self.filterBox.setChecked(True)
        self.filterBox.setObjectName("filterBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.filterBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.filterWgt = QtWidgets.QWidget(self.filterBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterWgt.sizePolicy().hasHeightForWidth())
        self.filterWgt.setSizePolicy(sizePolicy)
        self.filterWgt.setObjectName("filterWgt")
        self.gridLayout = QtWidgets.QGridLayout(self.filterWgt)
        self.gridLayout.setObjectName("gridLayout")
        self.INSPIREthemaLbl = QtWidgets.QLabel(self.filterWgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INSPIREthemaLbl.sizePolicy().hasHeightForWidth())
        self.INSPIREthemaLbl.setSizePolicy(sizePolicy)
        self.INSPIREthemaLbl.setObjectName("INSPIREthemaLbl")
        self.gridLayout.addWidget(self.INSPIREthemaLbl, 0, 0, 1, 1)
        self.INSPIREthemaCbx = QtWidgets.QComboBox(self.filterWgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INSPIREthemaCbx.sizePolicy().hasHeightForWidth())
        self.INSPIREthemaCbx.setSizePolicy(sizePolicy)
        self.INSPIREthemaCbx.setSizeIncrement(QtCore.QSize(0, 0))
        self.INSPIREthemaCbx.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.INSPIREthemaCbx.setFrame(True)
        self.INSPIREthemaCbx.setObjectName("INSPIREthemaCbx")
        self.gridLayout.addWidget(self.INSPIREthemaCbx, 0, 1, 1, 1)
        self.typeLbl = QtWidgets.QLabel(self.filterWgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeLbl.sizePolicy().hasHeightForWidth())
        self.typeLbl.setSizePolicy(sizePolicy)
        self.typeLbl.setObjectName("typeLbl")
        self.gridLayout.addWidget(self.typeLbl, 0, 2, 1, 1)
        self.INSPIREserviceCbx = QtWidgets.QComboBox(self.filterWgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INSPIREserviceCbx.sizePolicy().hasHeightForWidth())
        self.INSPIREserviceCbx.setSizePolicy(sizePolicy)
        self.INSPIREserviceCbx.setSizeIncrement(QtCore.QSize(0, 0))
        self.INSPIREserviceCbx.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.INSPIREserviceCbx.setFrame(True)
        self.INSPIREserviceCbx.setObjectName("INSPIREserviceCbx")
        self.gridLayout.addWidget(self.INSPIREserviceCbx, 1, 3, 1, 1)
        self.INSPIREserviceLbl = QtWidgets.QLabel(self.filterWgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INSPIREserviceLbl.sizePolicy().hasHeightForWidth())
        self.INSPIREserviceLbl.setSizePolicy(sizePolicy)
        self.INSPIREserviceLbl.setObjectName("INSPIREserviceLbl")
        self.gridLayout.addWidget(self.INSPIREserviceLbl, 1, 2, 1, 1)
        self.typeCbx = QtWidgets.QComboBox(self.filterWgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeCbx.sizePolicy().hasHeightForWidth())
        self.typeCbx.setSizePolicy(sizePolicy)
        self.typeCbx.setSizeIncrement(QtCore.QSize(0, 0))
        self.typeCbx.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.typeCbx.setFrame(True)
        self.typeCbx.setObjectName("typeCbx")
        self.gridLayout.addWidget(self.typeCbx, 0, 3, 1, 1)
        self.organisatiesCbx = QtWidgets.QComboBox(self.filterWgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.organisatiesCbx.sizePolicy().hasHeightForWidth())
        self.organisatiesCbx.setSizePolicy(sizePolicy)
        self.organisatiesCbx.setSizeIncrement(QtCore.QSize(0, 0))
        self.organisatiesCbx.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.organisatiesCbx.setFrame(True)
        self.organisatiesCbx.setObjectName("organisatiesCbx")
        self.gridLayout.addWidget(self.organisatiesCbx, 1, 1, 1, 1)
        self.organisatiesLbl = QtWidgets.QLabel(self.filterWgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.organisatiesLbl.sizePolicy().hasHeightForWidth())
        self.organisatiesLbl.setSizePolicy(sizePolicy)
        self.organisatiesLbl.setObjectName("organisatiesLbl")
        self.gridLayout.addWidget(self.organisatiesLbl, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.filterWgt)
        self.verticalLayout.addWidget(self.filterBox)
        self.splitter = QtWidgets.QSplitter(dataCatalogDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.resultWgt = QtWidgets.QFrame(self.splitter)
        self.resultWgt.setMinimumSize(QtCore.QSize(120, 0))
        self.resultWgt.setBaseSize(QtCore.QSize(200, 0))
        self.resultWgt.setFrameShape(QtWidgets.QFrame.Panel)
        self.resultWgt.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.resultWgt.setObjectName("resultWgt")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.resultWgt)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.resultView = QtWidgets.QListView(self.resultWgt)
        self.resultView.setMinimumSize(QtCore.QSize(100, 0))
        self.resultView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.resultView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.resultView.setAlternatingRowColors(True)
        self.resultView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.resultView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.resultView.setObjectName("resultView")
        self.verticalLayout_2.addWidget(self.resultView)
        self.countLbl = QtWidgets.QLabel(self.resultWgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.countLbl.sizePolicy().hasHeightForWidth())
        self.countLbl.setSizePolicy(sizePolicy)
        self.countLbl.setText("")
        self.countLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.countLbl.setObjectName("countLbl")
        self.verticalLayout_2.addWidget(self.countLbl)
        self.modelFilter = QtWidgets.QFrame(self.resultWgt)
        self.modelFilter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.modelFilter.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.modelFilter.setObjectName("modelFilter")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.modelFilter)
        self.horizontalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.modelFilter)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.modelFilterCbx = QtWidgets.QComboBox(self.modelFilter)
        self.modelFilterCbx.setObjectName("modelFilterCbx")
        self.modelFilterCbx.addItem("")
        self.modelFilterCbx.addItem("")
        self.modelFilterCbx.addItem("")
        self.modelFilterCbx.addItem("")
        self.modelFilterCbx.addItem("")
        self.modelFilterCbx.addItem("")
        self.horizontalLayout_6.addWidget(self.modelFilterCbx)
        self.verticalLayout_2.addWidget(self.modelFilter)
        self.descriptionText = QtWidgets.QTextBrowser(self.splitter)
        self.descriptionText.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.descriptionText.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.descriptionText.setOpenExternalLinks(True)
        self.descriptionText.setObjectName("descriptionText")
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addWMSbtn = QtWidgets.QPushButton(dataCatalogDlg)
        self.addWMSbtn.setEnabled(False)
        self.addWMSbtn.setMinimumSize(QtCore.QSize(0, 0))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/plugins/inspireNL/images/WmsLayer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addWMSbtn.setIcon(icon2)
        self.addWMSbtn.setAutoDefault(False)
        self.addWMSbtn.setObjectName("addWMSbtn")
        self.horizontalLayout_2.addWidget(self.addWMSbtn)
        self.addWFSbtn = QtWidgets.QPushButton(dataCatalogDlg)
        self.addWFSbtn.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/plugins/inspireNL/images/WfsLayer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addWFSbtn.setIcon(icon3)
        self.addWFSbtn.setAutoDefault(False)
        self.addWFSbtn.setObjectName("addWFSbtn")
        self.horizontalLayout_2.addWidget(self.addWFSbtn)
        self.addWCSbtn = QtWidgets.QPushButton(dataCatalogDlg)
        self.addWCSbtn.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/plugins/inspireNL/images/WcsLayer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addWCSbtn.setIcon(icon4)
        self.addWCSbtn.setObjectName("addWCSbtn")
        self.horizontalLayout_2.addWidget(self.addWCSbtn)
        self.addWMTSbtn = QtWidgets.QPushButton(dataCatalogDlg)
        self.addWMTSbtn.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/plugins/inspireNL/images/tiles.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addWMTSbtn.setIcon(icon5)
        self.addWMTSbtn.setObjectName("addWMTSbtn")
        self.horizontalLayout_2.addWidget(self.addWMTSbtn)
        self.DLbtn = QtWidgets.QPushButton(dataCatalogDlg)
        self.DLbtn.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/plugins/inspireNL/images/zip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DLbtn.setIcon(icon6)
        self.DLbtn.setAutoDefault(False)
        self.DLbtn.setObjectName("DLbtn")
        self.horizontalLayout_2.addWidget(self.DLbtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.closeBtn = QtWidgets.QPushButton(dataCatalogDlg)
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_2.addWidget(self.closeBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.msgLbl = QtWidgets.QLabel(dataCatalogDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msgLbl.sizePolicy().hasHeightForWidth())
        self.msgLbl.setSizePolicy(sizePolicy)
        self.msgLbl.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.msgLbl.setOpenExternalLinks(True)
        self.msgLbl.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.msgLbl.setObjectName("msgLbl")
        self.horizontalLayout_3.addWidget(self.msgLbl)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.addWMSaction = QtWidgets.QAction(dataCatalogDlg)
        self.addWMSaction.setObjectName("addWMSaction")
        self.Download_action = QtWidgets.QAction(dataCatalogDlg)
        self.Download_action.setObjectName("Download_action")
        self.addWFSaction = QtWidgets.QAction(dataCatalogDlg)
        self.addWFSaction.setObjectName("addWFSaction")

        self.retranslateUi(dataCatalogDlg)
        self.filterBox.toggled['bool'].connect(self.filterWgt.setVisible)
        self.closeBtn.clicked.connect(dataCatalogDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(dataCatalogDlg)

    def retranslateUi(self, dataCatalogDlg):
        _translate = QtCore.QCoreApplication.translate
        dataCatalogDlg.setWindowTitle(_translate("dataCatalogDlg", "Zoek INSPIRE Datasets en services"))
        self.zoekBtn.setText(_translate("dataCatalogDlg", "Zoek"))
        self.filterBox.setTitle(_translate("dataCatalogDlg", "Uitgebreide zoekcriteria"))
        self.INSPIREthemaLbl.setText(_translate("dataCatalogDlg", "INSPIRE-thema:"))
        self.typeLbl.setText(_translate("dataCatalogDlg", "Type:"))
        self.INSPIREserviceLbl.setText(_translate("dataCatalogDlg", "Servicetype:"))
        self.organisatiesLbl.setText(_translate("dataCatalogDlg", "Organisatie:"))
        self.label.setText(_translate("dataCatalogDlg", "Enkel resultaten met:"))
        self.modelFilterCbx.setItemText(0, _translate("dataCatalogDlg", "Alle lagen"))
        self.modelFilterCbx.setItemText(1, _translate("dataCatalogDlg", "WMS"))
        self.modelFilterCbx.setItemText(2, _translate("dataCatalogDlg", "WFS"))
        self.modelFilterCbx.setItemText(3, _translate("dataCatalogDlg", "Download"))
        self.modelFilterCbx.setItemText(4, _translate("dataCatalogDlg", "WCS"))
        self.modelFilterCbx.setItemText(5, _translate("dataCatalogDlg", "WMTS"))
        self.addWMSbtn.setText(_translate("dataCatalogDlg", "WMS "))
        self.addWFSbtn.setText(_translate("dataCatalogDlg", "WFS "))
        self.addWCSbtn.setText(_translate("dataCatalogDlg", "WCS"))
        self.addWMTSbtn.setText(_translate("dataCatalogDlg", "WMTS"))
        self.DLbtn.setText(_translate("dataCatalogDlg", "Downloaden"))
        self.closeBtn.setText(_translate("dataCatalogDlg", "Sluiten"))
        self.msgLbl.setText(_translate("dataCatalogDlg", "<html><head/><body><p><a href=\"http://www.nationaalgeoregister.nl/\"><span style=\" text-decoration: underline; color:#0000ff;\">http://www.nationaalgeoregister.nl/</span></a></p></body></html>"))
        self.addWMSaction.setText(_translate("dataCatalogDlg", "WMS toevoegen"))
        self.Download_action.setText(_translate("dataCatalogDlg", "Downloadpagina openen"))
        self.addWFSaction.setText(_translate("dataCatalogDlg", "WFS toevoegen"))

from . import resources_rc