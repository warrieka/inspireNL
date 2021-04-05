import json, sys, json
from urllib.parse import urlencode, unquote, urlparse, parse_qsl
import xml.etree.ElementTree as ET
from io import StringIO
from .webUtil import getUrlData, metaError

CSW_URL = "https://www.nationaalgeoregister.nl/geonetwork/srv/dut/inspire"


class MDdata(object):
    def __init__(self, metadataXML):
        """Parse a CSW-metadataXML 
    
        :param metadataXML: a CSW-metadata XMLdocument
        """
        if not metadataXML: return
        self.count = int( metadataXML.attrib["numberOfRecordsMatched"] ) 
        self.records = []
        self.count = 0
        
        mds = metadataXML.findall("{http://www.opengis.net/cat/csw/2.0.2}Record")
        for md in mds:
           record = {}
           identifier = md.find("{http://purl.org/dc/elements/1.1/}identifier")
           title = md.find('{http://purl.org/dc/elements/1.1/}title') 

           if identifier == None or not identifier.text: continue 

           record['uuid'] = identifier.text
           record['title'] = title.text

           description = md.find('{http://purl.org/dc/elements/1.1/}description')
           if (description != None):
              record['abstract'] = description.text if description.text != None else ''

           bbox = md.find('{http://www.opengis.net/ows}BoundingBox')
           if (bbox != None): 
               LowerCorner = md.find('{http://www.opengis.net/ows}LowerCorner')
               UpperCorner = md.find('{http://www.opengis.net/ows}UpperCorner')
               if LowerCorner and UpperCorner: 
                   record['geoBox'] = [float(n) for n in LowerCorner.text.split(" ")] + [float(n) for n in UpperCorner.text.split(" ")]
               else:
                   record['geoBox'] = [3.1, 50.6, 7.4, 53.6]
           else: 
               record['geoBox'] = [3.1, 50.6, 7.4, 53.6]
           
           record['wms'] =  self._findWXS( md, "OGC:WMS" )
           record['wfs'] =  self._findWXS( md, "OGC:WFS" )
           record['wcs'] =  self._findWXS( md, "OGC:WCS" )
           record['wmts'] = self._findWXS( md, "OGC:WMTS")
           record['download'] = self._findDownloads( md )
           self.records.append(record)
           
    def _findWXS(self, node, protocol= None ):
        links =    [n for n in node.findall("{http://purl.org/dc/elements/1.1/}URI") 
                            if "protocol" in n.attrib and n.attrib["protocol"] == protocol] 
        links +=   [ n for n in node.findall("{http://purl.org/dc/elements/1.1/}URI")
                     if n.text
                     and 'SERVICE' in dict( parse_qsl( urlparse( n.text.upper() ).query ))  
                     and dict(parse_qsl(urlparse( n.text.upper() ).query))['SERVICE'] in protocol ]   
        
        if len(links) > 0: 
            name = links[0].attrib["name"] if "name" in links[0].attrib else links[0].text
            return (name, links[0].text)
        return ("","")

    def _findDownloads(self, node):
        links = [n for n in node.findall("{http://purl.org/dc/elements/1.1/}URI") 
                                if "protocol" in n.attrib and "DOWNLOAD" in n.attrib["protocol"].upper() ] 
        atoms = [n.text for n in node.findall("{http://purl.org/dc/elements/1.1/}URI") 
                                if "protocol" in n.attrib and "ATOM" in n.attrib["protocol"].upper() ] 
        
        if len(links) == 0 and len(atoms) == 0: 
            return []
        
        if len(links) > 0 and len(atoms) == 0: 
            results = [ [ n.attrib["name"] if "name" in n.attrib else n.text , n.text ] for n in links ]
            return results
    
        atom = atoms[0]

        try:    
            resp= getUrlData(atom)
            results = []
            root = ET.fromstring(resp)
        except ET.ParseError:
            print( "WARNING: Geen correcte xml:  {} ".format(atom) )
            return []
        except metaError as me:
            print( "WARNING: http-fout {} -> geeft {}".format(atom, me.message) )
            return []
        
        entries =  root.findall( ".//{http://www.w3.org/2005/Atom}entry" )
        for entry in entries:
            dl = entry.find( "{http://www.w3.org/2005/Atom}link")
            titleNode = entry.find( "{http://www.w3.org/2005/Atom}title")
            if dl is not None and titleNode is not None and "href" in dl.attrib: 
               results.append( [ titleNode.text, dl.attrib["href"] ] )  
        return results


