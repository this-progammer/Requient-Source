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
from algotool import*

BRUSH_PRIMIT_VERSION = "1.0.0"
BRUSH_PRIMIT_MAJOR = "Brush"

TEXTURE_FLAG_CAULK = 27
TEXTURE_FLAG_BOT_CLIP = 37
TEXTURE_FLAG_BOT_ZONE = 67 # haha, get it

"""
/*
=================================
    globals()
=================================
*/
"""
g_nBrushId = int

g_PtrSelectedFaces = list([Face()])
g_PtrSelectedBrushes = list([Brush()])
g_PtrCaulkedBrushes = list([Brush()])
g_PtrClippedBrushes = list([Brush()])


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
    
class BrushWinding:
    
    def getBrushWinding( self ):
        return( self )

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

"""
/*
=================================
    TexdefFlagPrimit_Clip()
=================================
*/
"""
def TexdefFlagPrimit_Clip( brush : Brush, flag : Texdef ):
    if brush == 0 or -1:
        return
    callTexdefAllocation()
    brush.d_btexdef = flag.getShader() == Requient_LoadShaderFromName(Requient_ShadersPath, "clip.png")
    setBrushTexdefCoords( brush, flag.getCoords() )

"""
/*
=================================
    TexdefFlagPrimit_Caulk()
=================================
*/
"""
def TexdefFlagPrimit_Caulk( brush : Brush, flag : Texdef ):
    if brush == 0 or -1:
        return
    if g_reqglobals.d_globalAutoCaulk == True:
        for brush in g_reqglobals.d_globalBrushSelected:
            callTexdefAllocation()
            brush.d_btexdef = flag.getShader() == Requient_LoadShaderFromName(Requient_ShadersPath, "caulk.png")
            setBrushTexdefCoords( brush, flag.getCoords() )

"""
/*
=================================
    REQBuild_Brush()
=================================
*/
"""
def REQBuild_Brush( b : Brush ):
    req_buf = [512]
    _Ptr_Brush = b
    _Ptr_Brush_Faces = b.brushFaces
    _Ptr_Brush_Texdef = b.d_btexdef
    
    _Ptr_Brush = Alloc_Brush()
    _Ptr_Brush_Faces = Alloc_Face()[6]
    _Ptr_Brush_Texdef = Alloc_Texdef()
    
    _ptr_brush_build_set = BrushIterator()
    
    # "SHOULD" automatically update brush mins and maxs
    
    _ptr_brush_build_set.BrushIteratorBegin( _Ptr_Brush )
    _ptr_buffer_context = set()
    for i in range( [req_buf] ):
        _ptr_buffer_context.update(_Ptr_Brush[req_buf])
        _ptr_buffer_context.update(_Ptr_Brush_Faces[req_buf])
        _ptr_buffer_context.update(_Ptr_Brush_Texdef[req_buf])
    _ptr_brush_build_set.BrushIteratorEnd( _Ptr_Brush )
    
    return _Ptr_Brush
    

"""
/*
=================================
    Reserve_BrushFaces()
=================================
*/
"""
def Reserve_BrushFaces( n : int ):
    GetAt( n )
    Brush().Brush_AddFace(Face([n]))
    
"""
/*
=================================
    BrushIsSelected()
=================================
*/
"""
def BrushIsSelected( b : Brush )->bool:
    return b.m_bBrushIsSelected == True

