from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QDialog 
from .ui_inspireNL_dialog import Ui_inspireNLdlg

class inspireNLabout(QDialog):
    """The dialog with the settins and about info

    :param parent: the parent window 
    :type parent: QWidget
    """
    
    def __init__(self, parent=None):
        """setup the user interface"""
        QDialog.__init__(self, None)
        self.setWindowFlags( self.windowFlags() & ~Qt.WindowContextHelpButtonHint )
        self.ui = Ui_inspireNLdlg()
        self.ui.setupUi(self)   
