# -*- coding: utf-8 -*-
from future import standard_library
standard_library.install_aliases()
import urllib.request, urllib.error, urllib.parse, json, sys, os.path, datetime
import xml.etree.ElementTree as ET

class MDdata(object):
    def __init__(self, metadataXML): 
        self.start = int( metadataXML.attrib["from"] )
        self.to =    int( metadataXML.attrib["to"] )
        self.count = int( metadataXML[0].attrib["count"] )
        self.records = []
        
        mds = metadataXML.findall("metadata")
        for md in mds:
           record = {}
                      
           geonet =  md.find('{http://www.fao.org/geonetwork}info')
           if geonet.find('uuid').text != None: 
              record['uuid'] = geonet.find('uuid').text
           else: 
              continue  #records with no id are just wrong
              
           if (md.find('title') != None) and (md.find('title').text != None):
              record['title'] = md.find('title').text
           else: 
              record['title'] = ''
             
           if (md.find('abstract') != None) and (md.find('abstract').text != None):
              record['abstract'] = md.find('abstract').text
           else: 
              record['abstract'] = ''
           
           if (md.find('geoBox') != None) and (md.find('geoBox').text != None): 
               try:
                   record['geoBox'] = [float(i) for i in md.find('geoBox').text.split('|') ]
               except:
                   record['geoBox'] = ""
           else: 
              record['geoBox'] = ""
           
           record['wms'] = self._findWMS( md )
           record['wfs'] = self._findWFS( md )
           record['wcs'] = self._findWCS( md )
           record['wmts'] = self._findWMTS( md )
           record['download'] = self._findDownload( md )
           
           self.records.append(record)
           
    def _findWFS(self , node ):
        links =  "|".join( [ n.text for n in node.findall("link") ] )
        links = links.split('|') 
        for n in range(1, len( links )):
            if "OGC:WFS" in links[n].upper(): 
              if "http" in  links[n - 1]:
                  return ( links[n - 2], links[n - 1])
        return ("","")
      
    def _findWMS(self , node ):
        links =  "|".join( [ n.text for n in node.findall("link") ] )
        links = links.split('|') 
        for n in range(2, len( links )):
            if "OGC:WMS" in links[n].upper(): 
              if "http" in  links[n - 1]: 
                  return ( links[n - 2], links[n - 1])
        return ("","")
      
    def _findWMTS(self , node ):
        links =  "|".join( [ n.text for n in node.findall("link") ] )
        links = links.split('|') 
        for n in range(2, len( links )):
            if "OGC:WMTS" in links[n].upper(): 
              if "http" in  links[n - 1]: 
                return ( links[n - 2], links[n - 1])
        return ("","")

    def _findWCS(self , node ):
        links =  "|".join( [ n.text for n in node.findall("link") ] )
        links = links.split('|') 
        for n in range(2, len( links )):
            if "OGC:WCS" in links[n].upper(): 
              if "http" in  links[n - 1]: #some wms are stored with relative path's, ignore those
                return ( links[n - 2], links[n - 1])
        return ("","")

    def _findDownload(self , node):
        links =  "|".join( [ n.text for n in node.findall("link") ] )
        links = links.split('|') 
        for n in range(2, len( links )):
            if "DOWNLOAD" in links[n].upper(): 
               if "http" in  links[n - 1]: #some files are stored with relative path's, ignore those
                  return links[n - 1]
        return ""


