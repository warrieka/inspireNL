# -*- coding: utf-8 -*-
import os
from qgis.PyQt.QtCore import Qt, QSettings, QTranslator, QTranslator
from qgis.PyQt.QtWidgets import QDialog 
from .ui_inspireNL_dialog import Ui_inspireNLdlg

class inspireNLabout(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, None)
        self.setWindowFlags( self.windowFlags() & ~Qt.WindowContextHelpButtonHint )

        # initialize locale
        locale = QSettings().value("locale/userLocale", "nl")
        if not locale: locale == 'nl' 
        else: locale = locale[0:2]
        localePath = os.path.join(os.path.dirname(__file__), 'i18n', 'geopunt4qgis_{}.qm'.format(locale))
        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)
            QTranslator.installTranslator(self.translator)
        self._initGui(parent)

    def _initGui(self, parent):
        self.ui = Ui_inspireNLdlg()
        self.ui.setupUi(self)   