# -*- coding: utf-8 -*--
""" 
*An QGIS plugin to search and add Datasets of the Dutch Dataportal 'Nationaal Georegister' to QGIS.*

**About the Dutch INSPIRE QGIS plugin**

In the context of INSPIRE, the European member states are realizing a digital network for the exchange of data on the living environment. INSPIRE ensures that this geo-information is of good quality and that its content, even across national borders, is coordinated. In the Netherlands, descriptions of more than 200 INSPIRE datasets and approximately 265 associated services are now available in the National Georegister (http://www.nationaalgeoregister.nl/).

To facilitate the use of INSPIRE data for the professional GIS users in the Netherlands, a plugin has been developed for QGIS. This plugin makes it easy to find, consult and download the INSPIRE datasets and services directly via the National Georegister. Through the plugin, a user can search INSPIRE data by keyword, INSPIRE theme, organization or type of service and add the result directly to QGIS.

The INSPIRE QGIS plugin was created under the responsibility of Geonovum. Geonovum supports the Ministry of the Interior and Kingdom Relations and data providers with the introduction of INSPIRE in the Netherlands. The plugin has been developed by KGIS (http://kgis.be/).

If you have any questions about INSPIRE or the plugin, please visit https://www.geonovum.nl/geo-standaarden/inspire-europese-leefomgeving or submit them to the INSPIRE helpdesk (inspire@geonovum.nl).

"""

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    from .inspireNL import inspireNL
    return inspireNL(iface)
