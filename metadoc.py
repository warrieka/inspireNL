from urllib.parse import urlencode
import xml.etree.ElementTree as ET
from .webUtil import getUrlData, metaError

class MDRecord(object):
    """Find and Interact with CSW-service metadata record. 
    
    :param uuid: the unique id of the record.
    """
    def __init__(self, uuid):
        self.uuid = uuid
        self.ns = {'gmd':'http://www.isotc211.org/2005/gmd', 'srv':'http://www.isotc211.org/2005/srv',
                   'gmx':'http://www.isotc211.org/2005/gmx', 'gco':'http://www.isotc211.org/2005/gco'}
        self.baseUrl = "https://nationaalgeoregister.nl/geonetwork/srv/dut/csw"
        self.xml   = self.getmetadataXML()
        titleNode  = self.xml.find('gmd:MD_Metadata/gmd:identificationInfo/srv:SV_ServiceIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString', self.ns)
        self.title = titleNode.text if titleNode else uuid
        abstrNode  = self.xml.find('gmd:MD_Metadata/gmd:identificationInfo/srv:SV_ServiceIdentification/gmd:abstract/gco:CharacterString', self.ns)
        self.decription = abstrNode.text if abstrNode else ''
        self.wms   = self.findService('WMS' )
        self.wmts  = self.findService('WMTS')
        self.wcs  = self.findService('WCS')
        self.wfs   = self.findService('WFS' )

        self.atom  = self.findService('ATOM')
        if len(self.atom) > 0:
            self.dl = self.findAtomDownloads(self.atom[0])
        else:
            self.dl = []

    def getmetadataXML(self):
        """Get a metadataRecord from URL 

        :param URL: the URL to metadata record.
        :return: a etree xml-object
        """
        data = {'REQUEST':'GetRecordById', 'Service':'CSW', 'Version':'2.0.2'}
        data['elementSetName'] = 'full'
        data['OutputSchema'] = 'http://www.isotc211.org/2005/gmd'
        data['ID'] = self.uuid
        values = urlencode(data)
        url = self.baseUrl +"?"+ values

        _r = getUrlData(url)
        _xml = ET.fromstring( _r )  
        return _xml

    def findAtomDownloads(self, atom_url):
        """Find the list of donwloads in a atom feed

        :param atom_url: the URL to atom feed.
        :return: a list of atom donwloads 
        """
        try:    
            resp= getUrlData(atom_url)
            results = []
            root = ET.fromstring(resp)
        except ET.ParseError:
            print( "WARNING: Geen correcte xml:  {} ".format(atom_url) )
            return []
        except metaError as me:
            print( "WARNING: http-fout {} -> geeft {}".format(atom_url, me.message) )
            return []
        
        entries =  root.findall( ".//{http://www.w3.org/2005/Atom}entry" )
        for entry in entries:
            dl = entry.find( "{http://www.w3.org/2005/Atom}link")
            titleNode = entry.find( "{http://www.w3.org/2005/Atom}title")
            if dl is not None and titleNode is not None and "href" in dl.attrib: 
               results.append( [ titleNode.text, dl.attrib["href"] ] )  
        return results


    def findService(self, srvType='WMS'):
        """Find the urls of a service of a certain srvType.

        :param srvType: the type of service: wmts, wms, wfs, atom
        :return: a array of url's 
        """
        links = []
        CI_ORs = self.xml.findall('.//gmd:CI_OnlineResource', self.ns)  
        for cior in CI_ORs:
           a = cior.find('.//gmd:protocol/gmx:Anchor', self.ns)
           u = cior.find('.//gmd:linkage/gmd:URL', self.ns)
           a = cior.find('.//gmd:protocol/gco:CharacterString', self.ns) if a is None else a
           u = cior.find('.//gmd:linkage/gco:CharacterString', self.ns) if u is None else u

           if a is not None and srvType.upper() in  a.text.upper():
              links.append(u.text)
        if len(links) == 0:
           links = [n.text for n in self.xml.findall('.//gmd:URL', self.ns)   
                    if n.text and srvType.upper() in n.text.upper()  ]
        return links