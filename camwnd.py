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
from math import*

class CameraWnd(QOpenGLWidget):
    
    camera_mins = vec3_t
    camera_maxs = vec3_t
    
    camera_workzone = Workzone

    projection = [16.0]

    x = vec3_t
    y = vec3_t
    z = vec3_t
    pitch = 0.0
    yaw = 0.0
    fov = 75.0
    aspect = 1
    near = 0.1
    far = 45.0
    movespeed = 0.1
    
    origin = ( 0.0, 0.0, 5.0 )


    """CAMERA MATH"""
    yaw_rad = radians(yaw)
    pitch_rad = radians(pitch)
    
    forward_x = cos(pitch_rad) * cos(yaw_rad)
    forward_y = cos(pitch_rad) * sin(yaw_rad)
    forward_z = -sin(pitch_rad)
    
    right_x = -sin(yaw_rad)
    right_y = cos(yaw_rad)
    right_z = 0
    

    # brushes, pull from the list
    m_pBrushes = g_BrushClipboard.m_nBrushCount

    def __init__(self, parent=None):
        super().__init__(parent)
        self.keys = set()
        self.setFocusPolicy(Qt.StrongFocus)
        
    def keyPressEvent(self, a0):
        self.keys.add(a0.key())
        
    def keyReleaseEvent(self, a0):
        self.keys.discard(a0.key())
        

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
        PixelsWriteColorToGl(COLOR_CAMERA_BACKGROUND)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        if Qt.Key.Key_W in self.keys:
            self.origin.x += self.forward_x * self.movespeed
            self.origin.y += self.forward_y * self.movespeed
            self.origin.z += self.forward_z * self.movespeed
        
        
    
        glLoadIdentity()
    
        CamDraw_Wireframe()
        
        
        
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

def CamDraw_Brushes(): pass
def CamDraw_Entities(): pass
def CamDraw_Wireframe():
    glColor4f(COLOR_SELBRUSHES[0], COLOR_SELBRUSHES[1], COLOR_SELBRUSHES[2], COLOR_SELBRUSHES[3])
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5, -0.5, -2.0)
    glVertex3f(0.5, -0.5, -2.0)
    glVertex3f(0.0, 0.5, -2.0)
    glEnd()
            
def CamDraw_Solid(): pass
def CamDraw_CullBrushes(): pass
def CamFilter_Brushes(): pass
def CamFilter_Entities(): pass
def CamFilter_TexdefType(): pass
        

globalCameraPanelManager = CameraWnd

# set worldzone bounds for camera
SetWorldZoneBounds( CameraWnd.camera_workzone, CameraWnd.camera_mins, CameraWnd.camera_maxs )