# -*- coding: utf-8 -*--
""" 
*An QGIS plugin to search and add Datasets of the Dutch Dataportal 'Nationaal Georegister' to QGIS.*
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    from .inspireNL import inspireNL
    return inspireNL(iface)
