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
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from OpenGL.GL import *
from OpenGL.GLU import *
# from OpenGL_accelerate import *   # optional - not required
from face import *
from entity import*
from node import*
from queuedraw import*
from brush import*
from algotool import*
from brushlist import*
from workzone import Workzone
from workzone import SetWorldZoneBounds

class CameraWnd(QOpenGLWidget):
    origin = vec3_t # the camera origin
    
    camera_mins = vec3_t
    camera_maxs = vec3_t
    
    camera_workzone = Workzone

    x = vec3_t
    y = vec3_t
    z = vec3_t
    pitch = vec3_t
    yaw = vec3_t
    fov = 75.0
    aspect = 1
    near = 0.1
    far = 2000.0

    # brushes, pull from the list
    m_pBrushes = g_BrushClipboard.m_nBrushCount
    m_pBrush = Brush()
    m_pFaces = Face()
    m_pFace = Face()
    m_pSideSel = Face()
    m_pWindings = Winding()
    m_pEntities = EntityWorldClass()

    def __init__(self, parent=None):
        super().__init__(parent)

    def initializeGL(self):
        PixelsWriteColorToGl( COLOR_CAMERA_BACKGROUND )

        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)

        glDisable(GL_CULL_FACE)

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glEnable(GL_LINE_SMOOTH)
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        glEnable(GL_POLYGON_SMOOTH)
        glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)

    def resizeGL(self, w: int, h: int):
        if h == 0:
            h = 1
        glViewport(0, 0, w, h)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        aspect = float(w) / float(h)
        gluPerspective(self.fov, aspect, self.near, self.far)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def paintGL(self):
        PixelsWriteColorToGl( COLOR_CAMERA_BACKGROUND )
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    

        # Modelview reset and camera
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
    def CamDraw_Brushes(): pass
    def CamDraw_Entities(): pass
    def CamDraw_Wireframe(): pass
    def CamDraw_Solid(): pass
    def CamDraw_CullBrushes(): pass
    def CamFilter_Brushes(): pass
    def CamFilter_Entities(): pass
    def CamFilter_TexdefType(): pass
        
        
        
        
def hookCameraWindow( glwindow : CameraWnd ):
    return glwindow

def unhookCameraWindow( glwindow : CameraWnd ):
    del glwindow
    
def getCameraWindowOrigin( glwindow : CameraWnd )->float:
    return glwindow.origin

def getCameraWindowAxisType( glwindow : CameraWnd )->float:
    if glwindow.x(float):
        return glwindow.x
    if glwindow.y(float):
        return glwindow.y
    if glwindow.z:
        return glwindow.z

def getCameraWindowPitch( glwindow : CameraWnd )->float:
    return glwindow.pitch

def getCameraWindowYaw( glwindow : CameraWnd )->float:
    return glwindow.yaw

def getCameraWindowFov( glwindow : CameraWnd )->float:
    return glwindow.fov

def getCameraWindowAspect( glwindow : CameraWnd )->int:
    return glwindow.aspect

def getCameraWindowNear( glwindow : CameraWnd )->float:
    return glwindow.near

def getCameraWindowFar( glwindow : CameraWnd )->float:
    return glwindow.far



# set worldzone bounds for camera
SetWorldZoneBounds( CameraWnd.camera_workzone, CameraWnd.camera_mins, CameraWnd.camera_maxs )