class MDReader(object):
    def __init__(self, proxyUrl=None, timeout=15 ):
        self.timeout = timeout
        self.geoNetworkUrl = "http://www.nationaalgeoregister.nl/geonetwork/srv/dut/" 

        self.dataTypes = [["Dataset", "dataset"],["Datasetserie","series"],
                          ["Objectencatalogus","model"],["Service","service"]]
        self.inspireServiceTypes =  ["Discovery","Transformation","View", "Download","Other","Invoke"]
        self.inspireannex =  ["i","ii","iii"]
        
        self.opener = None
        if proxyUrl:
             proxy = urllib.request.ProxyHandler({'http': proxyUrl})
             auth = urllib.request.HTTPBasicAuthHandler()
             self.opener = urllib.request.build_opener(proxy, auth, urllib.request.HTTPHandler)
        
    def _createFindUrl(self, q="", start=1, to=20, orgName='', dataType='', siteId='',
                       inspiretheme='', inspireannex='', inspireServiceType='', keyword=""):
        geopuntUrl = self.geoNetworkUrl + "/q?fast=index&"
        data = {}
        data["category"] = "inspire"   #REMARK: NL specifik
        data["any"] = "*" + q + "*"
        data["to"] = to
        data["from"] = start
        data["orgName"] =   orgName 
        data["keyword"] =   keyword 
                
        if dataType: data['type']= dataType
        if siteId: data['siteId']= siteId                
                
        if inspiretheme: 
            data["inspiretheme"] = inspiretheme            
        if inspireannex and (inspireannex.lower() in self.inspireannex ) : 
            data["inspireannex"] = inspireannex.lower()
        if inspireServiceType : 
            data["serviceType"] = inspireServiceType.lower() 

        values = urllib.parse.urlencode(data)
        result = geopuntUrl + values
        return result
          
    def list_inspire_theme(self, q=''):
        url = self.geoNetworkUrl + "/xml.search.keywords?pNewSearch=true&pTypeSearch=1&pThesauri=external.theme.inspire-theme&pKeyword=*" + q +"*"
        try:
            if self.opener: response = self.opener.open(url, timeout=self.timeout)
            else: response = urllib.request.urlopen(url, timeout=self.timeout)
        except  (urllib.error.HTTPError, urllib.error.URLError) as e:
            raise metaError( str( e.reason ))
        except:
            raise metaError( str( sys.exc_info()[1] ))
        else:
            result = ET.parse(response)
            r= result.getroot()
            themes = [ n.find("value").text for n in  r[0].findall('keyword') ]
            themes.sort()
            return themes
    
    def list_suggestionKeyword(self, q=''):
        url = self.geoNetworkUrl + "/main.search.suggest?field=keyword"
        if q:
            url= url + "&q=" + q
        
        try:
            if self.opener: response = self.opener.open(url, timeout=self.timeout)
            else: response = urllib.request.urlopen(url, timeout=self.timeout)
        except  (urllib.error.HTTPError, urllib.error.URLError) as e:
            raise metaError( str( e.reason ))
        except:
            raise metaError( str( sys.exc_info()[1] ))
        else:
            result = json.load(response)
            return result[1]

    def list_organisations(self):
        url = self.geoNetworkUrl + 'q?fast=index&from=1&to=1&category=inspire&any_OR_geokeyword_OR_title_OR_keyword=&relation=within'

        try:
            if self.opener: response = self.opener.open(url, timeout=self.timeout)
            else: response = urllib.request.urlopen(url, timeout=self.timeout)
        except  (urllib.error.HTTPError, urllib.error.URLError) as e:
            raise metaError( str( e.reason ))
        except:
            raise metaError( str( sys.exc_info()[1] ))
        else:
            result = ET.parse(response)
            r = result.getroot()
            organisations = [n.attrib['name'] for n in  r.findall('./summary/orgNames/orgName')]
            organisations.sort()
            return organisations
            
    def list_bronnen(self):
        url = self.geoNetworkUrl + "/xml.info?type=sources"
        try:
            if self.opener: response = self.opener.open(url, timeout=self.timeout)
            else: response = urllib.request.urlopen(url, timeout=self.timeout)
        except  (urllib.error.HTTPError, urllib.error.URLError) as e:
            raise metaError( str( e.reason ))
        except:
            raise metaError( str( sys.exc_info()[1] ))
        else:
            result = ET.parse(response)
            r= result.getroot()
            bronnen = [ ( n.find("uuid").text, n.find("name").text ) 
                     for n in  r[0].findall('source') ]
            bronnen.sort()
            return bronnen

    def search(self, q="", start=1, to=20, orgName='', dataType='', siteId='', inspiretheme='', inspireannex='', inspireServiceType='', keyword='' ):
        url = self._createFindUrl( q, start, to,  orgName, dataType, siteId, inspiretheme, inspireannex, inspireServiceType, keyword)
        try:
            if self.opener: response = self.opener.open(url, timeout=self.timeout)
            else: response = urllib.request.urlopen(url, timeout=self.timeout)
        except  (urllib.error.HTTPError, urllib.error.URLError) as e:
            raise metaError( str( e.reason ) +' on '+ url )
        except:
            raise metaError( str( sys.exc_info()[1] ))
        else:
            result = ET.parse(response)
            resultXML = result.getroot()
            return  resultXML

    def searchAll(self, q="", orgName='', dataType='', siteId='', inspiretheme='', inspireannex='', inspireServiceType='', keyword=''):
        start= 1
        step= 1000
        searchResult = self.search(q, start, step, orgName, dataType, siteId, inspiretheme, inspireannex, inspireServiceType, keyword)
        count = int( searchResult[0].attrib["count"] )
        start += step
        while (start) <= count:  
           result = self.search(q, start, (start + step -1), orgName, dataType, siteId, inspiretheme, inspireannex, inspireServiceType)
           mds= result.findall("metadata")
           for md in mds: searchResult.append( md )
           start += step
        return searchResult