class MDReader(object):
    """Interact with CSW-service, to get info
    
    :param proxyUrl: the proxy to use for internet calls
    :param timeout: the timeout for internet calls
    """
    def __init__(self):
        self.geoNetworkUrl =  CSW_URL
        self.dataTypes = [["Dataset", "dataset"],["Service","service"]]
        self.inspireServiceTypes = ["discovery","download","view","other"]
        
    def _createFindUrl(self, q="", start=1, maxRecords=100, orgName='', dataType='', inspiretheme='', inspireServiceType=''): 
        url = self.geoNetworkUrl 
        data = {}
        
        #escape '-sign's in CQL 
        q = q.replace("'", "''")
        orgName = orgName.replace("'", "''")
        inspiretheme = inspiretheme.replace("'", "''")
        
        #make CQL query
        CQLparts = []
        
        if inspiretheme: 
            CQLparts.append("(Subject LIKE '%"+ inspiretheme +"%' AND AnyText = 'GEMET - INSPIRE themes, version 1.0')")
        if len(q.strip()) > 0: 
            CQLparts.append(" AnyText LIKE '%" + q + "%' ")
        if orgName: 
            CQLparts.append(" OrganisationName = '" + orgName + "' ")
        if dataType: 
            CQLparts.append(" type = '" + dataType + "' ")
        if inspireServiceType: 
            CQLparts.append(" ServiceType = '" + inspireServiceType + "' ")

        CQL = "(" + " AND ".join(CQLparts) + ")"

        data["request"] = "GetRecords"
        data["service"] = "CSW"
        data["version"] = "2.0.2"
        data["elementsetname"] = "full"
        data["typenames"] = "gmd:MD_Metadata"
        data["RESULTTYPE"] = "results"
        data["constraintLanguage"] = "CQL_TEXT"
        data["constraint_language_version"] = "1.1.0"          
        data["maxRecords"] = maxRecords
        data["startPosition"] = start
        data["constraint"] = CQL
                
        values = urlencode(data)

        return url +"?"+ values
          
    def list_inspire_theme(self):
        """List the inspire-themes
        
        :return: a list containing the inspire themes
        """
        return [ "Administratieve eenheden", "Adressen", "Atmosferische omstandigheden", "Beschermde gebieden",
            "Biogeografische gebieden", "Bodem", "Bodemgebruik", "Energiebronnen", 
            "Faciliteiten voor landbouw en aquacultuur",
            "Faciliteiten voor productie en industrie", "Gebieden met natuurrisico's",
            "Gebiedsbeheer, gebieden waar beperkingen gelden, gereguleerde gebieden en rapportage-eenheden",
            "Gebouwen", "Geografisch rastersysteem", "Geografische namen", "Geologie",
            "Habitats en biotopen", "Hoogte", "Hydrografie", "Kadastrale percelen", "Landgebruik", 
            "Menselijke gezondheid en veiligheid",
            "Meteorologische geografische kenmerken", "Milieubewakingsvoorzieningen", "Minerale bronnen", 
            "Nutsdiensten en overheidsdiensten", "Oceanografische geografische kenmerken", "Orthobeeldvorming", 
            "Spreiding van de bevolking — demografie", "Spreiding van soorten", "Statistische eenheden", 
            "Systemen voor verwijzing door middel van coördinaten", "Vervoersnetwerken", "Zeegebieden" ]
    
    def list_suggestionKeyword(self):
        """List the Keywords
        
        :return: a list with the Keywords
        """
        url = self.geoNetworkUrl + "?request=GetDomain&service=CSW&version=2.0.2&PropertyName=Subject"
        resp = getUrlData(url)
        result = ET.fromstring(resp)  
        return [ n.text for n in result.findall('.//{http://www.opengis.net/cat/csw/2.0.2}Value') ]

    def list_organisations(self):
        """List the organisations
        
        :return: a list with the organisations
        """
        url = self.geoNetworkUrl + '?request=GetDomain&service=CSW&version=2.0.2&PropertyName=OrganisationName'
        resp = getUrlData(url)
        result = ET.fromstring(resp)  
        organisations = [ n.text for n in result.findall('.//{http://www.opengis.net/cat/csw/2.0.2}Value') ]
        organisations.sort()
        return organisations

    def _search(self, q="", start=1, step=100, orgName='', dataType='', inspiretheme='',  inspireServiceType=''):
        """Search the csw with the following parameters:
        
        :param q: free text to seach for
        :param start: initial postion of the searchresult 
        :param step: size of the searchresult
        :param orgName: filter on the name of a organisation
        :param dataType: filter on the type of record: service or dataset 
        :param inspiretheme: filter on inspiretheme
        :param inspireServiceType: filter on inspire serviceType
        :return: a XMLdocument with the results
        """
        url = self._createFindUrl( q, start, step, orgName, dataType, inspiretheme, inspireServiceType)
        resp = getUrlData(url)
        result = ET.fromstring(resp)  
        return result

    def searchAll(self, q="", orgName='', dataType='', inspiretheme='', inspireServiceType=''):
        """Search the csw, making multiple calls in case of large resultsets, with the following parameters:
        
        :param q: free text to seach for
        :param orgName: filter on the name of a organisation
        :param dataType: filter on the type of record: service or dataset 
        :param inspiretheme: filter on inspiretheme
        :param inspireServiceType: filter on inspire serviceType
        :return: a composite XMLdocument with the results
        """
        start= 1
        step= 100
        result = self._search(q, start, step, orgName, dataType, inspiretheme, inspireServiceType)
        searchResult = result.find(".//{http://www.opengis.net/cat/csw/2.0.2}SearchResults")
        if not searchResult: 
            return
        count = int( searchResult.attrib["numberOfRecordsMatched"] )
        start += step
        while (start) <= count:  
           result = self._search(q, start, step, orgName, dataType,inspiretheme, inspireServiceType)
           mds= result.findall(".//{http://www.opengis.net/cat/csw/2.0.2}Record")
           for md in mds: searchResult.append( md )
           start += step

        mdata = MDdata( searchResult )
        return mdata

   
