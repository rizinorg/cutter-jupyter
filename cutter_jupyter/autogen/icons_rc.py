# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Mo. März 25 16:57:53 2019
#      by: The Resource Compiler for PySide2 (Qt v5.12.2)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x01\xae\
<\
!DOCTYPE svg  PU\
BLIC '-//W3C//DT\
D SVG 1.1//EN'  \
'http://www.w3.o\
rg/Graphics/SVG/\
1.1/DTD/svg11.dt\
d'>\x0a<svg style=\x22\
enable-backgroun\
d:new 0 0 32 32\x22\
 xmlns=\x22http://w\
ww.w3.org/2000/s\
vg\x22 xml:space=\x22p\
reserve\x22 height=\
\x2232px\x22 width=\x2232\
px\x22 version=\x221.1\
\x22 y=\x220px\x22 x=\x220px\
\x22 xmlns:xlink=\x22h\
ttp://www.w3.org\
/1999/xlink\x22 vie\
wBox=\x220 0 32 32\x22\
>\x0a\x09<path d=\x22m16 \
0l-16 16h4v16h24\
v-16h4l-16-16zm8\
 28h-6v-6h-4v6h-\
6v-14l8-6 8 5.7v\
14z\x22 fill=\x22#4d4d\
4f\x22/>\x0a</svg>\x0a\
"

qt_resource_name = b"\
\x00\x0e\
\x08\xb5\x90\xa2\
\x00c\
\x00u\x00t\x00t\x00e\x00r\x00_\x00j\x00u\x00p\x00y\x00t\x00e\x00r\
\x00\x08\
\x068W'\
\x00h\
\x00o\x00m\x00e\x00.\x00s\x00v\x00g\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x22\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
