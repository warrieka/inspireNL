# -*- coding: utf-8 -*-
import urllib2, urllib, json, sys, os.path, datetime
import xml.etree.ElementTree as ET

class MDdata:
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
              record['geoBox'] = md.find('geoBox').text  #[float(i) for i in md.find('geoBox').text.split('|') ]
           else: 
              record['geoBox'] = ""
           
           record['wms'] = self._findWMS( md )
           record['wfs'] = self._findWFS( md )
           record['download'] = self._findDownload( md )
           
           self.records.append(record)
           
    def _findWFS(self , node ):
        links =  "|".join( [ n.text for n in node.findall("link") ] )
        links = links.split('|') 
        for n in range(1, len( links )):
            if "OGC:WFS" in links[n].upper(): 
              if "http" in  links[n - 1]: #some wfs are store with relative path's, ignore those
                  return links[n - 1]
        return ""
      
    def _findWMS(self , node ):
        links =  "|".join( [ n.text for n in node.findall("link") ] )
        links = links.split('|') 
        for n in range(1, len( links )):
            if "OGC:WMS" in links[n].upper(): 
              if "http" in  links[n - 1]: #some wms are stored with relative path's, ignore those
                  return links[n - 1]
        return ""

    def _findDownload(self , node):
        links =  "|".join( [ n.text for n in node.findall("link") ] )
        links = links.split('|') 
        for n in range(1, len( links )):
            if "DOWNLOAD" in links[n].upper(): 
               if "http" in  links[n - 1]: #some files are stored with relative path's, ignore those
                  return links[n - 1]
        return ""


