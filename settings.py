# -*- coding: utf-8 -*-
from qgis.PyQt.QtCore import QSettings
from qgis.core import QgsNetworkAccessManager
from urllib.request import getproxies 

class settings(object):
    """Called one startup to get initial values from registry, saves changes to registry"""
    def __init__(self):
        self.s = QSettings()
        self.timeout =  int( self.s.value("inspireNL/timeout" ,15))
            
    def setTimeout(self,  seconds ):
        """Save changes in timeout setting"""
        self.s.setValue("inspireNL/timeout", seconds)
