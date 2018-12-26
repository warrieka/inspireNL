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
        """Get proxy-settings for corporate networks, try QgsNetworkAccessManager first, then urllib.request.getproxies()"""
        self.proxyEnabled = self.proxyHost = self.proxyPort = self.proxyUser = self.proxyPassword = None
        self.proxyUrl = ""
        proxyEnabled = self.s.value("proxy/proxyEnabled", "")
        if proxyEnabled == 1 or proxyEnabled == "true": #1 is win or linux, mac is "true"
            self.proxyEnabled = True
            self.proxy_type = self.s.value("proxy/proxyType", "")
            self.proxyHost = self.s.value("proxy/proxyHost", "" )
            self.proxyPort = self.s.value("proxy/proxyPort", "" )
            self.proxyUser = self.s.value("proxy/proxyUser", "" )
            self.proxyPassword = self.s.value("proxy/proxyPassword", "" )

            if self.proxy_type == "DefaultProxy": 
               proxies = urllib.request.getproxies()
               if len(proxies) == 0:
                  qgsNetMan = QgsNetworkAccessManager.instance() 
                  proxy = qgsNetMan.proxy().applicationProxy() 
                  self.proxyHost = proxy.hostName() 
                  self.proxyPort = str(proxy.port()) 
                  self.proxyUser = proxy.user() 
                  self.proxyPassword = proxy.password() 

               elif len(proxies) > 0 and 'http' in list(proxies.keys()):
                  self.proxyUrl = proxies['http']
                  self.proxyUrlS = proxies['https']

            else:
               self.proxyUrl = "http://"
               if self.proxyUser and self.proxyPassword:
                   self.proxyUrl += self.proxyUser + ':' + self.proxyPassword + '@'
               self.proxyUrl += self.proxyHost + ':' + self.proxyPort
               self.proxyUrlS = self.proxyUrl.replace("http://", "https://")
            
    def setTimeout(self,  seconds ):
        """Save changes in timeout setting"""
        self.s.setValue("inspireNL/timeout", seconds)
