# -*- coding: utf-8 -*-
from qgis.PyQt.QtCore import Qt, QSettings, QTranslator, QCoreApplication,  QSortFilterProxyModel, QRegExp, QStringListModel
from qgis.PyQt.QtGui import QCursor, QStandardItemModel, QStandardItem
from qgis.PyQt.QtWidgets import QApplication, QDialog, QSizePolicy, QCompleter, QInputDialog, QMessageBox, QFileDialog
from .ui_dataCatalog_dialog import Ui_dataCatalogDlg
from qgis.core import QgsProject, QgsVectorLayer, QgsRasterLayer, Qgis, QgsWkbTypes 
from qgis.gui import QgsMessageBar
from . import geometryhelper as gh
from .settings import settings
from . import metadataParser as metadata
from .metadataParser import MDReader, MDdata, getWmsLayerNames, getWFSLayerNames, makeWFSuri, getWMTSlayersNames, makeWMTSuri,  getWCSlayerNames, makeWCSuri
import sys, os, webbrowser, json

class dataCatalog(QDialog):
    """The dialog for the catalog searchwindow

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
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
    
        self.initGui()

    def initGui(self):
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
        self.ui.resultView.setModel(self.proxyModel )
        
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
        self.ui.DLbtn.clicked.connect(self.dlClicked)
        self.ui.resultView.clicked.connect(self.resultViewClicked)
        self.ui.modelFilterCbx.currentIndexChanged.connect(self.modelFilterCbxIndexChanged)
        self.finished.connect(self.clean)

    def setModel(self, records): 
        """set the model of the seachresult with records (metadata.MDdata)"""
        self.model.clear()
        reclist = sorted(records, key=lambda k: k['title']) 
         
        for rec in reclist:
            title = QStandardItem( rec['title'] )             #0
            wms = QStandardItem( rec['wms'][1] )              #1
            dl = json.dumps( rec['download'] ) if len(rec['download']) else None
            downloadLinks = QStandardItem(dl)                 #2
            
            id =       QStandardItem( rec['uuid'] )           #3
            abstract = QStandardItem( rec['abstract'] )       #4
            wfs =      QStandardItem( rec['wfs'][1] )         #5
            wcs =      QStandardItem( rec['wcs'][1] )         #6
            wmts =     QStandardItem( rec['wmts'][1] )        #7
            ### 
            wmsName =  QStandardItem( rec['wms'][0] )         #8
            wfsName =  QStandardItem( rec['wfs'][0] )         #9
            wcsName =  QStandardItem( rec['wcs'][0] )         #10
            wmtsName = QStandardItem( rec['wmts'][0] )        #11
            self.model.appendRow([title,wms,downloadLinks,id,abstract,wfs,wcs,wmts,wmsName,wfsName,wcsName,wmtsName])

    #overwrite
    def show(self):
        """Overwrite of QDialog.show"""
        QDialog.show(self)
        self.setWindowModality(0)
        if self.firstShow:
            self.ui.organisatiesCbx.addItems( ['']+ self.md.list_organisations() )
            keywords = sorted( self.md.list_suggestionKeyword() ) 
            self.completerModel.setStringList( keywords )
            #self.bronnen = self.md.list_bronnen()
            self.ui.typeCbx.addItems( ['']+  [ n[0] for n in self.md.dataTypes] )                
            
            #self.ui.INSPIREannexCbx.addItems( ['']+ self.md.inspireannex )
            self.ui.INSPIREserviceCbx.addItems( ['']+ self.md.inspireServiceTypes )
            self.ui.INSPIREthemaCbx.addItems( ['']+ self.md.list_inspire_theme() )
            self.firstShow = False      
      
    #eventhandlers
    def resultViewClicked(self):
        """Called when user clicked resultView"""
        if self.ui.resultView.selectedIndexes(): 
           row = self.ui.resultView.selectedIndexes()[0].row()  
           
           self.wms = self.proxyModel.data( self.proxyModel.index( row, 1) )
           dl  = self.proxyModel.data( self.proxyModel.index(row, 2) )
           self.dl = json.loads(dl) if dl else None

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
        """Called when user clicked zoekBtn"""  
        self.zoek = self.ui.zoekTxt.currentText()
        self.search()  
      
    def modelFilterCbxIndexChanged(self):
        """Called when user changes the ModelFilterCbx """
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
        """Filter model with col from modelFilter""" 
        if col != None:
           self.proxyModel.setFilterKeyColumn(col)
           expr = QRegExp("?*", Qt.CaseInsensitive, QRegExp.Wildcard )
           self.proxyModel.setFilterRegExp(expr)
        else:
           self.proxyModel.setFilterRegExp(None)
        
    def search(self): 
        """start the search"""
        QApplication.setOverrideCursor(Qt.WaitCursor)
        if self.ui.filterBox.isChecked():
            orgName= self.ui.organisatiesCbx.currentText()
            dataTypes= [ n[1] for n in self.md.dataTypes if n[0] == self.ui.typeCbx.currentText()] 
            if dataTypes != []: dataType= dataTypes[0]
            else: dataType=''
            inspiretheme= self.ui.INSPIREthemaCbx.currentText()
            inspireServiceType= self.ui.INSPIREserviceCbx.currentText()
            searchResult = metadata.MDdata( 
                self.md.searchAll( self.zoek, orgName, dataType, inspiretheme, inspireServiceType),  proxyUrl=self.s.proxyUrl)
        else:
            searchResult = metadata.MDdata( self.md.searchAll( self.zoek ), proxyUrl=self.s.proxyUrl )
        QApplication.restoreOverrideCursor()
        
        self.ui.countLbl.setText( "Aantal gevonden: %s" % searchResult.count  )
        self.ui.descriptionText.setText('')
        self.setModel(searchResult.records)
        if searchResult.count == 0:
           self.bar.pushMessage( QCoreApplication.translate("datacatalog", "Waarschuwing "), 
             QCoreApplication.translate("datacatalog", "Er zijn geen resultaten gevonden voor deze zoekopdracht"), duration=10)

    def openUrl(self, url):
        """Open url in browserwindow """
        if url: webbrowser.open_new_tab( url )

    def addWMS(self):
        """Add WMS from current record to map"""
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
            self.bar.pushMessage("WMS", QCoreApplication.translate("datacatalog",
            "Kan geen lagen vinden in: %s" % self.wms + "?service=WMS&request=Getcapabilities&version=1.3.0" ), level=Qgis.Warning, duration=10)
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
                self.bar.pushMessage("Error", QCoreApplication.translate("datacatalog", "Kan WMS niet laden"), 
                                    level=Qgis.Critical , duration=10) 
        except: 
            self.bar.pushMessage("Error", str(sys.exc_info()[1] ), level=Qgis.Critical , duration=10)
            return 
      
    def addWFS(self):    
        """Add WFS from current record to map"""
        if self.wfs == None: return

        wfsinfo = metadata.getWFSLayerNames( self.wfs, self.s.proxyUrl )
        lyrs =  wfsinfo['layerNames']
        wfsVersion = wfsinfo['version']
        
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
        IsComplex = [n[3] for n in lyrs if n[1] == layerTitle ][0]
        url =  self.wfs.split('?')[0]
           
        if self.ui.dlGMLchk.isChecked():
           self.dlWFS(url, layerName, crs, wfsVersion) 
           return
           
        if IsComplex:
            if self.complexWFS():
                self.dlWFS(url, layerName, crs, wfsVersion)
            return
        else: 
            wfsUri = metadata.makeWFSuri(url, layerName, crs, wfsVersion )
            vlayer = QgsVectorLayer( wfsUri, layerTitle , "WFS")            
            QgsProject.instance().addMapLayer(vlayer)


    def complexWFS(self):
       """Warning messagebox to be called when working WFS with complex features, 
       User will be asked if (s)he wants to try load te service with download instead.
       
       :return: True if user wants to download else false.
       """
       msg = """
       Deze laag kon niet correct ingeladen worden als WFS-laag, het vermoedelijk gaat om een service met complexe features.<br/>
       U kunt de laag downloaden voor het huidge kaartbeeld als GML. Mogelijk worden ook dan niet alle gegeven correct waergegeven. 
       
       <br/><br/>U kunt eventueel de plugin 
       <a href='https://plugins.qgis.org/plugins/gml_application_schema_toolbox'>GML Application Schema Toolbox</a>
       installeren een WFS die complexe features correcter te raadplegen." 
       Na installatie, vindt u deze tool op de menubalk onder: <strong>Plugins > QGIS GML Application Schema Toolbox > Wizard</strong>
        
       <br/><br/> Wilt u in de plaats proberen deze laag te downloaden vor het huidge kaartbeeld en in te laden? 
       """
       
       buttonDlg = QMessageBox.warning(self.iface.mainWindow(), "Kan features niet correct lezen.", 
            QCoreApplication.translate("datacatalog", msg),  QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)  
       if buttonDlg == QMessageBox.Yes:  
           return True
       else:
           return False 
       
    def dlWFS(self, url,  layerName="", crs="EPSG:4326", wfsVersion="2.0.0"):
        """Download a WFS as a GML-file for current extend. 
        The user wil be asked to chose filename and location. 
        
       :param url: the url of the wfs
       :param iserror: true/false, has an error been called?
       :param wfsVersion: 2.0.0 or 1.1.0
       :param layerName: the typeName of the layer in  the WFS
        """
        title = "Opslaan als GML voor huidig kaartbeeld"
        fileName, _ = QFileDialog.getSaveFileName(self.iface.mainWindow(), title, None ,"GML (*.gml)")

        if not fileName: return
    
        e = self.iface.mapCanvas().extent()
        
        #find numerice part in crs
        crsNumS = "".join([s for s in crs if s.isdigit() ])
        if crsNumS == "":
            crsNum= 4326
            crs="EPSG:4326"
        else:
            crsNum = int(crsNumS)
        
        eMin = self.gh.prjPtFromMapCrs( [e.xMinimum(), e.yMinimum()], crsNum)
        eMax = self.gh.prjPtFromMapCrs( [e.xMaximum(), e.yMaximum()], crsNum)
        
        bbox = [ eMin.x(), eMin.y(), eMax.x(), eMax.y() ]
        metadata.downloadWFS(url, layerName, fileName, crs, 50000, wfsVersion, bbox, self.s.proxyUrl, 120)
        layer = self.iface.addVectorLayer(fileName , layerName, "ogr")
             

    def addWMTS(self):
      """Add WMTS from current record to map"""
      if self.wmts == None: return
      try:
          lyrs =  metadata.getWMTSlayersNames( self.wmts, self.s.proxyUrl )
      except:
          self.bar.pushMessage("Error",'Kan niet connecteren met '+ self.wmts, level=Qgis.Critical , duration=10)
          return 
      if len(lyrs) == 0:
          self.bar.pushMessage("WMTS", 
          QCoreApplication.translate("datacatalog", "Kan geen lagen vinden in: %s" % self.wmts ), level=Qgis.Warning, duration=10)
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
      """Add WCS from current record to map"""
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
            
    def dlClicked(self):
        """Called when user clicked downloadBtn, initiate download of current record"""
        if not self.dl or len(self.dl) == 0: 
            return
        
        if len(self.dl) == 1:
            self.openUrl( self.dl[0][1] )
            return
        
        layerTitle, accept = QInputDialog.getItem(self, "Laag downloaden", 
                              "Kies een download", [n[0] for n in self.dl], editable=0)
        if not accept: 
            return
    
        dlName = [n[1] for n in self.dl if n[0] == layerTitle ][0]
        self.openUrl( dlName )
  
    def clean(self):
        """Reset the UI to initial positions"""
        self.model.clear()
        self.wms = None
        self.wfs = None
        self.dl = None
        self.wmts = None
        self.wcs = None
        self.ui.zoekTxt.setCurrentIndex(0)
        self.ui.descriptionText.setText("")
        self.ui.countLbl.setText("")
        self.ui.DLbtn.setEnabled(0)
        self.ui.addWFSbtn.setEnabled(0)
        self.ui.addWMTSbtn.setEnabled(0)
        self.ui.addWMSbtn.setEnabled(0)
        self.ui.addWCSbtn.setEnabled(0)
        self.ui.INSPIREthemaCbx.setCurrentIndex(0)
        self.ui.organisatiesCbx.setCurrentIndex(0)
        self.ui.typeCbx.setCurrentIndex(0)
        self.ui.INSPIREserviceCbx.setCurrentIndex(0)
        self.ui.modelFilterCbx.setCurrentIndex(0)
        