class metaError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)
   
def getWmsLayerNames( url, proxyUrl=''):
    if (not "request=getcapabilities" in url.lower()) or (not "service=wms" in url.lower()):
        capability = url.split("?")[0] + "?request=GetCapabilities&version=1.3.0&service=wms"
    else: 
        capability = url
        
    if proxyUrl:
        proxy = urllib.request.ProxyHandler({'http': proxyUrl})
        auth = urllib.request.HTTPBasicAuthHandler()
        opener = urllib.request.build_opener(proxy, auth, urllib.request.HTTPHandler)
        responseWMS =  opener.open(capability)
    else:
        responseWMS =  urllib.request.urlopen(capability)
    
    result = ET.parse(responseWMS)
    layers =  result.findall( ".//{http://www.opengis.net/wms}Layer" )
    layerNames=[]

    for lyr in layers:
        name= lyr.find("{http://www.opengis.net/wms}Name")
        title = lyr.find("{http://www.opengis.net/wms}Title")
        style = lyr.find("{http://www.opengis.net/wms}Style/{http://www.opengis.net/wms}Name")
        if ( name != None) and ( title != None ):
            if style == None: layerNames.append(( name.text, title.text, ''))
            else: layerNames.append(( name.text, title.text, style.text))

    return layerNames

def getWFSLayerNames( url, proxyUrl='' ):
    if (not "request=getcapabilities" in url.lower()) or (not "service=wfs" in url.lower()):
        capability = url.split("?")[0] + "?request=GetCapabilities&version=1.0.0&service=wfs"
    else: 
        capability = url
    if proxyUrl:
        proxy = urllib.request.ProxyHandler({'http': proxyUrl})
        auth = urllib.request.HTTPBasicAuthHandler()
        opener = urllib.request.build_opener(proxy, auth, urllib.request.HTTPHandler)
        responseWFS =  opener.open(capability)
    else:
        responseWFS =  urllib.request.urlopen(capability)
    
    result = ET.parse(responseWFS).getroot()
    
    serv = result.find(
         "{http://www.opengis.net/ows/1.1}ServiceIdentification/{http://www.opengis.net/ows/1.1}ServiceTypeVersion")
    if serv != None :
       raise Exception("Deze WFS is versie %s, QGIS ondersteunt alleen versie 1.0.0, eventueel kunt u de WFS 2.0 plugin gebruiken." % serv.text)
    serv = result.find(
         "{http://www.opengis.net/ows}ServiceIdentification/{http://www.opengis.net/ows}ServiceTypeVersion")
    if serv != None :
       raise Exception("Deze WFS is versie %s, QGIS ondersteunt alleen versie 1.0.0, eventueel kunt u de WFS 2.0 plugin gebruiken." % serv.text) 

    layers =  result.findall( ".//{http://www.opengis.net/wfs}FeatureType" )
    layerNames=[]

    for lyr in layers:
        name= lyr.find("{http://www.opengis.net/wfs}Name")
        title = lyr.find("{http://www.opengis.net/wfs}Title")
        srs = lyr.find("{http://www.opengis.net/wfs}SRS")
        if ( name != None) and ( title != None ):
            if srs == None: layerNames.append(( name.text, title.text, 'EPSG:28992'))
            else: layerNames.append(( name.text, title.text, srs.text))

    return layerNames