class MDReader:
    def __init__(self, timeout=15 ):
        self.timeout = timeout
        self.geoNetworkUrl = "http://www.nationaalgeoregister.nl/geonetwork/srv/dut/" #"https://metadata.geopunt.be/zoekdienst/srv/dut"

        self.dataTypes = [["Dataset", "dataset"],["Datasetserie","series"],
                          ["Objectencatalogus","model"],["Service","service"]]
        self.inspireServiceTypes =  ["Discovery","Transformation","View","Other","Invoke"]
        self.inspireannex =  ["i","ii","iii"]

    def _createFindUrl(self, q="", start=1, to=20, orgName='', dataType='', siteId='', inspiretheme='', inspireannex='', inspireServiceType=''):
        geopuntUrl = self.geoNetworkUrl + "/q?fast=index&sortBy=changeDate&"
        data = {}
        data["any"] = "*" + unicode(q).encode('utf-8') + "*"
        data["to"] = to
        data["from"] = start
        
        if orgName  and not " or " in orgName.lower():
            if " " in orgName:
                data["orgName"] = '"' +  orgName + '"' 
            else: 
                data["orgName"] = orgName
                
        if dataType: data['type']= dataType
        if siteId: data['siteId']= siteId                
                
        if inspiretheme: 
            if " " in inspiretheme and not " or " in inspiretheme.lower():
                data["inspiretheme"] = '"' +  inspiretheme + '"' 
            else: 
                data["inspiretheme"] = inspiretheme            
        if inspireannex and (inspireannex.lower() in self.inspireannex ) : 
            data["inspireannex"] = inspireannex.lower()
        if inspireServiceType : 
            data["serviceType"] = inspireServiceType.lower() 

        values = urllib.urlencode(data)
        result = geopuntUrl + values
        return result
          
    def list_inspire_theme(self, q=''):
        url = self.geoNetworkUrl + "/xml.search.keywords?pNewSearch=true&pTypeSearch=1&pThesauri=external.theme.inspire-theme&pKeyword=*" + unicode(q).encode('utf-8') +"*"
        try:
            response= urllib2.urlopen(url, timeout=self.timeout)
        except  (urllib2.HTTPError, urllib2.URLError) as e:
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
        url = self.geoNetworkUrl + "/main.search.suggest?field=any" 
        if q:
            url= url + "&q=" + unicode(q).encode('utf-8') 
        
        try:
            response= urllib2.urlopen(url, timeout=self.timeout)
        except  (urllib2.HTTPError, urllib2.URLError) as e:
            raise metaError( str( e.reason ))
        except:
            raise metaError( str( sys.exc_info()[1] ))
        else:
            result = json.load(response)
            return result[1]

    def list_organisations(self, q=''):
        url = self.geoNetworkUrl + "/main.search.suggest?field=orgName" 
        if q:
            url= url + "&q=" + unicode(q).encode('utf-8') 
        try:
            response = urllib2.urlopen(url, timeout=self.timeout)
        except  (urllib2.HTTPError, urllib2.URLError) as e:
            raise metaError( str( e.reason ))
        except:
            raise metaError( str( sys.exc_info()[1] ))
        else:
            result = json.load(response)
            if len( result ) <= 2:
               organisations = result[1]
               organisations.sort()
               return organisations
            else:
               return []
               

    def list_bronnen(self):
        url = self.geoNetworkUrl + "/xml.info?type=sources"
        try:
            response = urllib2.urlopen(url, timeout=self.timeout)
        except  (urllib2.HTTPError, urllib2.URLError) as e:
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

    def search(self, q="", start=1, to=20, orgName='', dataType='', siteId='', inspiretheme='', inspireannex='', inspireServiceType='' ):
        url = self._createFindUrl( q, start, to,  orgName, dataType, siteId, inspiretheme, inspireannex, inspireServiceType)
        try:
            response = urllib2.urlopen(url, timeout=self.timeout)
        except  (urllib2.HTTPError, urllib2.URLError) as e:
            raise metaError( str( e.reason ) +' on '+ url )
        except:
            raise metaError( str( sys.exc_info()[1] ))
        else:
            result = ET.parse(response)
            resultXML = result.getroot()
            return  resultXML

    def searchAll(self, q="", orgName='', dataType='', siteId='', inspiretheme='', inspireannex='', inspireServiceType=''):
        start= 1
        step= 100        
        searchResult = self.search(q, start, step,  orgName, dataType, siteId, inspiretheme, inspireannex, inspireServiceType)
        count = int( searchResult[0].attrib["count"] )
        start += step
        while (start) <= count:  #https://metadata.geopunt.be/zoekdienst/srv/dut/q?fast=index&sortBy=changeDate&to=&from=Herbruikbaar&any=%2A%2A'
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

      
def getWmsLayerNames( url ):
      if (not "request=GetCapabilities" in url.lower()) or (not "service=wms" in url.lower()):
          capability = url.split("?")[0] + "?request=GetCapabilities&version=1.3.0&service=wms"
      else: 
          capability = url
      
      responseWMS =  urllib2.urlopen(capability)
      
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

def getWFSLayerNames( url ):
      if (not "request=GetCapabilities" in url.lower()) or (not "service=wfs" in url.lower()):
          capability = url.split("?")[0] + "?request=GetCapabilities&version=1.0.0&service=wfs"
      else: 
          capability = url
      
      responseWFS =  urllib2.urlopen(capability)
      
      result = ET.parse(responseWFS)
      layers =  result.findall( ".//{http://www.opengis.net/wfs}FeatureType" )
      layerNames=[]

      for lyr in layers:
          name= lyr.find("{http://www.opengis.net/wfs}Name")
          title = lyr.find("{http://www.opengis.net/wfs}Title")
          srs = lyr.find("{http://www.opengis.net/wfs}SRS")
          if ( name != None) and ( title != None ):
              if srs == None: layerNames.append(( name.text, title.text, 'EPSG:31370'))
              else: layerNames.append(( name.text, title.text, srs.text))

      return layerNames

def makeWFSuri( url, name='', srsname="EPSG:3857", version='1.0.0' ):
    params = {  'SERVICE': 'WFS',
                'VERSION': version ,
                'REQUEST': 'GetFeature',
                'TYPENAME': name,
                'SRSNAME': srsname }
    
    uri = url.split("?")[0] + '?' + urllib.unquote( urllib.urlencode(params) )
    return uri