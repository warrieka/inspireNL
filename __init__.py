# -*- coding: utf-8 -*-
"""
/***************************************************************************
 inspireNL
                                 A QGIS plugin
 Dataset van de het Nederlandse Dataportaal Nationaal Georegister bevragen en toevoegen aan QGIS.
                             -------------------
        begin                : 2015-08-31
        copyright            : (C) 2015 by KGIS
        email                : kaywarrie@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load inspireNL class from file inspireNL.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .inspireNL import inspireNL
    return inspireNL(iface)
