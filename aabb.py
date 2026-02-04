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

class aabb_spawnable:
    aabb_scalar = vec3_t
    aabb_bounds = { 0, 1, 2, 3, 4, 5, 6, 7 } # points

def getAxisAllignedBoundingBox( aabb : aabb_spawnable ):
    return aabb

def getAABB_Bounds( aabb : aabb_spawnable )->float:
    return aabb.aabb_scalar

def getABBB_Points( aabb : aabb_spawnable )->int:
    return aabb.aabb_bounds
    