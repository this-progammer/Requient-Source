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

from mathvec import*

# this brush does not use the winding class
class BrushBox:
    boxpoints = [8]
    boxmidpoint = 1
    boxmins = vec3_t
    boxmaxs = vec3_t
    box_wrapper = bool

globalBoxManager = BrushBox

# get a box
def getBrushBox( box : BrushBox ):
    return box

def getBrushBoxPoints( box : BrushBox )->int:
    return box.boxpoints

def getBrushBoxMins( box : BrushBox )->float:
    return box.boxmins

def getBrushBoxMaxs( box : BrushBox )->float:
    return box.boxmaxs



    
    

