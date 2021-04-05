from qgis.core import QgsBlockingNetworkRequest
from qgis.PyQt.QtNetwork import QNetworkRequest
from qgis.PyQt.QtCore import QUrl

def getUrlData(url, data=None, returnBytes=False):
    """Performs a blocking “get” operation on the specified *url* and returns the response,
    if *data* is given a "post" is performed. 

    :param url: the url to fetch 
    :param data: the data to post as bytes 
    :param returnBytes: return bytes instead of string if True
    :return: the response as a string
    """
    bnr = QgsBlockingNetworkRequest()
    if not data:
        respcode = bnr.get(QNetworkRequest( QUrl(url) ) )
    else:
        respcode = bnr.post(QNetworkRequest( QUrl(url) ) , data )

    if respcode == 0: 
        response = bnr.reply().content().data() 
        if returnBytes == False: response = response.decode('utf-8') 
    else: 
        raise metaError( bnr.reply().errorString() )
    return response


class metaError(Exception):
    """Exception, a error in metadataXML
    
    :param message: a message to pass with the exception
    """
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)