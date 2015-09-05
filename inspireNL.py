# -*- coding: utf-8 -*-
"""
/***************************************************************************
 inspireNL
                                 A QGIS plugin
 Dataset van de het Nederlandse Dataportaal Nationaal Georegister bevragen en 
 toevoegen aan QGIS.
                              -------------------
        begin                : 2015-08-31
        git sha              : $Format:%H$
        copyright            : (C) 2015 by KGIS
        email                : kaywarrie@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
# Initialize Qt resources from file resources.py
import resources_rc as resources
# Import the code for the dialog
from inspireNLabout import inspireNLabout
from dataCatalog import dataCatalog
import os.path, sys


class inspireNL:
    def __init__(self, iface):
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(self.plugin_dir, 'i18n', 
'{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialogs (after translation) and keep reference
        self.aboutDlg = inspireNLabout()
        self.dataCatalogDlg = dataCatalog(self.iface)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&INSPIRE Nederland plugin voor QGIS')
        
        self.toolbar = self.iface.addToolBar(u'inspireNL')
        self.toolbar.setObjectName(u'inspireNL')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        "Get the translation for a string using Qt translation API."
        return QCoreApplication.translate('inspireNL', message)

    def add_action(self, icon_path, text, callback, enabled_flag=True, add_to_menu=True,  add_to_toolbar=True, status_tip=None, parent=None):
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(self.menu, action)

        self.actions.append(action)

        return action

    def initGui(self):        
        self.add_action( ':/plugins/inspireNL/images/icon.png',
            text=self.tr(u'Nationaal Georegister'), callback=self.runCatalog, 
            parent=self.iface.mainWindow())

        self.add_action( ':/plugins/inspireNL/images/wrench.png',
            text=self.tr(u'INSPIRE NL'), callback=self.runAbout, 
            parent=self.iface.mainWindow())
        
    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&INSPIRE Nederland plugin voor QGIS'), action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    def runAbout(self):
        ' show the dialog'
        self.aboutDlg.show()
        # Run the dialog event loop and See if OK was pressed
        result = self.aboutDlg.exec_()
   
    def runCatalog(self):
        ' show the dialog'
        self.dataCatalogDlg.show()
        # Run the dialog event loop and See if OK was pressed
        result = self.dataCatalogDlg.exec_()