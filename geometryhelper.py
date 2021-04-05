# -*- coding: utf-8 -*-
from qgis.core import QgsPoint, QgsCoordinateTransform, QgsCoordinateReferenceSystem, QgsGeometry, QgsRectangle, QgsProject
from qgis.PyQt.QtGui import QColor
from qgis.gui import QgsVertexMarker

class geometryHelper(object):
    """Several tools to modify geometry etc.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    
    def __init__(self , iface ):
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.adreslayerid = ''
    
    @staticmethod
    def getGetMapCrs(iface):
        """Get CRS of the current mapCanvas.
        
        :param iface: A QGIS interface instance.
        :type iface: QgsInterface
        :return:  QgsCoordinateReferenceSystem of the current mapCanvas."""
        return iface.mapCanvas().mapSettings().destinationCrs() 
        
    def prjPtToMapCrs( self, xy , fromCRS=4326 ):
        """Project point xy form fromCrs to the CRS of mapCanvas.
        
        :param xy: a QGSpoint object
        :param fromCRS: the CRSid of xy
        :return: QGSpoint in the CRS of mapCanvas.
        """
        fromCrs = QgsCoordinateReferenceSystem(fromCRS)
        toCrs =   self.iface.mapCanvas().mapSettings().destinationCrs() 
        xform =   QgsCoordinateTransform( fromCrs, toCrs, QgsProject.instance() )
        return    xform.transform( xy[0], xy[1] )
    
    def prjPtFromMapCrs( self, xy , toCRS=31370 ):
        """Project point xy from the CRS of mapCanvas to toCrs.
        
        :param xy: a QGSpoint object
        :param toCRS: the CRSid of xy
        :return: QGSpoint in toCRS.
        """
        toCrs = QgsCoordinateReferenceSystem(toCRS)
        fromCrs = self.iface.mapCanvas().mapSettings().destinationCrs() 
        xform = QgsCoordinateTransform( fromCrs, toCrs, QgsProject.instance() )
        return   xform.transform( xy[0], xy[1] )

    def prjLineFromMapCrs(self, lineString, toCRS=4326 ):
        """Project lineString from the CRS of mapCanvas to toCrs.
        
        :param xy: a QGSgeometry object, must be a line
        :param toCRS: the CRSid of xy
        :return: QgsGeometry in toCrs
        """
        fromCrs = self.iface.mapCanvas().mapSettings().destinationCrs() 
        toCrs = QgsCoordinateReferenceSystem(toCRS)
        xform = QgsCoordinateTransform(fromCrs, toCrs, QgsProject.instance())
        wgsLine = [ xform.transform( xy ) for xy in  lineString.asPolyline()]
        return QgsGeometry.fromPolyline( wgsLine )

    def prjLineToMapCrs(self, lineString, fromCRS=4326 ):
        """Project lineString from  fromCRS to the CRS of mapCanvas.
        
        :param xy: a QGSgeometry object, must be a line
        :param toCRS: the CRSid of xy
        :return: QgsGeometry in toCrs
        """
        fromCrs = QgsCoordinateReferenceSystem(fromCRS)
        toCrs = self.iface.mapCanvas().mapSettings().destinationCrs() 
        xform = QgsCoordinateTransform(fromCrs, toCrs, QgsProject.instance() )
        if isinstance(lineString, QgsGeometry):
            wgsLine = [ xform.transform( xy ) for xy in  lineString.asPolyline()]
        if hasattr(lineString, '__iter__'):
            wgsLine = [ xform.transform( QgsPoint(xy[0], xy[1]) ) for xy in  lineString]
        return QgsGeometry.fromPolyline( wgsLine )

    def zoomtoRec(self, xyMin, xyMax , crs=None):
        """zoom to rectangle from 2 points with given crs, default= mapCRS
        
        :param xyMin: a QgsPoint of the left undercorner of the rectangle
        :param xyMax: a QgsPoint of the right uppercorner of the rectangle
        """
        if crs is None:
            crs = self.getGetMapCrs(self.iface)
            
        maxpoint = QgsPoint(xyMax[0], xyMax[1])
        minpoint = QgsPoint(xyMin[0], xyMin[1])
        
        pmaxpoint = self.prjPtToMapCrs(maxpoint, crs)
        pminpoint = self.prjPtToMapCrs(minpoint, crs)
        
        # Create a rectangle to cover the new extent
        rect = QgsRectangle( pmaxpoint, pminpoint )
    
        # Set the extent to our new rectangle
        self.iface.mapCanvas().setExtent(rect)
        # Refresh the map
        self.iface.mapCanvas().refresh()
    
    def zoomtoRec2(self, bounds, crs=None):
        """zoom to rectangle from a list containing: [xmin,ymin,xmax,ymax] with given crs, default= mapCRS
        
        :param bounds: a List in the form: [xmax, ymax, xmin, ymin].
        """
        if not bounds or len(bounds) != 4:
            return
        if crs is None:
            crs = self.getGetMapCrs(self.iface)
            
        maxpoint = QgsPoint( bounds[0], bounds[1])
        minpoint = QgsPoint( bounds[2], bounds[3])
        
        pmaxpoint = self.prjPtToMapCrs(maxpoint, crs)
        pminpoint = self.prjPtToMapCrs(minpoint, crs)
      
        # Create a rectangle to cover the new extent
        rect = QgsRectangle( pmaxpoint, pminpoint )
    
        # Set the extent to our new rectangle
        self.iface.mapCanvas().setExtent(rect)
        # Refresh the map
        self.iface.mapCanvas().refresh()
      
    def addPointGraphic(self, xy, color="#FFFF00", size=1, pen=10, markerType=QgsVertexMarker.ICON_BOX ):
        """create a point Graphic at location xy and return it
        
        :param xy: list in the form [x,y] or QgsPoint
        :param color: the color of the icon
        :param size: icon size in mm
        :param pen: outline width in mm
        :param markerType: the type of the form of the QgsVertexMarker: ICON_NONE, ICON_CROSS, ICON_X, ICON_BOX, ICON_CIRCLE, ICON_DOUBLE_TRIANGLE 
        :return: the created graphic (QgsVertexMarker)"""
        "create a point Graphic at location xy and return it"
        x, y = list( xy )[:2]
        m = QgsVertexMarker(self.canvas)
        m.setCenter(QgsPoint(x,y))
        m.setColor(QColor(color))
        m.setIconSize(size)
        m.setIconType(markerType) 
        m.setPenWidth(pen)
        return m
    
