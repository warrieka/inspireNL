# -*- coding: utf-8 -*-
from qgis.PyQt.QtCore import QSettings
from qgis.core import QgsNetworkAccessManager
import sys, os, urllib.request

class settings(object):
    """Called one startup to get initial values from registry, saves changes to registry"""
    def __init__(self):
        self.s = QSettings()
        self.timeout =  int( self.s.value("inspireNL/timeout" ,15))
        self.getProxySettings()

    def getProxySettings(self):
        self.proxyEnabled = proxyHost = proxyPort = proxyUser = proxyPassword = None
        self.proxyUrl = ""

        self.proxyEnabled = self.s.value("proxy/proxyEnabled", "")
        self.proxy_type = "DefaultProxy"
        proxies = urllib.request.getproxies()
        if len(proxies) == 0:
            qgsNetMan = QgsNetworkAccessManager.instance() 
            self.proxy = qgsNetMan.proxy().applicationProxy() 
            proxyHost =  self.proxy.hostName() 
            proxyPort = str( self.proxy.port()) 
            proxyUser =  self.proxy.user() 
            proxyPassword =  self.proxy.password()
            
            if proxyHost:
                self.proxyUrl = "http://"
                if proxyUser and proxyPassword:
                    self.proxyUrl += proxyUser + ':' + proxyPassword + '@'
                self.proxyUrl += proxyHost + ':' + proxyPort
                self.proxyUrlS = self.proxyUrl.replace("http://", "https://")

        elif len(proxies) > 0 and 'http' in list(proxies.keys()):
                self.proxyUrl = proxies['http']
                self.proxyUrlS = proxies['https']
            
    def setTimeout(self,  seconds ):
        """Save changes in timeout setting"""
        self.s.setValue("inspireNL/timeout", seconds)
