## Process this file with automake to produce Makefile.in
## Created by Anjuta


uidir = $(pkgdatadir)/ui
ui_DATA = textcrypt.ui


## The main script
bin_SCRIPTS = textcrypt.py

## Directory where .class files will be installed
textcryptdir = $(pythondir)/textcrypt


textcrypt_PYTHON = \
	textcrypt.py


EXTRA_DIST = $(ui_DATA)


# Remove ui directory on uninstall
uninstall-local:

	-rm -r $(uidir)

	-rm -r $(pkgdatadir)
