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

XY_BUTTON_SIGNAL = QMouseEvent

class XYWnd(QOpenGLWidget):
    
    xyScale = vec3_t
    xyNormal = vec3_t
    xyDrag = vec3_t
    bReDrawLines = bool
    xyUndo = int
    xyRedo = int
    m_bBrushSelected = bool
    m_bXyBrushSelect = bool
    xyPenDrawColor = (0.45, 0.45, 0.40, 0.0)
    xyPenBrushSelectionColor = vec3_t
    bXYCurTracking = bool
    m_pBrushes = [Brush()]
    m_pXYPrevDrag_Point_t = int
    m_xyBrush = Brush() # real member brush
    xy_gridSize = int
    g_reqglobals.d_globalGridSize = xy_gridSize
    xy_s_windings = Winding
    
    def __init__(self, rows=1024, cols=1024, cell_size=50):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.setEnabled(True)
        self.setMouseTracking(True)
        
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
        
    
    def XYZoomIn( self ):
        w = self.cols
        h = self.rows
        
        if self.resize( w, h ):
            self.resizeGL()
        self.paintGL()
        UpdateGLWindow( self )
            
    def wheelEvent(self, a0):
        delt = a0.angleDelta().y()
        
        if delt:
            self.cell_size = 80
            self.XYZoomIn()
            
            
        if delt < 0:
            self.cell_size = 50
            self.XYZoomIn()
        
        
        a0.accept()
        
                        
        

# current x [position] in xy window
def g_XYCurrX(xywnd)->int:
    return xywnd.x()

# current y [position] in xy window
def g_XYCurrY(xywnd)->int:
    return xywnd.y()


# Update GL Window

def UpdateGLWindow( window : QOpenGLWidget ):
    window.update()
