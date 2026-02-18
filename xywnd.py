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
from node import*
from brush import*
from brushcreationtool import*
from box import*
from brushwrapperapi import*
from qesmatictypes import*
from brush_primit import*

XY_BUTTON_SIGNAL = QMouseEvent

# XY_DRAG_RANGE
BOGUS_BRUSH_DRAG = 9999

class XYWnd(QOpenGLWidget):
    
    xy_gridSize = int
    globalREQGlobalsManager().d_globalGridSize = xy_gridSize
    
    floor = vec3_t
    celing = vec3_t
    mins = vec3_t
    maxs = vec3_t
    
    def __init__(self, rows=1024, cols=1024, cell_size=50):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.setEnabled(True)
        self.setMouseTracking(True)
        self.keys = set()
        self.xy_gridSize = self.rows + self.cols

    def initializeGL( self ):
        PixelsWriteColorToGl( COLOR_GRID_BACKGROUND )
        glDisable(GL_DEPTH_TEST)  # 2D, no depth needed
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_TEXTURE_1D)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
            

    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        # Compute ideal scale for square cells
        scale_x = w / self.cols
        scale_y = h / self.rows
        scale = min(scale_x, scale_y)

        # Compute small stretch factors to fill window
        stretch_x = w / (self.cols * scale)
        stretch_y = h / (self.rows * scale)

        # Set orthographic projection with slight stretch
        glOrtho(0, self.cols * stretch_x, 0, self.rows * stretch_y, -1, 1)

        glViewport(0, 0, w, h)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        
        glColor3f(0.6, 0.6, 0.6)  # white grid
        glBegin(GL_LINES)
        # vertical lines
        for i in range(self.cols + 1):
            x = i * self.cell_size
            glVertex2f(x, 0)
            glVertex2f(x, self.rows * self.cell_size)
        # horizontal lines
        for j in range(self.rows + 1):
            y = j * self.cell_size
            glVertex2f(0, y)
            glVertex2f(self.cols * self.cell_size, y)
        glEnd()
    
    
    
    def keyPressEvent(self, a0):
        self.keys.add(a0.key())
    
    def keyReleaseEvent(self, a0):
        self.keys.discard(a0.key())
        
    def mouseDoubleClickEvent(self, a0):
        c = Qt.MouseButton.RightButton
        
        
        if c:
            _menu = QMenu(self)
            _menu.setGeometry(a0.pos().x(), a0.pos().y(), 0, 0)
            
            path_node = QAction("&Spawn Path Node", _menu)
            _menu.addAction(path_node)
            
            _menu.addSeparator()
            
            target_node = QAction("&Spawn Target Node", _menu)
            _menu.addAction(target_node)
            
            _menu.addSeparator()
            
            script_node = QAction("&Spawn Script Node", _menu)
            _menu.addAction(script_node)
            
            _menu.addSeparator()
            
            aabb_node = QAction("&Spawn Bounding Box", _menu)
            _menu.addAction(aabb_node)
            
            _menu.addSeparator()
            
            caulk_brush = QAction("&Caulk selected brush", _menu)
            _menu.addAction(caulk_brush)
            
            _menu.addSeparator()
            
            esp_node = QAction("&Spawn ESP MaxArm Entity", _menu)
            _menu.addAction(esp_node)
            
            _menu.show()
            
            
    
    
    def Print_GL_String( self, char : str, x : int, y : int ): pass
        
    def XYZoomIn( self ):
        w = self.cols
        h = self.rows
        
        UpdateGLWindow( self )
            
    def wheelEvent(self, a0):
        delt = a0.angleDelta().y()
        
        if delt:
            self.cell_size = 80
            self.XYZoomIn()
            
            
        if delt < 0:
            self.cell_size = 20
            self.XYZoomIn()
        
        
        a0.accept()
            
            
        
    # handles the NewBrush_Drag event
    def mousePressEvent(self, a0):
        pres = a0.buttons() == Qt.MouseButton.LeftButton
        pres_x = a0.x()
        pres_y = a0.y()
        if self and pres:
            NewBrush_Drag( pres_x, pres_y )
            UpdateGLWindow( self )
                
"""
/*
=================================
    NewBox_Drag()
=================================
*/
"""
def NewBox_Drag( x : int, y : int ):
    m_aabb = aabb_spawnable
    m_mins = ( 1.0, 5.0, 10.0 )
    m_maxs = ( 10.0, 5.0, 1.0 )
    
    boxDoCreation( m_aabb, m_mins, m_maxs, True )
    
    if m_aabb == -1:
        REQUIENT_MESSAGE("New-Box-Drag Tool failed...", m_aabb)
    
    
    if m_aabb != -1:
        REQUIENT_MESSAGE("New-Box-Drag Tool creation succesfull...", m_aabb)
"""
/*
=================================
    NewBrush_Drag()
=================================
*/
"""
def NewBrush_Drag( x : int, y : int ):
    new_brush = Brush

    mins = new_brush.mins
    maxs = new_brush.maxs
    
    world_mins = g_MinWorldCoord
    world_maxs = g_MaxWorldCoord
    
    workzone_mins = vec3_t
    workzone_maxs = vec3_t
    
    nDim = [ VIEW_XY ] , [ VIEW_XZ ], [ VIEW_YZ ]
    
    for k in range( BOGUS_BRUSH_DRAG ):
        ++k
    
    xy_w = Winding
    
    new_brush = Alloc_Brush()
    
    Brush_Cuboid( new_brush, mins, maxs, True )
    WindingMake_Brush( xy_w )
    BrushDraw_XY( new_brush, nDim )
    Select_Brush( new_brush )
    REQBuild_Brush( new_brush )
    
    if new_brush == 0:
        del( new_brush )
        REQUIENT_MESSAGE("NewBrush_Drag Failed... at mouse coords", x and y )
    
    if new_brush != 0:
        REQUIENT_MESSAGE("New-Brush-Drag Tool succesfull...", x and y)
    
    return x, y
    
def Draw_Brushes():pass
def Draw_BrushesSelected():pass
def Draw_Entities():pass
def Draw_EntitiesSelected():pass
def Draw_ConnectLines():pass

globalXYManager = XYWnd

# current x [position] in xy window
def g_XYCurrX(xywnd)->int:
    return xywnd.x()

# current y [position] in xy window
def g_XYCurrY(xywnd)->int:
    return xywnd.y()


# Update GL Window

def UpdateGLWindow( window : QOpenGLWidget ):
    window.update()
    
    
