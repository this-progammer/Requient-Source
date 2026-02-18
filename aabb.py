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
    box_mins = vec3_t
    box_maxs = vec3_t

globalAABBManager = aabb_spawnable

def getAxisAllignedBoundingBox( aabb : aabb_spawnable ):
    return aabb

def getAABB_Bounds( aabb : aabb_spawnable ):
    aabb.aabb_bounds

def getABBB_Points( aabb : aabb_spawnable ):
    return aabb.aabb_bounds

def boxDoCreation( box : aabb_spawnable, mins : float, maxs : float, bounded : bool ):
    mins = box.box_mins
    maxs = box.box_maxs
    box_center = tuple((max_val + min_val) / 2.0 for max_val, min_val in zip(maxs, mins))
    box_size = tuple(max_val - min_val for max_val , min_val in zip(maxs, mins))
    box_radius = tuple((max_val - min_val) / 2.0 for max_val, min_val in zip(maxs, mins))

    return box