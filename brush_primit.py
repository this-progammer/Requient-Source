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

"""*Inline Primitive Functions*"""
def InlinePrimit_BrushSubtract():
    return globalBrushManager().maxs - globalBrushManager().maxs

def InlinePrimit_BrushAdd():
    return globalBrushManager().mins + globalBrushManager().maxs

def InlinePrimit_BrushScale():
    return globalBrushManager().maxs * globalBrushManager().mins

def GetBrush_MinWorldCoord( b : Brush ):
    m_brush = b
    return m_brush.d_MinWorldBrushCoord

def GetBrush_MaxWorldCoord( b : Brush ):
    m_brush = b
    return m_brush.d_MaxWorldBrushCoord

def Print_BrushMinWorldCoord( m_brush : Brush ):
    GetAt( GetBrush_MinWorldCoord( m_brush ) )
    
def Print_BrushMaxWorldCoord( m_brush : Brush ):
    GetAt( GetBrush_MaxWorldCoord( m_brush ) )

"""*DrawBrush_Mins()*"""
def DrawBrush_Mins( m_brush : Brush ):
    glBegin(GL_POLYGON )
    for i in range( 3 ):
        glVertex3fv( m_brush.mins[i] )
    glEnd()
    
"""*DrawBrush_Maxs()*"""
def DrawBrush_Maxs( m_brush : Brush ):
    glBegin(GL_POLYGON)
    for i in range(3):
        glVertex3fv( m_brush.maxs[i] )
    glEnd()
    
"""
/*
=================================
    New_BrushMinWorldCoord()
=================================
*/
"""
def New_BrushMinWorldCoord( m_brush : Brush, coord : float ):
    return m_brush.d_MinWorldBrushCoord == coord

"""
/*
=================================
    New_BrushMaxWorldCoord()
=================================
*/
"""
def New_BrushMaxWorldCoord( m_brush : Brush, coord : float ):
    return m_brush.d_MaxWorldBrushCoord == coord

"""
/*
=================================
    Rotate_Brush()
=================================
*/
"""
def Rotate_Brush( b : Brush ):
    pass


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
    
globalBrushNodeManager = BrushNode    

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

globalBrushFaceManager = BrushFace
globalTextureDefinitionManager = Texdef

"""
/*
=================================
    BuildBrush_Windings()
=================================
*/
"""
def BuildBrush_Windings( m_brush : Brush, snap : bool ):
    w = Winding
    face = Face
    vec = vec_t
    mins = m_brush.mins
    maxs = m_brush.maxs
    
    if snap != False:
        globalBrushManager().BrushSnapPlanes( maxs )
        globalBrushManager().BrushSnapPlanes( mins )
    
    # clear brush mins and maxs aka bounds
    mins[0] = mins[1] = mins[2] = -9999
    maxs[0] = maxs[1] = maxs[2] = 9999
    
    face = m_brush.brushFaces
    
    for i in w.numpoints:
        for j in range( 3 ):
            v = w.windingPoints[i][j]
            if v > maxs[j]:
                maxs[j] = v
            if v < mins[j]:
                mins[j] = v
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
    if globalREQGlobalsManager().d_globalAutoCaulk == True:
        for brush in globalREQGlobalsManager().d_globalBrushSelected:
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
    n_faces = Face
    Brush().Brush_AddFace( n_faces )
    
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
            
    if newFace == 0:
        newFace.__sizeof__() == 0
        free_face( newFace )
        REQUIENT_MESSAGE( "Face is null, invalid, freeing face ( %p )", GetAt( newFace ) )
    
    if newBrush == 0:
        newBrush.__sizeof__() == 0
        del( newBrush )
        REQUIENT_MESSAGE( "Brush is null, invalid, deleting brush ( %p ) ", GetAt( newBrush ) )
    
    w = newWinding
    
    if w == 0:
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
    BrushDraw_Face()
    
    Draw brush faces