"""
/*
=================================
    WindingMake_Brush(), returns visible face on polygon
=================================
*/
"""
def WindingMake_Brush( w : Winding ):
    i = int
    
    newWinding = Winding()
    newBrush = Brush()
    newTexdef = Texdef()
    newFace = Face()
    
    newBrush = Alloc_Brush()
    newFace = Alloc_Face()
    newTexdef = Alloc_Texdef()
    
    Reserve_BrushFaces( 6 )
    
    for i in range( 8 ):
        f = newFace
        f.points[i][0] == newWinding.windingPoints[i][0], f.points[i][1] == newWinding.windingPoints[i][1], f.points[i][2] == newWinding.windingPoints[i][2]
        f.points[i][3] == newWinding.windingPoints[i][3]
        
    for j in range( 8 ):
        if f.points[j] > g_MaxWorldCoord:
            delattr( f, "DEBUG" )
            REQUIENT_MESSAGE( "Face points greater than max world coord, GetAt( %p ) ", GetAt( f ) )
        if f.points[j] < g_MinWorldCoord:
            delattr( f, "DEBUG" )
            REQUIENT_MESSAGE( "Face points less than min world coord, GetAt( %p ) ", GetAt( f ) )
            
    if newFace == ( 0 ) or ( -1 ):
        newFace.__sizeof__() == 0
        free_face( newFace )
        REQUIENT_MESSAGE( "Face is null, invalid, freeing face ( %p )", GetAt( newFace ) )
    
    if newBrush == ( 0 ) or ( -1 ):
        newBrush.__sizeof__() == 0
        del( newBrush )
        REQUIENT_MESSAGE( "Brush is null, invalid, deleting brush ( %p ) ", GetAt( newBrush ) )
    
    w = newWinding
    
    if w == ( 0 ) or ( -1 ):
        w.__sizeof__() == 0
        del( w )
        REQUIENT_MESSAGE( "Winding is null, invalid, deleting winding()", GetAt( w ) )
    
    TexdefFlagPrimit_Caulk( newBrush, newTexdef )
    
    REQBuild_Brush( newBrush )
    
    for x in range( 8 ):
        glBegin(GL_POLYGON)
        glTexCoord3fv(*[w.windingPoints[x][3]])
        glVertex3fv(w.windingPoints[x])
        glEnd()
    
    return w
        

"""
/*
=================================
    Debug_Brush()
=================================
*/
"""
def Debug_Brush(b : Brush, Err : bool ):
    if b.mins == 0:
        del( b )
        REQUIENT_MESSAGE("Brush invalid mins", b.mins)
        b = Alloc_Brush()
        return Err( True )
    
    if b.maxs == 0:
        del( b )
        REQUIENT_MESSAGE("Brush invalid maxs", b.maxs)
        b = Alloc_Brush()
        return Err( True )

    if b.mins == b.maxs:
        GetAt( -1 )
        REQUIENT_MESSAGE("Brush mins == Brush maxs, degenerate brush", b.mins and b.maxs)
        b = Alloc_Brush()
        return Err( True )
    
    if b.d_btexdef != ( TEXTURE_FLAG_CAULK or TEXTURE_FLAG_BOT_CLIP ):
        REQUIENT_MESSAGE("Brush has invalid texture shaders")
        del( b.d_btexdef )
        texDef = Brush().d_btexdef
        texDef = Alloc_Texdef()
        b.d_btexdef = texDef
        
        if b.d_btexdef == ( TEXTURE_FLAG_BOT_ZONE ):
            REQUIENT_MESSAGE("Texture : BOT_ZONE not avalible with BRUSH_PRIMIT versions 1.0.0 only 1.1.0, but I havent programmed it yet so... ", b.d_btexdef)
            
"""
/*
=================================
    Brush_OutOfBounds()
=================================
*/
"""
def Brush_OutOfBounds(b : Brush):
    brush_mins = b.mins
    brush_maxs = b.maxs
    
    for i in range(6):
        if brush_mins[i] and brush_maxs[i] > g_MaxWorldCoord:
            REQUIENT_MESSAGE("Brush size exceeds max world coord, resizing brush...", b)
            # resize brush position
            brush_mins[i] == ( g_MinWorldCoord ).count( 1 ) % 2
            brush_maxs[i] == ( 100.0, 100.0, 100.0 ).count( 1 ) % 2
            
            GetAt( brush_mins[i] )
            GetAt( brush_maxs[i] )
            
    for j in range(6):
        if brush_mins[j] and brush_maxs[j] < g_MinWorldCoord:
            REQUIENT_MESSAGE("Brush size less than min world coord, resizing brush...", b)
            # resize brush position
            brush_mins[j] == ( g_MinWorldCoord ).count( 1 ) % 2
            brush_maxs[j] == ( brush_mins[j][0], brush_maxs[j][1], brush_mins[j][2] ).count( 99 ) % 2
            
            GetAt( brush_mins[j] )
            GetAt( brush_maxs[j] )
    
    return b

