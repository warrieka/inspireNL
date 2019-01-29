
.. _Contribute:

Contributing and forking
========================

Compiling and running the plugin from code:
-------------------------------------------

You can find the lated version of the code on Github_. 

To modify the the code, you can clone the repo::

    git clone https://github.com/warrieka/inspireNL 
    cd inspireNL
    
To test and compile the code a Makefile is provided. There are different files for Linux and windows. Rename the version for you system to *Makefile* to make correct one active. 

In order to use this makefile you need to have a GNU-compatible shell with make installed and the QGIS-binaries and its python modules on the system PATH. The PyQT commandline tools should be part of your QGIS install, these are essential for compiling the plugin. On windows you can use MinGW and on Linux you just need to install the basic build-tools::

    sudo apt install build-essential 

Before use you need to edit the Makefile_ at line 25 and set PROFILE to the location of your QGIS userprofile. The default location on windows is *C:\Users\<username>\AppData\Roaming\QGIS\QGIS3\profiles\default* but you should make a separate devprofile. 

To compile the code you can type just make ass it is the default target or: ::

    make compile
    
To compile and deploy the compiled code to the PROFILE as a plugin::

    make deploy

To compile, deploy and start QGIS with PROFILE::

    make run
    
To delete the plugin under PROFILE::

    make derase
    
To delete compiled files from the codebase::

    make clean
  
The dclean target removes compiled python files from plugin directory::

    make dclean
    
The zip target deploys the plugin and creates a zip file with the deployed content. You can then upload the zip file on http://plugins.qgis.org to add this plugin to standard plugin-repo. This target requires *zip* to be on the PATH::

    make zip
    
The package target creates a zip package of all the code of the plugin named $(PLUGINNAME).zip of a specific version ofthe code for archiving purposes. THis is NOT the package you should upload to http://plugins.qgis.org.::
  
    make package VERSION=<VERSION NAME>
    
There are also commands for translations, but rigth now there is only one language supported: dutch. 

Modifing the code to target an other CSW:
-----------------------------------------

First Fork the code. 

The application was orignaly develloped to work against a specific version of geonetwork. Originaly it contained many non-stardard geonetwork specific requests. Starting from the version 2.x on the qgis3-branch, only standard OGC-services are used to query the server. 

To target another CSW-service, you wil need to modify the :ref:`metadataParser`. The minimal change will global variable **CSW_URL** that contains the full url of the csw-service up to the query string. For the NGR this is: http://www.nationaalgeoregister.nl/geonetwork/srv/dut/inspire . This Global can be fount at the top of the metadataParser.py file. 

You might have make specific changes for like for custom vendor parameters, custom thypes of services and application-schema's used etc. Normaly al these have to be made in the metadataParser Module. MDdata contains all the metadata-xml parsing, MDreader contains al the interactiing with the CSW. Their are functions for constructing requests to OGC W*S services and handling downloads. 

Rebranding can be done by changing the icons in the images folder. 

Contributing 
-------------

To upload your modifications, just edit the code commit and make a Pull-request_ on github. 
The orignal develloper will review and merge the edits if approved. 
    
.. _Github: https://github.com/warrieka/inspireNL
.. _Makefile: https://github.com/warrieka/inspireNL/blob/qgis3/Makefile#L25
.. _MinGW: http://www.mingw.org/
.. _Pull-request: https://help.github.com/articles/about-pull-requests/