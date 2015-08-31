# -*- coding: utf-8 -*-

import os

from PyQt4 import QtGui, QtCore
from ui_inspireNL_dialog import Ui_inspireNLdlg

class inspireNLabout(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, None)
        self.setWindowFlags( self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint )

        # initialize locale
        locale = QtCore.QSettings().value("locale/userLocale", "nl")
        if not locale: locale == 'nl' 
        else: locale = locale[0:2]
        localePath = os.path.join(os.path.dirname(__file__), 'i18n', 'geopunt4qgis_{}.qm'.format(locale))
        if os.path.exists(localePath):
            self.translator = QtCore.QTranslator()
            self.translator.load(localePath)
            QtCore.QCoreApplication.installTranslator(self.translator)
        self._initGui(parent)

    def _initGui(self, parent):
        self.ui = Ui_inspireNLdlg()
        self.ui.setupUi(self)   