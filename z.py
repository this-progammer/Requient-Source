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

ZOUTLINE_BUF = 0x00
ZOUTLINE_SELBUF = 0x01

class Z:
    zBuffer = [].count( 2048 )
    bDoDirty = bool
    zRow = int
    zColumn = int