Notas
====

Update april 2021
----------------

Vraag: Er wordt opmerkt dat de plugin niet goed werkt achter een proxy. 

Hier voorbeeld code zoals ik in een project de geocodeer service aanroep om daarmee uiteindelijk adressen van een locatie te voorzien:

```python
proxieLijst={
            "http":"http://<server>:<poort>",
            "https":"http://<server>:<poort>"
}
strUrl = "http://geodata.nationaalgeoregister.nl/locatieserver/v3/free"
postdata = {
    "fq": "type:adres",
    "q": "postcode:3521BJ AND woonplaatsnaam:Utrecht AND straatnaam:Croeselaan AND huis_nlt:15",
    "rows": 1
}
resp = requests.post(strUrl, proxies=proxieLijst, data=postdata)
```

WMTS QGIS uri's
----
contextualWMSLegend=0
crs=EPSG:31370
dpiMode=7
featureCount=10
format=image/png
layers=P_Publiek_P_basemap
styles=default
tileMatrixSet=default028mm
url=http://geodata.antwerpen.be/arcgissql/rest/services/P_Publiek/P_basemap/MapServer/WMTS/1.0.0/WMTSCapabilities.xml


contextualWMSLegend=0
crs=EPSG:31370
dpiMode=7
featureCount=10
format=image/png
layers=grb_bsk_gr
styles=default
tileMatrixSet=BPL72VL
url=http://grb.agiv.be/geodiensten/raadpleegdiensten/geocache/wmts/?SERVICE%3DWMTS%26VERSION%3D1.0.0%26REQUEST%3DGetCapabilities

WMS uri's
----

crs=EPSG:25831
dpiMode=7
format=image/png
layers=Boringen
styles=
url=https://www.dov.vlaanderen.be/geoserver/dov-pub/Boringen/ows?


Fetch  WMS 2.0 through ogr2ogr
-------
ogr2ogr --config OGR_WFS_PAGING_ALLOWED --config OGR_WFS_PAGE_SIZE 1000 YES -f GEOJSON ProtectedSite.json "WFS:http://services.inspire-provincies.nl/ProtectedSites/services/download_PS" ps:ProtectedSite
