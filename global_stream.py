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
This file has the global functions of the application
"""

class Global:
    
    def GlobalOutputStream(__cout):
        return print(__cout)
    
    def Global_InsertCommand(any):
        any()
        
        
def getGlobalObject( globaltype : Global ):
    return globaltype

def globalWriteOutputStream( stream : Global, out : str ):
    stream.GlobalOutputStream( out )