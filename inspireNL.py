# -*- coding: utf-8 -*-
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon

# Import the code for the dialog
from .inspireNLabout import inspireNLabout
from .dataCatalog import dataCatalog
import os.path


class inspireNL(object):
    """The inspireNL-toolbar
    
    :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
    :type iface: QgsInterface
        """
    def __init__(self, iface):
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(self.plugin_dir, 'i18n', '{}.qm'.format(locale))

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

    @staticmethod
    def tr(message):
        """Get the translation for a string using Qt translation API.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message. (String)
        """
        "Get the translation for a string using Qt translation API."
        return QCoreApplication.translate('inspireNL', message)

    def add_action(self, icon_path, text, callback, enabled_flag=True, add_to_menu=True, add_to_toolbar=True, status_tip=None, parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list. (QAction)
        """
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
        """Initialize the GUI: Add the plugin menu item and icon to QGIS GUI."""
        self.add_action( ':/plugins/inspireNL/images/inspireSearch.png',
            text=self.tr(u'Zoek INSPIRE Datasets en services'), callback=self.runCatalog, 
            parent=self.iface.mainWindow())

        self.add_action( ':/plugins/inspireNL/images/icon.png', add_to_toolbar=True, 
            text=self.tr(u'Instellen INSPIRE Nederland plugin  voor QGIS'), callback=self.runAbout, 
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
        'show the about dialog'
        self.aboutDlg.show()
        self.aboutDlg.exec_()
   
    def runCatalog(self):
        'show the catalog search dialog'
        if self.dataCatalogDlg.isVisible():
           self.dataCatalogDlg.showNormal()
           self.dataCatalogDlg.activateWindow()
           return 
        
        self.dataCatalogDlg.show()
        # Run the dialog event loop
        self.dataCatalogDlg.exec_()
        
