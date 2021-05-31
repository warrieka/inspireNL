from urllib.parse import urlencode
import xml.etree.ElementTree as ET
from .webUtil import getUrlData

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

    def findService(self, srvType='WMS'):
        """Find the urls of a service of a certain srvType.

        :param srvType: the type of service: wmts, wms, wfs, atom
        :return: a array of url's 
        """
        return [n.text for n in
                self.xml.findall('.//gmd:URL', self.ns)   
                if n.text and srvType.upper() in n.text.upper()  ]
        