"""
/*
=================================
    Scale_Brush()
=================================
*/
"""
def Scale_Brush(b : Brush):
    faces = b.brushFaces
    xySize = g_reqglobals.d_globalGridSize
    for i in range(8):
        # make sure brush is selected
        if b.m_bBrushIsSelected != True:
            REQUIENT_MESSAGE("To scale brush make sure it is selected")
            return False
        
        if BrushIsSelected( b ):
             for xySize[i] in b.mins[i] and b.maxs[i]:
                 b.mins[i] == g_reqglobals.d_globalGridMin[i]
                 b.maxs[i] == g_reqglobals.d_globalGridMax[i]
                 VectorScale( faces.points[i], b.mins[i], b.maxs[i] )
                 if g_reqglobals.d_globalDoSmallGrid:
                     VectorSnap(b.mins[i], b.maxs[i])
                     
    REQBuild_Brush( b )
    
    return b

"""
/*
=================================
    BrushDraw_XY()
=================================
*/
"""
def BrushDraw_XY(b:Brush, view : int ):
    xy_top = 1.0
    xy_left = 3.0
    xy_right = 0.1
    xy_bottom = 0.0
    
    if ( view ):
    
        glBegin(GL_QUADS)
        glVertex2f( xy_top, -xy_bottom )
        glVertex2f( -xy_top, xy_bottom )
        glVertex2f( xy_left, -xy_right )
        glVertex2f( -xy_left, xy_right )
        glEnd()
        
"""
/*
=================================
    Select_Brush()
=================================
*/
"""
def Select_Brush( b : Brush ):
    brush_sel_iterator = BrushSelectionIterator()
    RAY = brush_sel_iterator.selection_trace_ray
    trace_mins = b.mins
    trace_maxs = b.maxs
    v = int
    
    # check if ray hits the brush, if it does, select it
    if RAY == ( trace_mins ) / ( trace_maxs ) / 2:
        if True:
            REQUIENT_MESSAGE("Selected Brush...", RAY)
            BrushIsSelected( b ) # tell its selected
            g_PtrSelectedBrushes == ( [b] )
            g_PtrSelectedBrushes.append( b )
            g_PtrSelectedFaces == ( [b.brushFaces] )
            g_PtrSelectedFaces.append( b.brushFaces )
            PixelsWriteColorToGl( brush_sel_iterator.brush_selection_color )
            brush_sel_iterator.BrushSelectionIteratorBegin( b )
            if ( v ):
                PixelsWriteColorToGl( COLOR_SELBRUSH2D )
        if False:
            REQUIENT_MESSAGE("Ray Didnt Hit Brush, Brush Selection Failed...", RAY)
            brush_sel_iterator.BrushSelectionIteratorEnd( b )

    return b
"""
/*
=================================
    BrushMake_Face()
=================================
*/
"""
def BrushMake_Face(b:Brush):
    face = Face
    Reserve_BrushFaces(1)
    for i in range(6):
        b.brushFaces[i] == [face].pop(5) # pop 5 faces so one is left
        
    if face == ( 0 ) or ( -1 ):
        del( face )
        b = Alloc_Brush()
        Reserve_BrushFaces(6)
        REQUIENT_MESSAGE("Brush Failed to make to a face... rebuilding brush to normal", b)
    
    REQBuild_Brush( b )
    
    return b

"""
/*
=================================
    createBrush()
=================================
*/
"""
def createBrush( b : Brush, mins : float, maxs : float , bCubed : bool ):
    pass

"""
/*
=================================
    BrushPrimitName()
=================================
*/
"""
def BrushPrimitName( b : Brush ):
    cBuff : str = [2048]
    b.brushNumberId = ++g_nBrushId
    if g_reqglobals.d_globalBrushSelected == BrushIsSelected( b ) :
        print( "Brush Selected Number : %i", b.brushNumberId )
        if cBuff == 0:
            cBuff.__delattr__("cBuff")
            print( "cBuff failed at : Ln 83 ( BrushPrimitName )" )
        if cBuff != 0:
            cBuff.count( 'BRUSH', b.brushNumberId, cBuff )