def getWmsLayerNames(url):
    """List all the thr layers in a WMS
    
    :param url: the getcapabilities url of the WMS
    :param proxyUrl: the url of the network proxy 
    :param timeout:  the timeout for internet calls
    
    :return: a list of tuples in de form: [(name, title, style ), ...]
    """
    capability = url.split("?")[0] + "?request=GetCapabilities&version=1.3.0&service=wms"
    
    resp = getUrlData(capability)
    result = ET.fromstring(resp)  
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
    """List all the layers in a WFS
    
    :param url: the getcapabilities url of the WFS
    :param proxyUrl: the url of the network proxy 
    :param timeout:  the timeout for internet calls
    
    :return: a list of tuples in de form: [(name, title, srs ), ...]
    """
    capability = url.split("?")[0] + "?request=GetCapabilities&version=2.0.0&service=wfs"
    resp = getUrlData(capability)
    result = ET.fromstring(resp)  
    layerNames=[]
    
    #default
    version = "2.0.0"
    serv = result.find(".//{http://www.opengis.net/ows/1.1}ServiceTypeVersion")

    if serv is None: 
        serv = result.find(".//{http://www.opengis.net/ows}ServiceTypeVersion")
    
    if serv is not None:  
        version = serv.text
    
    if version == "2.0.0": 
        layers =  result.findall( ".//{http://www.opengis.net/wfs/2.0}FeatureType" )
        for lyr in layers:
            name= lyr.find("{http://www.opengis.net/wfs/2.0}Name")
            title = lyr.find("{http://www.opengis.net/wfs/2.0}Title")
            srs = lyr.find("{http://www.opengis.net/wfs/2.0}DefaultCRS")
            
            isComplex = testComplex(url, name.text, version)
            
            if ( name != None) and ( title != None ):
                if srs == None: layerNames.append(( name.text, title.text, 'EPSG:28992'))
                else: layerNames.append(( name.text, title.text, srs.text, isComplex))          
    elif version == "1.1.0": 
        layers =  result.findall( ".//{http://www.opengis.net/wfs/2.0}FeatureType" )
        for lyr in layers:
            name= lyr.find("{http://www.opengis.net/wfs}Name")
            title = lyr.find("{http://www.opengis.net/wfs}Title")
            srs = lyr.find("{http://www.opengis.net/wfs}DefaultCRS")
                        
            isComplex = testComplex(url, name.text, version)
            
            if ( name != None) and ( title != None ):
                if srs == None: layerNames.append(( name.text, title.text, 'EPSG:28992'))
                else: layerNames.append(( name.text, title.text, srs.text, isComplex))
    else: 
        layers =  result.findall( ".//{http://www.opengis.net/wfs}FeatureType" )
        for lyr in layers:
            name= lyr.find("{http://www.opengis.net/wfs}Name")
            title = lyr.find("{http://www.opengis.net/wfs}Title")
            srs = lyr.find("{http://www.opengis.net/wfs}SRS")
            if ( name != None) and ( title != None ):
                if srs == None: layerNames.append(( name.text, title.text, 'EPSG:28992'))
                else: layerNames.append(( name.text, title.text, srs.text, False))
    return { 'version': version, 'layerNames': layerNames }

