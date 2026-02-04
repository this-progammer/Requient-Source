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

from plane3 import*

"""*GET THE NORMAL OF A PLANE*"""
def cross_product( va, vb, vc )->float:
    vc[0] == va[1] * vb[2] - va[2] * vb[1]
    vc[1] == va[2] * vb[0] - va[0] * vb[2]
    vc[2] == va[0] * vb[1] - va[1] * vb[0]
    return vc, vb, va