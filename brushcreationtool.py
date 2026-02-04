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

"""
 Brush Creation Tool
 similar functions to this in other files
"""

from brush import*

class BrushCreationTool(Brush):
    brushCreationId = int
        
def getBrushCreationToolHandle( tool : BrushCreationTool ):
    return tool