def getWMTSlayersNames( url ):
    """List all the layers in a WMTS
    
    :param url: the getcapabilities url of the WCS
    :param proxyUrl: the url of the network proxy 
    :param timeout:  the timeout for internet calls
    
    :return: a list of tuples in de form: [(name, title, matrix, format, srs ), ...]
    """
    if (not "request=getcapabilities" in url.lower()) or (not "service=wmts" in url.lower()):
        capability = url.split("?")[0] + "?service=WMTS&request=Getcapabilities&version="
    else: 
        capability = url

    resp = getUrlData(capability)
    result = ET.fromstring(resp)  
    content = result.find( "{http://www.opengis.net/wmts/1.0}Contents" )
    layers =  content.findall( "{http://www.opengis.net/wmts/1.0}Layer" )
    layerNames = []
    
    matrixSets = content.findall("{http://www.opengis.net/wmts/1.0}TileMatrixSet")

    for lyr in layers:
        name=    lyr.find("{http://www.opengis.net/ows/1.1}Identifier")
        title =  lyr.find("{http://www.opengis.net/ows/1.1}Title")
        matrix = lyr.find("{http://www.opengis.net/wmts/1.0}TileMatrixSetLink/{http://www.opengis.net/wmts/1.0}TileMatrixSet")
        format = lyr.find("{http://www.opengis.net/wmts/1.0}Format")
        
        srsList = [ n.find("{http://www.opengis.net/ows/1.1}SupportedCRS").text
                    for n in matrixSets if n.find("{http://www.opengis.net/ows/1.1}Identifier").text == matrix.text]

        if srsList: srs =  "EPSG:"+ srsList[0].split(':')[-1]
        else: srs = "" 
        
        if ( name != None) and ( title != None ) and ( matrix != None ) and ( format != None ):
              layerNames.append(( name.text, title.text, matrix.text, format.text, srs ))

    return layerNames

def getWCSlayerNames( url, wcs_version="1.1"):
    """List all the layers in a WFS
    
    :param url: the getcapabilities url of the WCS
    :param proxyUrl: the url of the network proxy 
    :param wcs_version: the version of WCS to use, supported versions: 2.0, 1.1, 1.0
    :param timeout:  the timeout for internet calls
    
    :return: a list of tuples in de form:   [(Identifier, Title ), ...]
    """    
    capability = url.split("?")[0] + "?request=GetCapabilities&version=%s.0&service=WCS" % wcs_version

    resp = getUrlData(capability)
    result = ET.fromstring(resp) 

    #find namespaces to identify WCS-version returned
    namespaces = dict([node for _, node in ET.iterparse( StringIO(result), events=['start-ns'])])
    wcs_version = namespaces[''][-3:]
    wcsNS = "http://www.opengis.net/wcs/" + wcs_version
    owsNS = "http://www.opengis.net/ows/" + wcs_version

    content = result.find( "{%s}Contents" % wcsNS)
    
    layers =  content.findall( "{%s}CoverageSummary" % wcsNS)
    layerNames = []
    if wcs_version =="1.1":
       for lyr in layers: layerNames.append([lyr.find("{%s}Identifier" % wcsNS).text, lyr.find("{%s}Title" % owsNS).text ])
    else:
       for lyr in layers: layerNames.append([lyr.find("{%s}CoverageId" % wcsNS).text, lyr.find("{%s}CoverageId" % wcsNS).text ])
    
    return layerNames

def makeWFSuri( url, name='', srsname="EPSG:28992", version='1.0.0' ):
    """Make a QGIS-uri to load WFS-services.
    
    :param url: the base url of the wfs
    :param name: The name of the layer
    :param srsname: the crs as a string,this form <auth>:<id>, like EPSG:28992
    :param version: WFS version: 1.0.0, 1.1.0 or 2.0.0

    :return: the QGIS-uri
    """
    params = {  'SERVICE': 'WFS',
                'VERSION': version ,
                'REQUEST': 'GetFeature',
                'TYPENAME': name,
                'SRSNAME': srsname }
    
    uri = url.split("?")[0] + '?' + unquote( urlencode(params) )
    return uri

