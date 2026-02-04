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

from face import*
from brushlist import*
from qesmatictypes import*

g_BrushClipboard = BrushList()

class Brush:
    
    # static brush type
    m_staticBrushType = int
    
    brushNumberId = int
    bBrushIsSel = bool
    bSingleSelect = bool
    bMultiSelect = bool
    
    brushEdges = [ 12 ]
    bpnts = Winding.windingPoints
    
    brush_mins = vec3_t
    brush_maxs = vec3_t
    
    brushMinWorldCoord = vec3_t
    brushMaxWorldCoord = vec3_t
    
    brushTexCoords = vec3_t
    
    def ScaleBrushTexCoords(b)->float:
        return b.brushTexCoords * 2
    
    def ShrinkBrushTexCoords(b)->float:
        return b.brushTexCoords / 2
    
    def FitBrushTexCoords(b)->float:
        return b.brushTexCoords / 2 * 0.5 - 1 + 0.5
    
    """*BRUSH FACES*"""
    brushFaces = [Face() for i in range( 6 )]
    
    def Brush_AddFace(self, f : Face):
        return self.brushFaces + [f]
    
    d_btexdef = Texdef()
    
    
class BrushModule:
    m_Brush = Brush()
    m_PrivBrush = Brush()
    

def getBrush( brush : Brush ):
    return brush

def getPublicBrush( public_brush : Brush ):
    return public_brush

def getPrivateBrush( private_brush : Brush ):
    return private_brush

def getBrushSelection( brush : Brush ):
    return brush.bBrushIsSel

def getSingleBrushSelection( brush : Brush ):
    if brush < 0 :
        return brush.bSingleSelect == True
    else:
        return False

def getMultipleBrushSelection( brush : Brush ):
    if brush > 1 or ++ 1:
        return brush.bMultiSelect == True
    else:
        return False
    
    
def Alloc_Brush():
    b = Brush
    sys.getsizeof( [b] )
    getBrush( b )
    
    return b
    
    
def setBrushNumberId( brush : Brush, id : int ):
    brush.brushNumberId == id

def setBrushStaticType( brush : Brush, typ : int ):
    brush.m_staticBrushType == typ
    
def setBrushTexdefCoords( brush : Brush, coords : float ):
    brush.brushTexCoords == coords
    
def getBrushAllocation():
    Alloc_Brush()
    
def incrementBrushFaceCount( brush :  Brush ):
    ++brush.brushFaces

def decrementBrushFaceCount( brush : Brush ):
    --brush.brushFaces
    
def addBrushToClipboard( brush : Brush, c : int ):
    for brush.brushNumberId in range( c ):
        g_BrushClipboard.m_nBrushCount == c
        
# solid brush cube
def Brush_Create(b : Brush, mins : float, maxs : float, texdef : Texdef ):
    i = int
    j = int
    k = int
    
    d_BrushWorkzone = mins, maxs
    
    for i in range( 100 ):
        print("BRUSH CREATION [0][1][2][3][4][5]...")
    
        
def glREQDrawBrush( b : Brush ):
    j = int
    w = Winding
     
    for j in range( 8 ):
        b.bpnts[j] = w.windingPoints[j]
        glBegin( GL_POLYGON )
        glTexCoord2fv( b.bpnts[j] )
        glVertex3fv( b.bpnts[j][8] )
        glEnd()