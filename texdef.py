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
import sys
from PyQt5.QtWidgets import*

class Texdef:
    texcoords = (0.0, 0.0, 0.0, 0.0)
    bScale = bool
    shadername = str
    
    def getShader(_shader)->str:
        return _shader
    
    def getCoords(_coords)->float:
        return _coords
    
    def getScaleMode(_scalemode)->bool:
        return _scalemode == True
    
def getTexdefWrapper( texdef : Texdef ):
    return texdef

def Alloc_Texdef():
    t = Texdef
    sys.getsizeof( [t] )
    getTexdefWrapper( t )
    
    return t
    
def callTexdefAllocation():
    Alloc_Texdef()
    
def getTexdefCoordsMemeber( texdef : Texdef ):
    texdef.getCoords()
    
def getTexdefScalableMember( texdef : Texdef ):
    texdef.getScaleMode()
    
def getTexdefShaderMember( texdef : Texdef, shader : str ):
    texdef.getShader() == shader
    
def getTexdefCoords( texdef : Texdef )->float:
    return texdef.texcoords

def getTexdefScalable( texdef : Texdef )->bool:
    return texdef.bScale == True

def getTexdefShader( texdef : Texdef, shader : str )->str:
    return texdef.shadername == shader

class TextureWnd(QDialog):
    m_nX = 50
    m_nY = 50
    m_nW = 600
    m_nH = 600
    
    m_nTexImgW = 30
    m_nTexImgH = 30
    
    m_bPopup = bool
    
    m_selected_texture = [Texdef()]
    
    def sel_texture( self, texture : Texdef ):
        return texture.getShader()
        
            
    def PopulateTextureDirectory(self, dir : str):
        pass
