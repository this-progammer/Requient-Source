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

"""queuedraw.py"""

from face import*
from plane3 import*
from OpenGL.GL import*

"""face draw"""
def Queue_DrawFace( f : Face ):
    w = f.winding
    j = int
    
    for j in range( 4 ):
        glBegin( GL_POLYGON )
        glVertex3fv( w.wfpnts[4][j] )
        glEnd()
    
def glREQDrawPlane( plane : Plane3 ):
   return
    
def glREQDrawFace( face : Face ):
   Queue_DrawFace( face )
   