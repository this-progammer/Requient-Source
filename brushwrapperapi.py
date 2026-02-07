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

# brush wrapper api

from matrix import*

class BrushWrapperAPI:
    
    def WrapBrush( m_brush ):
        return m_brush
    
    def BrushWrapper( m_brush, m_wrapper ):
        return m_brush, m_wrapper
    
    def IncrementBrushWrapper( m_brush ):
        return ++m_brush
    
    def DecrementBrushWrapper( m_brush ):
        return --m_brush
    
def getBrushWrapperAPIModule( api : BrushWrapperAPI ):
    return api
