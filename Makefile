#/***************************************************************************
# inspireNL
#
# Datasets van de het Nederlandse Dataportaal Nationaal Georegister bevragen  
#							 -------------------
#		begin				: 2015-08-31
#		copyright			: (C) 2015 by KGIS
#		email				: kaywarrie@gmail.com
# ***************************************************************************/
#
#/***************************************************************************
# *																		 *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or	 *
# *   (at your option) any later version.								   *
# *																		 *
# ***************************************************************************/

# Add iso code for any locales you want to support here (space separated)
# default is no locales
LOCALES = nl

# CONFIGURATION
PROFILE=E:\work\devProfile

# translation
SOURCES = \
	__init__.py \
	inspireNL.py inspireNLabout.py dataCatalog.py

PLUGINNAME = inspireNL

PY_FILES = \
	__init__.py settings.py \
	inspireNL.py inspireNLabout.py dataCatalog.py geometryhelper.py metadataParser.py

UI_FILES = ui_inspireNL_dialog.py ui_dataCatalog_dialog.py

EXTRAS = metadata.txt images

RESOURCE_FILES = resources_rc.py

PLUGIN_UPLOAD = $(c)/scripts/plugin_upload.py

QGISDIR=.qgis2

default: compile

compile: $(UI_FILES) $(RESOURCE_FILES) 

%_rc.py : %.qrc
	pyrcc5 -o $*_rc.py  $<

%.py : %.ui
	pyuic5  --import-from=. -o $@ $<

run: deploy
	qgis --profiles-path $(PROFILE)

# The deploy  target only works on unix like operating system where
# [KW]: use "make runplugin" instead on windows
deploy: derase compile
	rm -rf $(PROFILE)\profiles\default\python\plugins\$(PLUGINNAME) 
	mkdir $(PROFILE)\profiles\default\python\plugins\$(PLUGINNAME)
	cp -vfr $(PY_FILES) $(PROFILE)\profiles\default\python\plugins\$(PLUGINNAME)
	cp -vf $(UI_FILES) $(PROFILE)\profiles\default\python\plugins\$(PLUGINNAME)
	cp -vf $(RESOURCE_FILES) $(PROFILE)\profiles\default\python\plugins\$(PLUGINNAME)
	cp -vfr $(EXTRAS) $(PROFILE)\profiles\default\python\plugins\$(PLUGINNAME)
	cp -vfr i18n $(PROFILE)\profiles\default\python\plugins\$(PLUGINNAME)


# The dclean target removes compiled python files from plugin directory
# also deletes any .git entry
dclean:
	find $(PROFILE)\profiles\default\python\plugins\$(PLUGINNAME) -iname "*.pyc" -delete
	find $(PROFILE)\profiles\default\python\plugins\$(PLUGINNAME) -iname ".git" -prune -exec rm -Rf {} \;


derase:
	rm -Rf $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)

zip: deploy 
	# The zip target deploys the plugin and creates a zip file with the deployed
	# content. You can then upload the zip file on http://plugins.qgis.org
	rm -f $(PLUGINNAME).zip
	cd $(PROFILE)\profiles\default\python\plugins; zip -9r $(CURDIR)\$(PLUGINNAME).zip $(PLUGINNAME)

package: compile
	# Create a zip package of the plugin named $(PLUGINNAME).zip.
	# This requires use of git (your plugin development directory must be a
	# git repository).
	# To use, pass a valid commit or tag as follows:
	#   make package VERSION=Version_0.3.2
	rm -f $(PLUGINNAME).zip
	git archive --prefix=$(PLUGINNAME)/ -o $(PLUGINNAME).zip $(VERSION)
	echo "Created package: $(PLUGINNAME).zip"

transup:
	@chmod +x scripts/update-strings.sh
	@scripts/update-strings.sh $(LOCALES)

transcompile:
	@chmod +x scripts/compile-strings.sh
	@scripts/compile-strings.sh lrelease $(LOCALES)

transclean:
	rm -f i18n/*.qm

clean:
	rm $(UI_FILES) $(RESOURCE_FILES)