def getWMTSlayersNames( url, proxyUrl='' ):
    if (not "request=getcapabilities" in url.lower()) or (not "service=wmts" in url.lower()):
        capability = url.split("?")[0] + "?service=WMTS&request=Getcapabilities&version="
    else: 
        capability = url
    if proxyUrl:
        proxy = urllib.request.ProxyHandler({'http': proxyUrl})
        auth = urllib.request.HTTPBasicAuthHandler()
        opener = urllib.request.build_opener(proxy, auth, urllib.request.HTTPHandler)
        responseWMTS =  opener.open(capability)
    else:
        responseWMTS =  urllib.request.urlopen(capability)
        
    result = ET.parse(responseWMTS).getroot()
    content = result.find( "{http://www.opengis.net/wmts/1.0}Contents" )
    layers =  content.findall( "{http://www.opengis.net/wmts/1.0}Layer" )
    layerNames = []
    
    matrixSets = content.findall("{http://www.opengis.net/wmts/1.0}TileMatrixSet")

    for lyr in layers:
        name= lyr.find("{http://www.opengis.net/ows/1.1}Identifier")
        title = lyr.find("{http://www.opengis.net/ows/1.1}Title")
        matrix = lyr.find("{http://www.opengis.net/wmts/1.0}TileMatrixSetLink/{http://www.opengis.net/wmts/1.0}TileMatrixSet")
        format = lyr.find("{http://www.opengis.net/wmts/1.0}Format")
        
        srsList = [ n.find("{http://www.opengis.net/ows/1.1}SupportedCRS").text
                    for n in matrixSets if n.find("{http://www.opengis.net/ows/1.1}Identifier").text == matrix.text]

        if srsList: srs =  "EPSG:"+ srsList[0].split(':')[-1]
        else: srs = "" 
        
        if ( name != None) and ( title != None ) and ( matrix != None ) and ( format != None ):
              layerNames.append(( name.text, title.text, matrix.text, format.text, srs ))

    return layerNames

def getWCSlayerNames( url, proxyUrl='', wcs_version="1.1" ):    
    capability = url.split("?")[0] + "?request=GetCapabilities&version=%s.0&service=WCS" % wcs_version

    if proxyUrl:
       proxy = urllib.request.ProxyHandler({'http': proxyUrl})
       auth = urllib.request.HTTPBasicAuthHandler()
       opener = urllib.request.build_opener(proxy, auth, urllib.request.HTTPHandler)
       responseWCS =  opener.open(capability)
       #find namespaces to identify WCS-version returned
       namespaces = dict([node for _, node in ET.iterparse( responseWCS, events=['start-ns'])])
       responseWCS =  opener.open(capability)
    else:
       responseWCS =  urllib.request.urlopen(capability)
       #find namespaces to identify WCS-version returned
       namespaces = dict([node for _, node in ET.iterparse( responseWCS, events=['start-ns'])])
       responseWCS =  urllib.request.urlopen(capability)
    
    wcs_version = namespaces[''][-3:]
    wcsNS = "http://www.opengis.net/wcs/" + wcs_version
    owsNS = "http://www.opengis.net/ows/" + wcs_version

    result = ET.parse(responseWCS).getroot() 
    content = result.find( "{%s}Contents" % wcsNS)
    
    layers =  content.findall( "{%s}CoverageSummary" % wcsNS)
    layerNames = []
    if wcs_version =="1.1":
       for lyr in layers: layerNames.append([lyr.find("{%s}Identifier" % wcsNS).text, lyr.find("{%s}Title" % owsNS).text ])
    else:
       for lyr in layers: layerNames.append([lyr.find("{%s}CoverageId" % wcsNS).text, lyr.find("{%s}CoverageId" % wcsNS).text ])
    
    return layerNames

def makeWFSuri( url, name='', srsname="EPSG:28992", version='1.0.0', bbox=None ):
    params = {  'SERVICE': 'WFS',
                'VERSION': version ,
                'REQUEST': 'GetFeature',
                'TYPENAME': name,
                'SRSNAME': srsname }
    
    uri = url.split("?")[0] + '?' + urllib.parse.unquote( urllib.parse.urlencode(params) )
    return uri

def makeWMTSuri( url, layer, tileMatrixSet, srsname="EPSG:3857", styles='', format='image/png' ):
    params = {  'tileMatrixSet': tileMatrixSet,
                'styles': styles, 
                'format': format ,
                'layers': layer,
                'crs': srsname,
                'contextualWMSLegend': 0, 
                'url': url.split('?')[0]  }
    
    uri = urllib.parse.unquote( urllib.parse.urlencode(params)  )
    return uri

def makeWCSuri( url, layer ): # srsname="EPSG:28992", format="GEOTIFF"
    params = { 
                'dpiMode': 7 ,
                'identifier': layer,
                'url': url.split('?')[0]  } 

    uri = urllib.parse.unquote( urllib.parse.urlencode(params)  )
    return uri 
      
