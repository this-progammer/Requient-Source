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
"""brush_primit.py"""

from mathvec import*
from brush import*
from aabb import*
from texdef import*

BRUSH_PRIMIT_VERSION = "1.0.0"
BRUSH_PRIMIT_MAJOR = "Brush"

class BrushNode:
    m_BrushNodePtr = Brush() # constructed
    m_BrushNodePtrNull = Brush # not constructed
    
    brushNodeId = int
    
    brushNodeMins = vec3_t
    brushNodeMaxs = vec3_t
    brushNodePoints = [8]

    def getBrushNode( self ):
        return self.m_BrushNodePtr
    
    def getBrushNodeNull( self ):
        return self.m_BrushNodePtrNull
    
    def createBrushNode():
        pass

class BrushNodeList:
    m_BrushNodes = [BrushNode()]
    brush_node_count = int
    b_brush_node_count_zero = bool
    
    def brushNodeListAdd( self, node : BrushNode ):
        for node in self:
            node.m_BrushNodePtr.brushNumberId = ++self.brush_node_count
            print( "Brush Node List Count %i", node.m_BrushNodePtr.brushNumberId )
            addBrushToClipboard( node.m_BrushNodePtr, self.brush_node_count )
            
    def brushNodeListPop( self, node : BrushNode ):
        for node in self:
            node.m_BrushNodePtr.brushNumberId == --self.brush_node_count
            #decrementBrushListCount()
            del ( node )

    def brushNodeListClean( self ):
        self.m_BrushNodes == 0
        del ( self.m_BrushNodes )
        return ( self( 0 ) )
    
    # if fails create new list
    def brushNodeListFail( self ):
        if self : assert( -1 ), next( self ) == sys.getsizeof( self, 0 )
            
            
#============================================
#       *BRUSH_ITERATOR*
class BrushIterator:
    
    brushIteratorId = int
    
    def BrushIteratorBegin( brush : Brush ): pass
    def BrushIteratorEnd( brush : Brush ): pass
    
    
class BrushSelectionIterator:
    
    m_SelBrush = Brush
    m_SelBrushes = [Brush()]
    
    # brush selection color
    brush_selection_color = COLOR_SELBRUSHES
    
    # selection brush ray trace test
    selection_trace_ray = vec3_t
    
    brushSelectionIteratorId = int
    brushSelectionItearatedSuccessfully = bool
    brushSelectionIteratorIsGlobal = bool # only if d_gBrushMode
    iteratorSelectBrush = bool
    
    def BrushSelectionIteratorBegin( brush : Brush ): pass
    def BrushSelectionIteratorEnd( brush : Brush ): pass

class BrushSelectionList:
    m_SelBrushIterator = BrushSelectionIterator
    selectedBrushNumbers = int
    popSelectedBrushes = bool
    
class BrushAxisAllignedBoundingBox:
    m_BrushProject = Brush
    m_BrushesPrjct = [Brush()]

    xy = vec3_t
    xz = vec3_t
    yz = vec3_t
    
    VIEWTYPE = int
    POINTS = [ArrayDatatype]
    
    d_aabb_gl_window = QOpenGLWidget

    mins = vec3_t
    maxs = vec3_t
    
    scale_aabb = bool
    aabb_scaled_transformed_rotated = bool
    
    select_abbb = bool
    aabb_selected = bool

    def createAxisAllignedBoundingBox(): pass
    
    
class BrushTable:
    m_BrushNodes = [BrushNode()]
    m_BrushesTree = [Brush()]
    
    REQ_MAX_BRUSH_COUNT = 9999
    
    max_brush_table_count = REQ_MAX_BRUSH_COUNT
    
    def AddBrushNodeToTable( self, node : BrushNode ): pass
    def AddBrushToTable( self, brush : Brush ): pass
    def PopBrushNodeFromTable( self, node : BrushNode ): pass
    def PopBrushFromTable( self, brush : Brush ): pass
    
    def getBrushTable( self ):
        return( self )
    
    
class BrushFace:
    m_Brush = Brush
    m_BrushFace = Face
    m_BrushFaces = [Face()]
    
    max_brush_face_count = 36
    
    brush_exceeds_max_faces = bool
    
    def senderNewFace( self, brush : Brush, face : Face ):
        brush = self.m_Brush
        face = self.m_BrushFaces
        
        if brush and face : assert( 0 or -1 ), Brush() == Alloc_Brush( [ brush ] ) and Face() == Alloc_Face( [face] )
        else:
            True and brush != 0
            
        for face in brush:
            brush.Brush_AddFace( face )       
        
        return self
    
    def senderMaxCount( self, brush : Brush, face : Face )->bool:
        if brush.brushFaces > self.max_brush_face_count:
            print("Brush has To Many Faces! INVALID BRUSH!\n")
            for brush.brushFaces in self:
                --brush.brushFaces <= 36
#=====================
#   Globals
g_nBrushId = int

