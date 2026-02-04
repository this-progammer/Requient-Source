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

from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import Qt
from OpenGL.GL import*
from OpenGL_accelerate import*
from face import*
from plane3 import*
from texdef import*
from node import*
from entity import*
from scenegraph import*

class MapDocument:
    mapDocName = str
    
    m_pFaces = Face()
    m_pPlane = Plane3()
    m_pTexdef = Texdef()
    m_pNodes = Node()
    m_pEntities = EntityWorldClass()
    m_pBrushes = any
    
    m_fMapWorldCoord = 9999.0
    
    # check for nonviscol brushes, brushes that have degenerate collision or visibility
    m_bChckNoviscolSelBrushes = bool
    
    bSaved = bool
    
    # for an robotic app shouldnt be more than 10, lol ( jk )
    MAX_BRUSH_COUNT = 9999
    MAX_FACE_COUNT = 59994 # MAX_BRUSH_COUNT * 2
    
    def WriteBrushFormat( m_Brush : any ):
        print()
        
    def WriteFaceFormat(m_pFaces : Face):
        print()
        
    def WritePlaneFormat(m_pPlanes : Plane3):
        print()
        
    def WriteBrushPrimitTexdefFormat(m_pTexdef : Texdef):
        print()
        
    def WriteNodeFormat(m_pNode : Node):
        print()
        
    def WriteEntityFormat(m_pEntity : EntityWorldClass):
        print()
        
    
    
        
def getMapDocument( map : MapDocument ):
    return map 


#===============================
#=  Map Checking Functions
def Map_DoPlaneCheck( map : MapDocument, plane : Plane3 ):
    # check if any map planes are degenerate
    
    bPlnDegenerate = bool

    plane = map.m_pPlane
    
    if plane == 0:
        return

    if plane.normal == 0:
        print("Map %s : has planes with no normals... %p\n", map.mapDocName, plane)
        bPlnDegenerate = True
        del plane
        
    if plane.Points != 3:
        print("Map %s : has plane with non correct numbered points... %p\n", map.mapDocName, plane)
        bPlnDegenerate = True
        del plane
        
    if plane.plnvecs != 9:
        print("Map %s : has plane with incorrect vectors... %p\n", map.mapDocName, plane)
        bPlnDegenerate = True
        del plane
        
def Map_DoFaceCheck( map : MapDocument, face : Face ):
    # check if map faces are degenerate
    
    bFaceDegenerate = bool
    face = map.m_pFaces
    
    if face == 0:
        return
    
    if face.planes == 0:
        print("Map %s : face %p has invalid planes", map.mapDocName, face)
        del face