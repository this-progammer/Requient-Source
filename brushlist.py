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
"""*brushlist.py*"""

from worldspawn import*

class BrushList:
    
    m_nBrushCount = int
    m_bBrushEmpty = bool # is the brush list
    
    
def getBrushList( list : BrushList ):
    return list

def getBrushListCount( list : BrushList )->int:
    return list.m_nBrushCount

def getBrushListEmptyStatus( list : BrushList )->bool:
    return list.m_bBrushEmpty == True

def incrementBrushListCount( list : BrushList )->int:
    return ++list.m_nBrushCount

def decrementBrushListCount( list : BrushList )->int:
    return --list.m_nBrushCount