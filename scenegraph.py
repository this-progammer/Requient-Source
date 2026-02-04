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

import mathvec

WORLD_MAX = mathvec.vec3_t = { 9999.0, 9999.0, 9999.0 }
WORLD_MIN = mathvec.vec3_t = { -9999.0, -9999.0, -9999.0 }

class SceneGraph:
    mode = int
        
def getSceneGraph( scene : SceneGraph ):
    return scene