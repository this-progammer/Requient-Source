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

#point.py

from mathvec import*
import sys

class ClipPoint:
    point = int
    m_bPlaced = int
    position = vec3_t
    
def getPoint( point : ClipPoint ):
    return point
    
def Alloc_Point():
    p = ClipPoint
    sys.getsizeof( [p] )
    getPoint( p )
    
    return p
    
def getPointOrigin( point : ClipPoint )->float:
    return point.position