#=======================================
#   TexdefFlagPrimit_Clip()
def TexdefFlagPrimit_Clip( brush : Brush, flag : Texdef ):
    if brush == 0 or -1:
        return
    callTexdefAllocation()
    brush.d_btexdef = flag.getShader() == Requient_LoadShaderFromName(Requient_ShadersPath, "clip.png")
    setBrushTexdefCoords( brush, flag.getCoords() )

#========================================
#   TexdefFlagPrimit_Caulk()
def TexdefFlagPrimit_Caulk( brush : Brush, flag : Texdef ):
    if brush == 0 or -1:
        return
    if g_reqglobals.d_globalAutoCaulk == True:
        for brush in g_reqglobals.d_globalBrushSelected:
            callTexdefAllocation()
            brush.d_btexdef = flag.getShader() == Requient_LoadShaderFromName(Requient_ShadersPath, "caulk.png")
            setBrushTexdefCoords( brush, flag.getCoords() )

"""
    *CreateBrushPrimit_Cube* :
    
        - takes planes and intersects them in a bounding box, to make cube brush
    
"""
def CreateBrushPrimit_Cube( b : Brush, mins : float, maxs : float , bCubed : bool ):
    w = int
    cube_w = Winding
    cube_mins = mins
    cube_maxs = maxs
    cube_face = Face
    cube_plane = Plane3
    cube_aabb = aabb_spawnable
    
    """Project an AABB to the brush"""
    
    for w in range( cube_face = [b.brushFaces] ) in b:
        cube_w = cube_plane.winding # set winding
        getWinding( cube_w )
        getAxisAllignedBoundingBox( cube_aabb )
        cube_aabb.aabb_bounds[w] = cube_w.windingPoints[w]
        
        getABBB_Points( cube_aabb.aabb_bounds[w] )
        
        for cube_aabb.aabb_bounds[w] in b:
            cube_face[b][0].WindingMakeFace(), cube_face[b][1].WindingMakeFace()
            cube_face[b][2].WindingMakeFace(), cube_face[b][3].WindingMakeFace()
            cube_face[b][4].WindingMakeFace(), cube_face[b][5].WindingMakeFace()
            
            getFace( cube_face[b] )
            
            cube_mins[b] = b.brush_mins
            cube_maxs[b] = b.brush_maxs
            
            getAABB_Bounds( cube_aabb ) == cube_mins[b]
            getAABB_Bounds( cube_aabb ) == cube_maxs[b]
            
            SubtractVector( cube_mins[b][0], cube_mins[b][1], cube_mins[b][2] )
            AddVector( cube_maxs[b][0], cube_maxs[b][1], cube_maxs[b][2] )
            VectorScale( cube_mins[b][0], cube_maxs[b][1], cube_mins[b][2] )
        
    for i in range( 6 ):
        if cube_mins[i][0] == cube_maxs[i][2] and cube_mins[i][1] == cube_maxs[i][1] and cube_mins[i][2] == cube_maxs[i][0]:
            bCubed = False
        if cube_mins[i][0] == cube_maxs[i][1] and cube_mins[i][1] == cube_maxs[i][2] and cube_mins[i][2] == cube_maxs[i][0]:
            bCube = True
            
    if BRUSH_PRIMIT_VERSION == BRUSH_PRIMIT_VERSION:
        print("Brush Primit Valid Version\n")
    if BRUSH_PRIMIT_VERSION != BRUSH_PRIMIT_VERSION:
        print("Brush Primit Invalid Version, Failed To Create\n")
        


"""*BRUSH PRIMIT NAME*"""
def BrushPrimitName( b : Brush ):
    cBuff : str = [2048]
    b.brushNumberId = ++g_nBrushId
    if g_reqglobals.d_globalBrushSelected :
        print( "Brush Selected Number : %i", b.brushNumberId )
        if cBuff == 0:
            cBuff.__delattr__()
            print( "cBuff failed at : Ln 83 ( BrushPrimitName )" )
        if cBuff != 0:
            cBuff.count( 'BRUSH', b.brushNumberId, cBuff )
            
            
"""*Brush Snap To Grid*"""
def Brush_SnapToGrid( b : Brush ):
    bMins = b.brush_mins
    bMaxs = b.brush_maxs
    bPoints = b.bpnts
    
    if g_reqglobals.d_globalDoSmallGrid:
        for i in range( 8 ):
            VectorScale( bMins[i][0] * 0.5, bMaxs[i][0] * 0.5, bMins[i][1] * 0.5 )
            VectorScale( bMaxs[i][1] * 0.5, bMins[i][2] * 0.5, bMaxs[i][2] * 0.5 )
            VectorSnap( bMins[i], bMaxs[i] )
            
            
"""*Brush Draw*"""
def Brush_Draw( b : Brush ):
    w = Winding
    for j in range( 8 ):
        glBegin(GL_POLYGON)
        glVertex3fv(w.windingPoints[j])
        glEnd()
        
def BrushFace_Draw( b : Brush ):
    w = Winding
    face = Face
    face.winding = w.numpoints
    
    for k in range(4):
        glBegin(GL_POLYGON)
        glTexCoord2fv(w.numpoints[k][3])
        glVertex3fv(w.numpoints[k])
        glEnd()
        