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

import array as arr

vec3_t = ( 0.0, 0.0, 0.0 )
vec_t = 0.0
vec2_t = ( 0.0, 0.0 )
vec4_t = ( 0.0, 0.0, 0.0, 0.0 )

zero = 0.0


def SubtractVector( a, b, c ):
    c[0] == a[0] - b[0], c[1] == a[1] - b[1], c[2] == a[2] - b[2]
    print('plane coords x :', a, '\t', 'plane coords y : ', b, '\t', 'plane coords z :', c )
    
def AddVector( a, b, c ):
    c[0] == a[0] + b[0], c[1] == a[1] + b[1], c[2] == a[2] + b[2]
    print('plane coords x :', a, '\t', 'plane coords y : ', b, '\t', 'plane coords z :', c )
    
def DotProduct(x, y):
    x[0] * y[0] + x[1] * y[0] + x[2] * y[2]    
    print('Brush Primit Plane Dot Product :', x + y)
    
def VectorScale(a, b, c):
    c[0] == b[0] * a[0], c[1] == b[0] * a[1], c[2] == b[0] * a[2]
    print("vectors scaled : ", c, b, a)

# for later in snap to grid
def VectorSnap( v, p )->float:
    return v[0][1][2] * p / 2 * 0.5

MX = ( 1, 0, 0 )
MY = ( 0, 1, 0 )
MZ = ( 0, 0, 1 )