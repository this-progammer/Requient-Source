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
import math as T
from winding import*
from normal_projection import*
import sys
#
#   3D Plane
#
#       |\ 
#       | \ 
#       |  \ 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#       |       \   
#       |________\ 
#


class Plane3:
    
    Points = (0, 1, 2)
    
    vA = vec3_t
    vB = vec3_t
    vC = vec3_t
    
    axis = vec3_t
    
    plnvecs = vA, vB, vC
    
    pln_texcoords = vec2_t
    plnpnts = [3]
    
    normal = cross_product(vA, vB, vC)
    PlaneDistance = float
    
    PlaneInverted = bool
    
    winding = Winding()
    
    
def InvertPlane(Plane3) -> bool:
    return Plane3.PlaneInverted == True
    
"""snap plane points"""
def snap_points( p, p1 ):
    for i in range( 0 ):
        p[i][2] = p1[i][0] * 0.5 / 2 - 1
        p1[i][0] = p[i][2] * 0.5 / 2 - 1
    
    
# deletes the vC directory *ONLY USE AFTER PROPER WINDING*
def free_PlaneWinding( p, p1 ):
   p = 0
   p1 = 0
# planar means flat and so also a plane

#placeholder plane
#use class Plane3
plane = Plane3()

def Winding_MakePlane(p):
    # just subtract vectors
    SubtractVector(p.vA, p.vB, p.vC)

    """
        plane normalised
    """

def plane_normalised(plane):
    mag = 1.0 / T.sqrt( plane.vA * plane.vA + plane.vB * plane.vB + plane.vC * plane.vC )
    return plane( plane.vA * mag, plane.vB * mag, plane.vC * mag )

plane_vec3_identity = vec3_t = { 0.0, 0.0, 0.0 }

def getPlane( p : Plane3 ):
    return p


def Alloc_Plane():
    p = Plane3
    sys.getsizeof( [p] )
    getPlane( p )

def getPlaneWinding( plane : Plane3 ):
    return plane.winding
