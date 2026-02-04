####################################################################
#
#   Application : MaxArm ESP32 Tools
#   
#   Add : Praise the Lord, not me
#
#   Programmer : Hunter M.
#
#   Use Of Code : This code is to write Software to control ESP32 MaxArm Robot, intended for, New Prairie High School
#
####################################################################

from brush import*
from brushcreationtool import*
from camwnd import*
from qesmatictypes import*
from pen import*


# the zone brushes are in
class Workzone:
    sel_zone = vec3_t # x, y, z
    workzone_brush = Brush()
    
# returns a zone
def getWorkzone(zone : Workzone):
    return zone

# returns a zones area
def getWorkzoneMatrix(zone : Workzone)->float:
    return zone.sel_zone

def getWorkzoneBrush( zone : Workzone ):
    return zone.workzone_brush

def EventW(zone : Workzone, T : int ):
    return T

#######################
#   set mins and maxs, used for XY and Viewport
#
def SetWorldZoneBounds( zone : Workzone, MIN : float, MAX : float ):
    i = int