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
    

# get a box
def getBrushBox( box : BrushBox ):
    return box

def getBrushBoxPoints( box : BrushBox )->int:
    return box.boxpoints

def getBrushBoxMins( box : BrushBox )->float:
    return box.boxmins

def getBrushBoxMaxs( box : BrushBox )->float:
    return box.boxmaxs

# todo : finish later!
def brushBoxCreate( box : BrushBox, mins : float, maxs : float ):
    pnts = box.boxpoints
    mins = box.boxmins
    maxs = box.boxmaxs
    bBackwards = bool # is the box backwards, if so then no
    
    pnts[0] = maxs[0], pnts[1] = maxs[1]
    pnts[2] = maxs[2], pnts[3] = maxs[3]
    pnts[4] = mins[0], pnts[5] = mins[1]
    pnts[6] = mins[2], pnts[7] = mins[3]
    
    if maxs < mins:
        print("Error : Brush Box is backwards")
        bBackwards = True


    
    