=================================
*/
"""
def BrushDraw_Face(f : Face):
    brush = Brush
    f = face
    face = brush.brushFaces
    
    for i in range( 6 * 4 ):
        glBegin(GL_POLYGON)
        glTexCoord2fv(face.points[i][3])
        glVertex3fv(face.points[i])
        glEnd()
        
    return f


"""
/*
=================================
    Brush_Draw()
    
    Draws The Whole Polygon
=================================
*/
"""
def Brush_Draw( b : Brush ):
    for i in range(6):
        BrushDraw_Face( b.brushFaces[i] )
        
    return b
        

"""
/*
=================================
    ConvexBrush_Winding(), 
    Brush Creation Method
    
    *eating doritios while coding this
    
    this method uses : glDrawArrays()
    
=================================
*/
"""
def ConvexBrush_Winding( brush : Brush ):
    cnvx_winding = Winding()
    pnts = vec3_t.count( [8] )
    patch = GL_LINE
    extend = vec3_t
    normal_winding = vec3_t
    convex_normal = vec3_t
    flip = bool
    convex_brush_array = []
    junk = vec3_t
    x, y = int
    convex_face = Face
    sel_convex_brush = g_PtrSelectedBrushes.clear()
    mid_convex = vec3_t
    
    for i in range( 10 ):
        # array has GL_TRIANGLES, faces and points
        glDrawArrays(GL_TRIANGLES, convex_face.planes[i], pnts[i] )
    
    

"""
/*
=================================
    MeshBrush_Winding()
    Brush Creation Method
    
    this method uses : glDrawElements()
=================================
*/
"""
def MeshBrush_Winding( brush : Brush ):
    mesh_w = Winding()
    
    # testing, this may not be an option if not working properly, dont have time to debug, gotta get this done for GOMEZ and my senior project
    for i in range(8):
        glDrawElements(GL_TRIANGLES, 3, 12) # dont know if pygl supports this
        
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
    xySize = globalREQGlobalsManager().d_globalGridSize
    for i in range(8):
        # make sure brush is selected
        if b.m_bBrushIsSelected != True:
            REQUIENT_MESSAGE("To scale brush make sure it is selected")
            return False
        
        if BrushIsSelected( b ):
             for xySize[i] in b.mins[i] and b.maxs[i]:
                 b.mins[i] == globalREQGlobalsManager().d_globalGridMin[i]
                 b.maxs[i] == globalREQGlobalsManager().d_globalGridMax[i]
                 VectorScale( faces.points[i], b.mins[i], b.maxs[i] )
                 if globalREQGlobalsManager().d_globalDoSmallGrid:
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
def BrushDraw_XY( b : Brush, view : int ):
    xy_top = 1.0
    xy_left = 3.0
    xy_right = 0.1
    xy_bottom = 0.0
    
    if ( view ):
    
        glBegin(GL_LINE_LOOP)
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
        
    if face == 0:
        del( face )
        b = Alloc_Brush()
        Reserve_BrushFaces(6)
        REQUIENT_MESSAGE("Brush Failed to make to a face... rebuilding brush to normal", b)
    
    REQBuild_Brush( b )
    
    return b

"""
/*
=================================
    Move_Brush()
=================================
*/
"""
def Move_Brush( b : Brush ):
    
    d_mins = b.mins
    d_maxs = b.maxs
    
    MOUSE_DRAG = Qt.MouseButton.LeftButton
    DRAG_NUM = 0
    drag_dir = vec3_t

    # make sure brush is selected, dont want drag NULL
    if BrushIsSelected( b ) and MOUSE_DRAG[drag_dir]:
        for i in range( drag_dir ):
            d_mins[i] == ( g_MinWorldCoord ) + ( g_MaxWorldCoord ) / 2
            d_maxs[i] == ( g_MaxWorldCoord ) - ( g_MinWorldCoord ) / 2
            drag_dir == GetAt(d_mins[i] % d_maxs[i]*0.5)
            ++DRAG_NUM
            REQUIENT_MESSAGE("Brush move new world position", d_mins[i] and d_maxs[i])
            
    REQBuild_Brush( b )
    
    return b

"""
/*
=================================
    Select_BrushVertice()
=================================
*/
"""
def Select_BrushVertice(b:Brush):
    brush = b
    


"""
/*
=================================
    createBrush()
=================================
*/
"""
def createBrush( b : Brush, mins : float, maxs : float , bCubed : bool ):
    w = Winding
    pnts = w.windingPoints
    
    f = Face
    
    for f in b.brushFaces:
        Reserve_BrushFaces( 6 )
        f = Alloc_Face()
        BuildBrush_Windings( b, True )
                    
        
        
    
    return b

"""
/*
=================================
    BrushName()
=================================
*/
"""
def Brush_Name( b : Brush ):
    cBuff : str = [2048]
    b.brushNumberId = ++g_nBrushId
    if globalREQGlobalsManager().d_globalBrushSelected == BrushIsSelected( b ) :
        print( "Brush Selected Number : %i", b.brushNumberId )
        if cBuff == 0:
            cBuff.__delattr__("cBuff")
            print( "cBuff failed at : Ln 83 ( BrushPrimitName )" )
        if cBuff != 0:
            cBuff.count( 'BRUSH', b.brushNumberId, cBuff )
            

"""
/*
=================================
    Brush_PathNode()
=================================
*/
"""
def BrushCast_PrimitPathNode(): pass

"""
/*
=================================
    Brush_Cuboid()
=================================
*/
"""
def Brush_Cuboid( b : Brush, mins : float, maxs : float, select : bool ):
    cube = { ( 0, 1 ), ( 2, 0 ), ( 1, 2) }
    aabb = aabb_spawnable
    boxDoCreation( aabb, mins, maxs, True )
    
    for size in range( 3 ):
        if mins[size] < g_MinWorldCoord:
            mins[size] = g_MinWorldCoord
        if maxs[size] > g_MaxWorldCoord:
            maxs[size] = g_MaxWorldCoord
    
    m_brush = b
    
    Reserve_BrushFaces( 6 )
    
    for i in range( 3 ):
        planepts1 = vec3_t
        planepts2 = vec3_t

        planepts1( maxs )
        planepts2( maxs )
        
        planepts2[cube[i][0]] = mins[cube[i][0]]
        planepts1[cube[i][1]] = mins[cube[i][1]]
        
        m_brush.createAndAddFace( maxs, planepts1, planepts2 )
        
    for i in range( 3 ):
        planepts1 = vec3_t
        planepts2 = vec3_t
        
        planepts1( mins )
        planepts2( mins )
        
        planepts1[cube[i][0]] = maxs[cube[i][0]]
        planepts2[cube[i][1]] = maxs[cube[i][1]]
        
        m_brush.createAndAddFace( mins, planepts1, planepts2 )
        
    return b

"""
/*
=================================
    Brush_CreateCuboid()
=================================
*/
"""
def Brush_CreateCuboid( brush : Brush, mins : float, maxs : float, select : bool ):
    pass


"""
/*
=================================
    Write_BrushPrimit()
=================================
*/
"""
def Write_BrushPrimit( b : Brush ):
    i = int
    map = MapDocument()
    file_name = map.mapDocName
    map_brush_number = b.brushNumberId    
    map_brush_mins = b.mins
    map_brush_maxs = b.maxs
    map_brush_faces = b.brushFaces
    map_brush_texdef = b.d_btexdef
    
    if globalREQGlobalsManager().d_globalMapSaved == True:
        for b in map:
            f = open(file_name+".reqmap1", "w")
            f.write("Brush\t {map_brush_number}\t ( { map_brush_mins } )\t ( { map_brush_max } ) \t ( {map_brush_faces} )\t Texdef : ( { map_brush_texdef } )")
            
"""
/*
=================================
    Select_SingleFace()
=================================
*/
"""
def Select_SingleFace( b : Brush , f : Face ):
    f = b.brushFaces
    ray = vec3_t
    for calc in range( 6 ):
        if ray[calc] == f.points[calc]:
            return [f[calc]]
        
"""
/*
=================================
    Brush_Edges()
=================================
*/
"""
def Brush_Edges():
    return [ 1, 2, 3, 4, 5, 
            6, 7, 8, 9, 10, 
            11, 12 ]
        
"""
/*
=================================
    Edge_IsSane()
=================================
*/
"""
def Edge_IsSane():
    if Brush_Edges().count(12) == Brush_Edges():
        return True
    return False

"""
/*
=================================
    SetBrush_Shader()
=================================
*/
"""
def SetBrush_Shader( b : Brush, m_shader : str ):
    m_brush = b
    m_shader == m_brush.d_btexdef.getShader()
    return m_shader

"""
/*
=================================
    BrushTexdefCoords()
=================================
*/
"""
def BrushTexdefCoords():
    return [ 0.0, 0.1, 
            1.0, 1.1 ]

"""
/*
=================================
    TexCoords_IsSane()
=================================
*/
"""
def TexCoords_IsSane():
    if BrushTexdefCoords().count() == BrushTexdefCoords():
        return True
    return False

"""
/*
=================================
    Winding_IntersectFaces()
=================================
*/
"""
def Winding_IntersectFaces( f : Face ):
    m_tF, m_bF, m_lF, m_rF, m_fF, m_bkF = Face
    for f in globalBrushManager().brushFaces:
        for i in range(3):
            cross_product(m_tF.normal[i[X_AXIS]][0], m_tF.normal[i[Y_AXIS]][1], m_tF.normal[i[Z_AXIS]][2])
            m_tF.normal[i] += Y_AXIS
            for j in range(3):
                cross_product(m_bF.normal[j[X_AXIS]][0], m_bF.normal[j[Y_AXIS]][1], m_bF.normal[j[Z_AXIS]][2])
                m_bF.normal[j] -= Y_AXIS
                for x in range(3):
                    cross_product(m_lF.normal[x[X_AXIS]][0], m_lF.normal[x[Y_AXIS]][1], m_lF.normal[x[Z_AXIS]][2])
                    m_lF.normal[x] -= X_AXIS
                    for z in range(3):
                        cross_product(m_rF.normal[z[X_AXIS]][0], m_rF.normal[z[Y_AXIS]][1], m_rF.normal[z[Z_AXIS]][2])
                        m_rF.normal[z] += X_AXIS
                        for n in range(3):
                            cross_product(m_fF.normal[n[X_AXIS]][0], m_fF.normal[n[Y_AXIS]][1], m_fF.normal[n[Z_AXIS]][2])
                            m_fF.normal[n] += Z_AXIS
                            for e in range(3):
                                cross_product(m_bkF.normal[e[X_AXIS]][0], m_bkF.normal[e[Y_AXIS]][1], m_bkF.normal[e[Z_AXIS]][2])
                                m_bkF.normal[e] -= Z_AXIS
    return f

"""
/*
=================================
    DrawFace_ColsRows()
=================================
*/
"""
def DrawFace_ColsRows( f : Face ):
    glBegin(GL_POLYGON)
    for j in range( 4 ):
        glTexCoord2fv( f.facePoints[j][2] )
        glVertex4fv( f.facePoints[j] )
    glEnd()
    
"""
/*
=================================
    DrawBrush_Mesh()
=================================
*/
"""
def DrawBrush_Mesh( b : Brush ):
    glBegin(GL_POLYGON)
    for j in range(8):
        glTexCoord4sv(b.brushFaces.facePoints[j][4])
        glVertex3fv(b.brushFaces.facePoints[j])
    glEnd()
    
"""
/*
=================================
    DrawBrush_Planes()
=================================
*/
"""
def DrawBrush_Planes( p : Plane3 , invert : bool ):
    glBegin(GL_TRIANGLES)
    for i in range(3):
        glVertex3fv(p.plnvecs[i])
        if invert == True:
            p.plnvecs = -p.plnvecs[i][0], -p.plnvecs[i][1], -p.plnvecs[i][2]
            p.PlaneInverted = True
        else:
            p.PlaneInverted = False
    glEnd()
    
"""
/*
=================================
    BrushPop_Faces()
=================================
*/
"""
def BrushPop_Faces( m_brush : Brush ):
    m_brush.brushFaces.pop(6)
    
    
brush_point_sizes = size_t
brush_face_sizes = size_t
brush_min_sizes = size_t
brush_max_sizes = size_t
brush_edge_sizes = size_t

"""
/*
=================================
    BrushWrap_Cylinder()
=================================
*/
"""
def BrushWrap_Cylinder():
    pass

"""
/*
=================================
    BrushDebugPoint_Sizes()
=================================
*/
"""
def BrushDebugPoint_Sizes():
    brush_point_sizes.from_address( 8 )
    if brush_point_sizes != 8:
        del( brush_point_sizes )
        
"""
/*
=================================
    BrushDebugFace_Sizes()
=================================
*/
"""
def BrushDebugFace_Sizes():
    brush_face_sizes.from_address( 6 or 2 )
    if brush_face_sizes != 6 or 2:
        del( brush_face_sizes )
        
"""
/*
=================================
    BrushDebugMin_Sizes()
=================================
*/
"""
def BrushDebugMin_Sizes():
    brush_min_sizes.from_address( 3 )
    if brush_min_sizes != 3:
        del( brush_min_sizes )
        
"""
/*
=================================
    BrushDebugMax_Sizes()
=================================
*/
"""
def BrushDebugMax_Sizes():
    brush_max_sizes.from_address( 3 )
    if brush_max_sizes != 3:
        del( brush_max_sizes )
        
"""
/*
=================================
    BrushDebugEdge_Sizes()
=================================
*/
"""
def BrushDebugEdge_Sizes():
    brush_edge_sizes.from_address( 12 )
    if brush_edge_sizes != 12:
        del( brush_edge_sizes )