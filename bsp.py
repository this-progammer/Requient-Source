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

BSP_LEAF_NODE = 0x01

class Bsp:
    
    # BspBrushCount = int = [], use brush list instead
    BspFaceCount = [int]
    BspPlaneCount = [int]
    
def getRequientBsp( bsp : Bsp ):
    return bsp

def getBspFaceLeafCount( bsp : Bsp )->int:
    return bsp.BspFaceCount

def getBspPlaneLeafCount( bsp : Bsp )->int:
    return bsp.BspPlaneCount
    