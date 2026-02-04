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

from mathvec import *

matrix_mdl = ( MX, MY, MZ )

"""
    m4x4 model
    
    x(1, 0, 0, 0)
    y(0, 1, 0, 0)
    z(0, 0, 1, 0)
     (0, 0, 0, 1) scale   
"""
