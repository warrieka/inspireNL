# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from ui_dataCatalog_dialog import Ui_dataCatalogDlg
from qgis.core import *
from qgis.gui import QgsMessageBar 
import os, json, webbrowser, sys, urllib2
import geometryhelper as gh
from settings import settings
import metadataParser as metadata

class dataCatalog(QtGui.QDialog):
    def __init__(self, iface):
        QtGui.QDialog.__init__(self, None)
        self.setWindowFlags( self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint )
        #self.setWindowFlags( self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.iface = iface
    
        # initialize locale
        locale = QtCore.QSettings().value("locale/userLocale", "nl")
        if not locale: locale == 'nl' 
        else: locale = locale[0:2]
        localePath = os.path.join(os.path.dirname(__file__), 'i18n', '{}.qm'.format(locale))
        if os.path.exists(localePath):
            self.translator = QtCore.QTranslator()
            self.translator.load(localePath)
            if QtCore.qVersion() > '4.3.3': QtCore.QCoreApplication.installTranslator(self.translator)
    
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
        self.bar.setSizePolicy( QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed )
        self.ui.verticalLayout.addWidget(self.bar)
        #vars
        self.firstShow = True
        self.wms = None
        self.wfs = None
        self.wmts = None
        self.wcs = None
        self.dl = None
        self.zoek = ''
        self.bronnen = None 
        #datamodel
        self.model = QtGui.QStandardItemModel(self)
        self.proxyModel = QtGui.QSortFilterProxyModel(self)
        self.proxyModel.setSourceModel(self.model)
        self.ui.resultView.setModel( self.proxyModel )
        #completer
        self.completer = QtGui.QCompleter( self )
        self.completerModel = QtGui.QStringListModel(self)
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
        self.ui.filterWgt.setHidden(1)
        self.finished.connect(self.clean)

    def _setModel(self, records):   
        self.model.clear()
         
        for rec in records:
            title = QtGui.QStandardItem( rec['title'] )            #0
            wms = QtGui.QStandardItem( rec['wms'][1] )             #1
            downloadLink = QtGui.QStandardItem(rec['download'])    #2
            id = QtGui.QStandardItem( rec['uuid'] )                #3
            abstract = QtGui.QStandardItem( rec['abstract'] )      #4
            wfs =     QtGui.QStandardItem( rec['wfs'][1] )         #5
            wcs =     QtGui.QStandardItem( rec['wcs'][1] )         #6
            wmts =    QtGui.QStandardItem( rec['wmts'][1] )        #7
            ### 
            wmsName = QtGui.QStandardItem( rec['wms'][0] )             #8
            wfsName =     QtGui.QStandardItem( rec['wfs'][0] )         #9
            wcsName =     QtGui.QStandardItem( rec['wcs'][0] )         #10
            wmtsName =    QtGui.QStandardItem( rec['wmts'][0] )        #11
            self.model.appendRow([title,wms,downloadLink,id,abstract,wfs,wcs,wmts,wmsName,wfsName,wcsName,wmtsName])

    #overwrite
    def show(self):
        QtGui.QDialog.show(self)
        self.setWindowModality(0)
        if self.firstShow:
             inet = internet_on( self.s.proxyUrl )
             if inet:
                self.ui.organisatiesCbx.addItems( ['']+ self.md.list_organisations() )
                keywords = sorted( self.md.list_suggestionKeyword() ) 
                self.completerModel.setStringList( keywords )
                self.bronnen = self.md.list_bronnen()
                self.ui.bronCbx.addItems( ['']+ [ n[1] for n in self.bronnen] )
                self.ui.typeCbx.addItems( ['']+  [ n[0] for n in self.md.dataTypes] )                
                
                self.ui.INSPIREannexCbx.addItems( ['']+ self.md.inspireannex )
                self.ui.INSPIREserviceCbx.addItems( ['']+ self.md.inspireServiceTypes )
                self.ui.INSPIREthemaCbx.addItems( ['']+ self.md.list_inspire_theme() )
                self.firstShow = False      
             else:
                self.bar.pushMessage(
                  QtCore.QCoreApplication.translate("datacatalog", "Waarschuwing "), 
                  QtCore.QCoreApplication.translate("datacatalog", 
                    "Kan geen verbing maken met het internet."), level=QgsMessageBar.WARNING, duration=3)
      
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
           expr = QtCore.QRegExp("?*", QtCore.Qt.CaseInsensitive, QtCore.QRegExp.Wildcard )
           self.proxyModel.setFilterRegExp(expr)
        else:
           self.proxyModel.setFilterRegExp(None)
        
    def search(self): 
        try:  
          QtGui.QApplication.setOverrideCursor( QtGui.QCursor(QtCore.Qt.WaitCursor))
          if self.ui.filterBox.isChecked():
            orgName= self.ui.organisatiesCbx.currentText()
            dataTypes= [ n[1] for n in self.md.dataTypes if n[0] == self.ui.typeCbx.currentText()] 
            if dataTypes != []: dataType= dataTypes[0]
            else: dataType=''
            siteIds = [ n[0] for n in self.bronnen if n[1] == self.ui.bronCbx.currentText() ]
            if siteIds != []: siteId= siteIds[0]
            else: siteId =''
            inspiretheme= self.ui.INSPIREthemaCbx.currentText()
            inspireannex= self.ui.INSPIREannexCbx.currentText()
            inspireServiceType= self.ui.INSPIREserviceCbx.currentText()
            searchResult = metadata.MDdata( self.md.searchAll(
              self.zoek, orgName, dataType, siteId, inspiretheme, inspireannex, inspireServiceType))
          else:
            searchResult = metadata.MDdata( self.md.searchAll( self.zoek ))
        except:
           self.bar.pushMessage("Error", str( sys.exc_info()[1]), level=QgsMessageBar.CRITICAL, duration=3)
           return
        finally:
           QtGui.QApplication.restoreOverrideCursor()
        
        self.ui.countLbl.setText( "Aantal gevonden: %s" % searchResult.count  )
        self.ui.descriptionText.setText('')
        self._setModel(searchResult.records)
        if searchResult.count == 0:
           self.bar.pushMessage(
             QtCore.QCoreApplication.translate("datacatalog", "Waarschuwing "), 
             QtCore.QCoreApplication.translate("datacatalog", 
                                               "Er werden geen resultaten gevonde voor deze zoekopdracht"), duration=5)

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
          self.bar.pushMessage( "Error", str( sys.exc_info()[1]), level=QgsMessageBar.CRITICAL, duration=10)
          return 
        
        if len(lyrs) == 0:
            self.bar.pushMessage("WMS", 
            QtCore.QCoreApplication.translate("datacatalog", 
                      "Kan geen lagen vinden in: %s" % self.wms ), level=QgsMessageBar.WARNING, duration=10)
            return 
        elif len(lyrs) == 1:
            layerTitle = lyrs[0][1]
        else:
            layerTitle, accept = QtGui.QInputDialog.getItem(self, "WMS toevoegen", 
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
               QgsMapLayerRegistry.instance().addMapLayer(rlayer)
            else:  
                self.bar.pushMessage("Error", 
                QtCore.QCoreApplication.translate("datacatalog", "Kan WMS niet laden"), 
                level=QgsMessageBar.CRITICAL, duration=10) 
        except: 
            self.bar.pushMessage("Error", str( sys.exc_info()[1] ), level=QgsMessageBar.CRITICAL, duration=10)
            return 
      
    def addWFS(self):    
        if self.wfs == None: return
      
        try:
            lyrs =  metadata.getWFSLayerNames( self.wfs, self.s.proxyUrl )
        except:
            self.bar.pushMessage( "Error", str( sys.exc_info()[1]), level=QgsMessageBar.CRITICAL, duration=10)
            return 
        if len(lyrs) == 0:
            self.bar.pushMessage("WFS", 
            QtCore.QCoreApplication.translate("datacatalog", 
                      "Kan geen lagen vinden in: %s" % self.wfs ), level=QgsMessageBar.WARNING, duration=10)
            return
        elif len(lyrs) == 1:
            layerTitle = lyrs[0][1]
        else:
            layerTitle, accept = QtGui.QInputDialog.getItem(self, "WFS toevoegen", 
                                "Kies een laag om toe te voegen", [n[1] for n in lyrs], editable=0) 
            if not accept: return
          
        layerName = [n[0] for n in lyrs if n[1] == layerTitle ][0]
        crs = [n[2] for n in lyrs if n[1] == layerTitle ][0]
        url =  self.wfs.split('?')[0]
                
        if self.ui.wfsBboxchk.isChecked():
            extent = self.iface.mapCanvas().extent()
            minX, minY = self.gh.prjPtFromMapCrs([extent.xMinimum(),extent.yMinimum()], int(crs.split(":")[-1]) )
            maxX, maxY = self.gh.prjPtFromMapCrs([extent.xMaximum(),extent.yMaximum()], int(crs.split(":")[-1]) )
            bbox = [minX, minY, maxX, maxY]
        else:
            bbox = None
        
        wfsUri = metadata.makeWFSuri( url, layerName, crs, bbox=bbox )
        try:
            vlayer = QgsVectorLayer( wfsUri, layerTitle , "WFS")
            QgsMapLayerRegistry.instance().addMapLayer(vlayer)
        except: 
            self.bar.pushMessage("Error", str( sys.exc_info()[1] ), level=QgsMessageBar.CRITICAL, duration=10)
            return 

    def addWMTS(self):
      if self.wmts == None: return
      try:
          lyrs =  metadata.getWMTSlayersNames( self.wmts, self.s.proxyUrl )
      except:
          self.bar.pushMessage("Error",'Kan niet connecteren met '+ self.wmts, level=QgsMessageBar.CRITICAL, duration=10)
          return 
      if len(lyrs) == 0:
          self.bar.pushMessage("WMTS", 
          QtCore.QCoreApplication.translate("datacatalog", 
                    "Kan geen lagen vinden in: %s" % self.wmts ), level=QgsMessageBar.WARNING, duration=10)
          return
      elif len(lyrs) == 1:
          layerTitle = lyrs[0][1]
      else:
         layerTitle, accept = QtGui.QInputDialog.getItem(self, "WMTS toevoegen", 
                                         "Kies een laag om toe te voegen", [n[1] for n in lyrs], editable=0) 
         if not accept: return
        
      layerName = [n[0] for n in lyrs if n[1] == layerTitle ][0]
      matrix = [n[2] for n in lyrs if n[1] == layerTitle ][0]
      frmt =  [n[3] for n in lyrs if n[1] == layerTitle ][0]
      srs = [n[4] for n in lyrs if n[1] == layerTitle ][0]
      
      wmtsUrl= metadata.makeWMTSuri(self.wmts , layerName, matrix, format=frmt, srsname=srs)
  
      try:
          rlayer = QgsRasterLayer(wmtsUrl, layerTitle, 'wms') 
          if rlayer.isValid():
              QgsMapLayerRegistry.instance().addMapLayer(rlayer)
          else:  
              self.bar.pushMessage("Error", 
              QtCore.QCoreApplication.translate("datacatalog", "Kan WMS niet laden"), 
              level=QgsMessageBar.CRITICAL, duration=10) 
      except: 
          self.bar.pushMessage("Error", str( sys.exc_info()[1] ), level=QgsMessageBar.CRITICAL, duration=10)
          return 
    
    def addWCS(self):
      try:
          QtGui.QApplication.setOverrideCursor( QtGui.QCursor(QtCore.Qt.WaitCursor))
          lyrs =  metadata.getWCSlayerNames( self.wcs, self.s.proxyUrl )
      except:
          self.bar.pushMessage( "Error", str( sys.exc_info()[1]), level=QgsMessageBar.CRITICAL, duration=10)
          return 
      finally:
           QtGui.QApplication.restoreOverrideCursor()
           
      if len(lyrs) == 0:
          self.bar.pushMessage("WCS", 
          QtCore.QCoreApplication.translate("datacatalog", 
                    "Kan geen lagen vinden in: %s" % self.wcs ), level=QgsMessageBar.WARNING, duration=10)
          return
      elif len(lyrs) == 1:
          layerTitle = lyrs[0][1]
      else:
          layerTitle, accept = QtGui.QInputDialog.getItem(self, "WCS toevoegen", 
                              "Kies een laag om toe te voegen", [n[1] for n in lyrs], editable=0) 
          if not accept: return
        
      layerName = [n[0] for n in lyrs if n[1] == layerTitle ][0] 
      layerFormat  = [n[2] for n in lyrs if n[1] == layerTitle ][0] 
      wcsUri = metadata.makeWCSuri( self.wcs, layerName, format=layerFormat )
      try:
          rlayer = QgsRasterLayer( wcsUri, layerTitle , "wcs")
          if rlayer.isValid():
              QgsMapLayerRegistry.instance().addMapLayer(rlayer)
          else:  
              self.bar.pushMessage("Error", 
              QtCore.QCoreApplication.translate("datacatalog", "Kan WCS niet laden"), 
              level=QgsMessageBar.CRITICAL, duration=10) 
      except: 
          self.bar.pushMessage("Error", str( sys.exc_info()[1] ), level=QgsMessageBar.CRITICAL, duration=10)
          return       
            
    def clean(self):
        self.model.clear()
        self.wms = None
        self.wfs = None
        self.dl = None
        self.wmts = None
        self.wcs = None
        self.ui.zoekTxt.setCurrentIndex(0)
        self.ui.descriptionText.setText('')
        self.ui.countLbl.setText( "")
        self.ui.msgLbl.setText("" )
        self.ui.DLbtn.setEnabled(0)
        self.ui.addWFSbtn.setEnabled(0)
        self.ui.addWMTSbtn.setEnabled(0)
        self.ui.modelFilterCbx.setCurrentIndex(0)
        
def internet_on(proxyUrl=None):
    try:
        if proxyUrl:
          proxy = urllib2.ProxyHandler({'http': proxyUrl})
          auth = urllib2.HTTPBasicAuthHandler()
          opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
          responseWFS = opener.open("https://www.google.be/", timeout=5)
        else: 
          responseWFS =  urllib2.urlopen("https://www.google.be/", timeout=5)
        return True
    except urllib2.URLError as err: pass
    return False
