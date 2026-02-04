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
#grklib.py

vec3 = [0.0, 0.0, 0.0]
dist = float

NULL = 0

def get_vec(vec3):
    assert(vec3)


def grkBegin(any):
    any()

def grkEnd(any):
    any()


class Grk():
    bits = 16
    pixels = 32
    fragcolor = 86
    depth = 164
    fov = 120
    graphicview = str

    def Line(vec3, fragcolor):
        grkBegin(vec3)
        grkBegin(fragcolor)
        grkEnd(fragcolor)
        grkEnd(vec3)