# -*- coding: utf-8 -*-
#from __future__ import absolute_import
from qgis.PyQt.QtCore import Qt, QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QCursor, QStandardItemModel, QStandardItem
from qgis.PyQt.QtWidgets import QApplication, QDialog, QSizePolicy, QCompleter, QInputDialog
from qgis.PyQt.QtCore import QSortFilterProxyModel, QRegExp, QStringListModel
from .ui_dataCatalog_dialog import Ui_dataCatalogDlg
from qgis.core import QgsProject, QgsVectorLayer, QgsRasterLayer, Qgis
from qgis.gui import QgsMessageBar 
import sys, os, webbrowser
from . import geometryhelper as gh
from .settings import settings
from . import metadataParser as metadata
from .metadataParser import MDReader, MDdata, getWmsLayerNames, getWFSLayerNames, makeWFSuri, getWMTSlayersNames, makeWMTSuri,  getWCSlayerNames, makeWCSuri

class dataCatalog(QDialog):
    def __init__(self, iface):
        QDialog.__init__(self, None)
        self.setWindowFlags( self.windowFlags() & ~Qt.WindowContextHelpButtonHint )
        #self.setWindowFlags( self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.iface = iface
    
        # initialize locale
        locale = QSettings().value("locale/userLocale", "nl")
        locale = locale[0:2]
        localePath = os.path.join(os.path.dirname(__file__), 'i18n', '{}.qm'.format(locale))
        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)
    
        self._initGui()

    def _initGui(self):
        """setup the user interface"""
        self.ui = Ui_dataCatalogDlg()
        self.ui.setupUi(self)
        
        #get settings
        self.s = settings()

        self.gh = gh.geometryHelper( self.iface )
        
        #setup a message bar
        self.bar = QgsMessageBar() 
        self.bar.setSizePolicy( QSizePolicy.Minimum, QSizePolicy.Fixed )
        self.ui.verticalLayout.addWidget(self.bar)
        #vars
        self.firstShow = True
        self.wms = None
        self.wfs = None
        self.wmts = None
        self.wcs = None
        self.dl = None
        self.zoek = ''
        #datamodel
        self.model = QStandardItemModel(self)
        self.proxyModel = QSortFilterProxyModel(self)
        self.proxyModel.setSourceModel(self.model)
        self.ui.resultView.setModel( self.proxyModel )
        #completer
        self.completer = QCompleter( self )
        self.completerModel = QStringListModel(self)
        self.ui.zoekTxt.setCompleter(self.completer )
        self.completer.setModel(self.completerModel )
        
        self.md = metadata.MDReader(timeout=self.s.timeout, proxyUrl=self.s.proxyUrl)
  
        #eventhandlers 
        self.ui.zoekBtn.clicked.connect(self.onZoekClicked)
        self.ui.addWMSbtn.clicked.connect(self.addWMS)
        self.ui.addWFSbtn.clicked.connect(self.addWFS)
        self.ui.addWMTSbtn.clicked.connect(self.addWMTS)
        self.ui.addWCSbtn.clicked.connect(self.addWCS)
        self.ui.DLbtn.clicked.connect(lambda: self.openUrl(self.dl))
        self.ui.resultView.clicked.connect(self.resultViewClicked)
        self.ui.modelFilterCbx.currentIndexChanged.connect(self.modelFilterCbxIndexChanged)
        self.finished.connect(self.clean)

    def _setModel(self, records):   
        self.model.clear()
        reclist = sorted(records, key=lambda k: k['title']) 
         
        for rec in reclist:
            title = QStandardItem( rec['title'] )             #0
            wms = QStandardItem( rec['wms'][1] )              #1
            downloadLink = QStandardItem(rec['download'])     #2
            id = QStandardItem( rec['uuid'] )                 #3
            abstract = QStandardItem( rec['abstract'] )       #4
            wfs =      QStandardItem( rec['wfs'][1] )         #5
            wcs =      QStandardItem( rec['wcs'][1] )         #6
            wmts =     QStandardItem( rec['wmts'][1] )        #7
            ### 
            wmsName =  QStandardItem( rec['wms'][0] )         #8
            wfsName =  QStandardItem( rec['wfs'][0] )         #9
            wcsName =  QStandardItem( rec['wcs'][0] )         #10
            wmtsName = QStandardItem( rec['wmts'][0] )        #11
            self.model.appendRow([title,wms,downloadLink,id,abstract,wfs,wcs,wmts,wmsName,wfsName,wcsName,wmtsName])

    #overwrite
    def show(self):
        QDialog.show(self)
        self.setWindowModality(0)
        if self.firstShow:
            self.ui.organisatiesCbx.addItems( ['']+ self.md.list_organisations() )
            keywords = sorted( self.md.list_suggestionKeyword() ) 
            self.completerModel.setStringList( keywords )
            self.bronnen = self.md.list_bronnen()
            #self.ui.keywordCbx.addItems( ['']+ keywords )
            self.ui.typeCbx.addItems( ['']+  [ n[0] for n in self.md.dataTypes] )                
            
            self.ui.INSPIREannexCbx.addItems( ['']+ self.md.inspireannex )
            self.ui.INSPIREserviceCbx.addItems( ['']+ self.md.inspireServiceTypes )
            self.ui.INSPIREthemaCbx.addItems( ['']+ self.md.list_inspire_theme() )
            self.firstShow = False      
      
    #eventhandlers
    def resultViewClicked(self):
        if self.ui.resultView.selectedIndexes(): 
           row = self.ui.resultView.selectedIndexes()[0].row()  
           
           self.wms = self.proxyModel.data( self.proxyModel.index( row, 1) )
           self.dl  = self.proxyModel.data( self.proxyModel.index( row, 2) )
           self.wfs = self.proxyModel.data( self.proxyModel.index( row, 5) )
           self.wcs = self.proxyModel.data( self.proxyModel.index( row, 6) )
           self.wmts= self.proxyModel.data( self.proxyModel.index( row, 7) )
           ##
           self.wmsLr   = self.proxyModel.data( self.proxyModel.index( row, 8) )
           self.wfsLr   = self.proxyModel.data( self.proxyModel.index( row, 9) )
           self.wcsLr   = self.proxyModel.data( self.proxyModel.index( row, 10) )
           self.wmtsLr  = self.proxyModel.data( self.proxyModel.index( row, 11) )
           ##
           title    = self.proxyModel.data( self.proxyModel.index( row, 0) )
           uuid     = self.proxyModel.data( self.proxyModel.index( row, 3) )
           abstract = self.proxyModel.data( self.proxyModel.index( row, 4) )
           
           self.ui.descriptionText.setText(
             """<h3>%s</h3><div>%s</div><br/><br/>
             <a href='http://www.nationaalgeoregister.nl/geonetwork/srv/search/?uuid=%s'>
             Bekijk in Nationaal Georegister</a>""" %  (title , abstract, uuid ))
           
           if self.wms: self.ui.addWMSbtn.setEnabled(1)
           else: self.ui.addWMSbtn.setEnabled(0)
           
           if self.wfs: self.ui.addWFSbtn.setEnabled(1)
           else: self.ui.addWFSbtn.setEnabled(0)
                      
           if self.wmts: self.ui.addWMTSbtn.setEnabled(1)
           else: self.ui.addWMTSbtn.setEnabled(0)
           
           if self.wcs: self.ui.addWCSbtn.setEnabled(1)
           else: self.ui.addWCSbtn.setEnabled(0)
           
           if self.dl: self.ui.DLbtn.setEnabled(1)
           else: self.ui.DLbtn.setEnabled(0)
        
    def onZoekClicked(self):
        self.zoek = self.ui.zoekTxt.currentText()
        self.search()  
      
    def modelFilterCbxIndexChanged(self):
        value = self.ui.modelFilterCbx.currentIndex()
        if value == 1:
           self.filterModel(1)
        elif value == 2:
           self.filterModel(5)
        elif value == 3:
           self.filterModel(2)
        elif value == 4:
           self.filterModel(6)
        elif value == 5:
           self.filterModel(7)
        else:
          self.filterModel()
          
    def filterModel(self, col=None):
        if col != None:
           self.proxyModel.setFilterKeyColumn(col)
           expr = QRegExp("?*", Qt.CaseInsensitive, QRegExp.Wildcard )
           self.proxyModel.setFilterRegExp(expr)
        else:
           self.proxyModel.setFilterRegExp(None)
        
    def search(self): 
        try:  
          QApplication.setOverrideCursor( QCursor(Qt.WaitCursor))
          if self.ui.filterBox.isChecked():
            orgName= self.ui.organisatiesCbx.currentText()
            dataTypes= [ n[1] for n in self.md.dataTypes if n[0] == self.ui.typeCbx.currentText()] 
            if dataTypes != []: dataType= dataTypes[0]
            else: dataType=''
            inspiretheme= self.ui.INSPIREthemaCbx.currentText()
            inspireannex= self.ui.INSPIREannexCbx.currentText()
            inspireServiceType= self.ui.INSPIREserviceCbx.currentText()
            searchResult = metadata.MDdata( self.md.searchAll(
              self.zoek, orgName, dataType, None, inspiretheme, inspireannex, inspireServiceType))
          else:
            searchResult = metadata.MDdata( self.md.searchAll( self.zoek ))
        except:
           self.bar.pushMessage("Error", str( sys.exc_info()[1]), level=Qgis.Critical , duration=3)
           return
        finally:
           QApplication.restoreOverrideCursor()
        
        self.ui.countLbl.setText( "Aantal gevonden: %s" % searchResult.count  )
        self.ui.descriptionText.setText('')
        self._setModel(searchResult.records)
        if searchResult.count == 0:
           self.bar.pushMessage(
             QCoreApplication.translate("datacatalog", "Waarschuwing "), 
             QCoreApplication.translate("datacatalog", 
                                     "Er zijn geen resultaten gevonden voor deze zoekopdracht"), duration=5)

    def openUrl(self, url):
        if url: webbrowser.open_new_tab( url.encode("utf-8") )

    def addWMS(self):
        if self.wms == None: return
      
        crs =  self.gh.getGetMapCrs(self.iface).authid()
        if crs != 'EPSG:28992' or  crs != 'EPSG:3857' or  crs != 'EPSG:3043':
           crs = 'EPSG:28992' 
        try:   
          lyrs =  metadata.getWmsLayerNames( self.wms, self.s.proxyUrl ) 
        except:
          self.bar.pushMessage( "Error", str(sys.exc_info()[1]), level=Qgis.Critical , duration=10)
          return 
        
        if len(lyrs) == 0:
            self.bar.pushMessage("WMS", 
            QCoreApplication.translate("datacatalog", 
                      "Kan geen lagen vinden in: %s" % self.wms ), level=Qgis.Warning, duration=10)
            return 
        elif len(lyrs) == 1:
            layerTitle = lyrs[0][1]
        else:
            layerTitle, accept = QInputDialog.getItem(self, "WMS toevoegen", 
                                              "Kies een laag om toe te voegen", [n[1] for n in lyrs], editable=0) 
            if not accept: return
        
        layerName = [n[0] for n in lyrs if n[1] == layerTitle ][0]
        style = [n[2] for n in lyrs if n[1] == layerTitle ][0]
        url= self.wms.split('?')[0]

        if crs != 'EPSG:28992' or  crs != 'EPSG:3857' : 
           crs = 'EPSG:28992' 
        wmsUrl = "url=%s&layers=%s&format=image/png&styles=%s&crs=%s" % (url, layerName, style , crs) 
        
        try:
            rlayer = QgsRasterLayer(wmsUrl, layerTitle, 'wms') 
            if rlayer.isValid():
               QgsProject.instance().addMapLayer(rlayer)
            else:  
                self.bar.pushMessage("Error", 
                QCoreApplication.translate("datacatalog", "Kan WMS niet laden"), 
                level=Qgis.Critical , duration=10) 
        except: 
            self.bar.pushMessage("Error", str(sys.exc_info()[1] ), level=Qgis.Critical , duration=10)
            return 
      
    def addWFS(self):    
        if self.wfs == None: return
      
        try:
            lyrs =  metadata.getWFSLayerNames( self.wfs, self.s.proxyUrl )
        except:
            self.bar.pushMessage( "Error", str(sys.exc_info()[1]), level=Qgis.Critical , duration=10)
            return 
        if len(lyrs) == 0:
            self.bar.pushMessage("WFS", QCoreApplication.translate("datacatalog", 
                      "Kan geen lagen vinden in: %s" % self.wfs ), level=Qgis.Warning, duration=10)
            return
        elif len(lyrs) == 1:
            layerTitle = lyrs[0][1]
        else:
            layerTitle, accept = QInputDialog.getItem(self, 
                 QCoreApplication.translate("datacatalog", "WFS toevoegen"), 
                 QCoreApplication.translate("datacatalog", "Kies een laag om toe te voegen"),
                 [n[1] for n in lyrs], editable=0) 
            if not accept: return
          
        layerName = [n[0] for n in lyrs if n[1] == layerTitle ][0]
        crs = [n[2] for n in lyrs if n[1] == layerTitle ][0]
        url =  self.wfs.split('?')[0]
                
        wfsUri = metadata.makeWFSuri( url, layerName, crs, bbox=None )
        try:
            vlayer = QgsVectorLayer( wfsUri, layerTitle , "WFS")
            QgsProject.instance().addMapLayer(vlayer)
        except: 
            self.bar.pushMessage("Error", str(sys.exc_info()[1] ), level=Qgis.Critical , duration=10)
            return 

    def addWMTS(self):
      if self.wmts == None: return
      try:
          lyrs =  metadata.getWMTSlayersNames( self.wmts, self.s.proxyUrl )
      except:
          self.bar.pushMessage("Error",'Kan niet connecteren met '+ self.wmts, level=Qgis.Critical , duration=10)
          return 
      if len(lyrs) == 0:
          self.bar.pushMessage("WMTS", 
          QCoreApplication.translate("datacatalog", 
                    "Kan geen lagen vinden in: %s" % self.wmts ), level=Qgis.Warning, duration=10)
          return
      elif len(lyrs) == 1:
          layerTitle = lyrs[0][1]
      else:
         layerTitle, accept = QInputDialog.getItem(self, "WMTS toevoegen", 
                                    "Kies een laag om toe te voegen", [n[1] for n in lyrs], editable=0) 
         if not accept: return
        
      layerName = [n[0] for n in lyrs if n[1] == layerTitle ][0]
      matrix = [n[2] for n in lyrs if n[1] == layerTitle ][0]
      frmt =  [n[3] for n in lyrs if n[1] == layerTitle ][0]
      srs = [n[4] for n in lyrs if n[1] == layerTitle ][0]
      
      wmtsUrl= metadata.makeWMTSuri(self.wmts , layerName, matrix, format=frmt, srsname=srs)

      rlayer = QgsRasterLayer(wmtsUrl, layerTitle, 'wms') 
      if rlayer.isValid():
         QgsProject.instance().addMapLayer(rlayer)
      else:  
         self.bar.pushMessage("Error", QCoreApplication.translate("datacatalog", "Kan WMS niet laden"), 
               level=Qgis.Critical , duration=10) 

    
    def addWCS(self):
      lyrs =  metadata.getWCSlayerNames( self.wcs, self.s.proxyUrl )
         
      if len(lyrs) == 0:
          self.bar.pushMessage("WCS", 
          QCoreApplication.translate("datacatalog", 
                    "Kan geen lagen vinden in: %s" % self.wcs ), level=Qgis.Warning, duration=10)
          return
      elif len(lyrs) == 1:
          layerTitle = lyrs[0][1]
      else:
          layerTitle, accept = QInputDialog.getItem(self, "WCS toevoegen", 
                              "Kies een laag om toe te voegen", [n[1] for n in lyrs], editable=0) 
          if not accept: return
        
      layerName = [n[0] for n in lyrs if n[1] == layerTitle ][0] 

      wcsUri = metadata.makeWCSuri(self.wcs, layerName )  #srsname=srs, invertAxis=axis

      QApplication.setOverrideCursor( QCursor(Qt.WaitCursor)) 
      rlayer = QgsRasterLayer( wcsUri, layerTitle , "wcs")

      if rlayer.isValid():
          QgsProject.instance().addMapLayer(rlayer)        
      else:  
          self.bar.pushMessage("Error", QCoreApplication.translate("datacatalog", "Kan WCS niet laden"), 
          level=Qgis.Critical , duration=10) 
      QApplication.restoreOverrideCursor()
            
    def clean(self):
        self.model.clear()
        self.wms = None
        self.wfs = None
        self.dl = None
        self.wmts = None
        self.wcs = None
        self.ui.zoekTxt.setCurrentIndex(0)
        self.ui.descriptionText.setText("")
        self.ui.countLbl.setText("")
        self.ui.msgLbl.setText("")
        self.ui.DLbtn.setEnabled(0)
        self.ui.addWFSbtn.setEnabled(0)
        self.ui.addWMTSbtn.setEnabled(0)
        self.ui.addWMSbtn.setEnabled(0)
        self.ui.addWCSbtn.setEnabled(0)
        self.ui.modelFilterCbx.setCurrentIndex(0)
        

