Changelog
=========

Version 2.8
-----------
- Added a new class to read metadata records in xml. 

Version 2.7
-----------
- Refactored to make http-calls through QNetWork_ and QgsBlockingNetworkRequest_ instead of urllib.request, so QGIS proxy-settings will be used. 

Version 2.6
-----------
- Production release

Version 2.5
-----------
- Further improved WFS with exotic CRS
- Improved Download-function: no longer use webbrowser.
- Changed some maessages a request of customer

Version 2.4
-----------
- Improved WFS CRS handling including working with inverted axis.
- User notificaton improvements.
- Spell fixes. 

Version 2.3
------------
- Option to download WFS instead  of loading as a service.
- Handle complex features in WFS better. 
- Various small bugfixes as reported by users.
- Improved documentation. 

Version 2.2
-----------
- Created a documentation project based on http://www.sphinx-doc.org

Version 2.1
-----------
- All search qeuries now use LIKE instead = as this yields more complete results, searches no longer cases sensitive. 
- Various small bugfixes as reported by users.
- Improved support for WFS 2.0 


Version 2.0 
-----------
The largest change in this version is the migration to QGIS3. 

In addition to the migration to QGIS3 / Python3 / QT5, the following issues have been improved.

- CSW: The geonetwork services are nowhere used anymore, everything is CSW/OGC based.
- Keywords are now a autocomplete on the search text instead of a dropdown.
- Download: Can now handle ATOM links with multiple entries. You get when there are several, a dropdown with titles of the various entries. The link is opened in a web page. That is the easiest way to handle that download. Possibly I can still replace this with a "save as" dialog, the disadvantage of this is that you also save the error messages and such if the link is no longer correct.
- WFS: WFS 2.0 is now also supported.
- WCS: Several improvements have been made, but you continue to bump into the limitations of that service.
    - AHN services work but are often slow due to the large quantity that needs to be downloaded.
    - The Bathymetrie Nederland service does not work, they are not compatible with QGIS. You can not add that service via the standard method.
- Networking, reverse network proxy is used if present. The plug-in will now also work on some corporate networks with high security.

.. _QNetWork: https://doc.qt.io/qt-5/qtnetwork-index.html
.. _QgsBlockingNetworkRequest: https://qgis.github.io/pyqgis/3.16/core/QgsBlockingNetworkRequest.html