def makeWMTSuri( url, layer, tileMatrixSet, srsname="EPSG:3857", styles='', format='image/png' ):
    """Make a QGIS-uri to load WMTS-services.
    
    :param url: the base url of the WMTS
    :param name: The name of the layer
    :param tileMatrixSet: The namae of the tileMatrixSet to use
    :param srsname: the crs as a string,this form <auth>:<id>, like EPSG:28992
    :param styles: the name(s) of the styles to use
    :param format: the name of the mimetype of the output: image/png, image/jpeg, ...

    :return: the QGIS-uri
    """
    params = {  'tileMatrixSet': tileMatrixSet,
                'styles': styles, 
                'format': format ,
                'layers': layer,
                'crs': srsname,
                'contextualWMSLegend': 0, 
                'url': url.split('?')[0]  }
    
    uri = unquote( urlencode(params)  )
    return uri

def makeWCSuri( url, layer ):  
    """Make a QGIS-uri to load WCS-services.
    
    :param url: the base url of the WMTS
    :param layer: The name of the layer

    :return: the QGIS-uri
    """
    params = {  'dpiMode': 7 ,
                'identifier': layer,
                'url': url.split('?')[0]  } 

    uri = unquote( urlencode(params) )
    return uri 
      
def testComplex(url, typeName, version="1.1.0" ):
    """Test if a WFS has complex features for a specific layer (typeName)
    
    :param url: the url of the WFS
    :param typeName: the typeName of the layer to test for complex features
    :param version: WFS version: 1.1.0 or 2.0.0
    :param proxyUrl: the url of the network proxy 
    :param timeout:  the timeout for internet calls
    
    :return: a boolean, true if the WFS has complex features
    """
    if version not in ["1.1.0", "2.0.0"]: return False
    if version == "1.1.0": countStr = "maxFeatures"
    if version == "2.0.0": countStr = "count"
    
    baseUrl = url.split("?")[0] 
    qryString = "?{}=1&SERVICE=WFS&VERSION={}&REQUEST=GetFeature&TYPENAME={}&outputFormat=json".format(countStr, version, typeName)
    fullUrl = baseUrl + qryString
    
    try: 
        response = getUrlData(fullUrl)
        geojson = json.loads(response) 
        features = geojson['features']
        
        if len(features) > 0:
            properties = features[0]["properties"]
            for n in properties:
                val = properties[n]
                if type(val) == dict: return True
        return False
            
    except:
        print("Error in finding out WFS-complex:" + str( sys.exc_info() ) )
        return False
    
def downloadWFS(url, typeName, outputLocation, crs="EPSG:4326", maxCount=10000, version="1.1.0", bbox=[]):
    """Download a WFS as GML-file for a specific area
    
    :param url: the url of the WFS
    :param typeName: the typeName of the layer to download
    :param outputLocation: the path and filename of the output gml
    :param maxCount: max number of features
    :param version: WFS version: 1.1.0 or 2.0.0
    :param bbox: limit the output to a certain area
    :param proxyUrl: the url of the network proxy 
    :param timeout:  the timeout for internet calls
    
    :return: outputLocation
    """
    if version not in ["1.1.0", "2.0.0"]: 
        version = "1.1.0"
    
    if version == "1.1.0": 
        typeNameStr = "TYPENAME"
        countStr = "maxFeatures"
    if version == "2.0.0":
        typeNameStr = "TYPENAMES"
        countStr = "count"
    if bbox: bboxS = ",".join([str(n) for n in bbox])
    
    # Thijs Brentjens, suggestiont for workaround different axis order for 4258, 4326
    # TODO: which CRSes should take into account different axis order for WFS download?
    if 'EPSG' in crs and ('4258' in crs or '4326' in crs) and bbox:
        bboxS = str(bbox[1])+','+str(bbox[0])+','+str(bbox[3])+','+str(bbox[2])  
    elif bbox: bboxS = ",".join([str(n) for n in bbox])  
    
    baseUrl = url.split("?")[0] 
    qryString = "?{}={}&SERVICE=WFS&VERSION={}&REQUEST=GetFeature&{}={}&srsName={}&bbox={}".format(
                                                countStr, maxCount, version, typeNameStr, typeName, crs, bboxS) 
    fullUrl = baseUrl + qryString
    response = getUrlData(fullUrl, returnBytes=True)
        
    with open(outputLocation, 'wb') as out_file:
        out_file.write(response)

    return outputLocation
    
def xmlIsEmpty(xml_file, gmlException=True):
    """test if a xml file contais data
    
    :param xml_file: a path to a xml file. 
    :param gmlException: also return if gmlException
    
    return: True if empty else False
    """
    try:
        tree = ET.parse(xml_file)  
        root = tree.getroot()
        if gmlException and "ExceptionReport" in root.tag:
            return True
        
        return not len(root)
    except:
        return True
