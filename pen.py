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
    pen tool is used for the workzone and grid
    for drawing shapes and pen color
"""

class Pen:
    #pen RGB aka color
    penColor = tuple[0.0, 0.0, 0.0]
    
class WorkzonePen:
    workzoneDrawpen = Pen()
    
class BrushPen:
    brushPen = Pen()
    
    
def getPen( pen : Pen ):
    return pen

def getPenColor( pen : Pen )->float:
    return pen.penColor

def getWorkzonePen( pen : WorkzonePen ):
    return pen

def directWorkzonePenDraw( pen : WorkzonePen ):
    return pen.workzoneDrawpen

def getBrushPen( pen : BrushPen ):
    return pen

def directBrushPenDraw( pen : BrushPen ):
    return pen.brushPen
