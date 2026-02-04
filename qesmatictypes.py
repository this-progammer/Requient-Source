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

#***imports***

from OpenGL.GL import*
from OpenGL_accelerate import*

EDITOR_VERSION = '1.0'

#entity visible???
bVisible = bool

Requient_MapPath = str
Requient_ShadersPath = str
Requient_ModelsPath = str

#grid arrow
ARROW = 0xDD0
ARROW_LOOP = 0xDD1
ARROW_LINE = 0xDD2

#=================================
AXIS_ALIGNED_BOUNDING_BOX = 0xEE0

#=================================
XY_UP = 0x0
XY_LEFT = 0x1
XY_DOWN = 0x2
XY_RIGHT = 0x3

# load shaders, use GL later
def Requient_LoadShaderFromName( dir : str, shader : str ):
    bShaderExists = bool
    dirObj = object
    
    # must set dir == requient shader path
    if dir != Requient_ShadersPath:
        print("Shader directory invalid")

    else:
        print("accessing shaders from shader directory")
        
    for dir in range:
        if shader != 0 or -1:
            setattr( dirObj, shader, 1 ) # flag it
            
            
            

#$=============================================================
#$             Simulation Stuff
Requient_SimulationWindowTitle = 'Requient Simulator'
Requient_bWindowPopup = bool # is the simulation window a popup ?


class REQApiWrapper:
    
    def ApiGetWrapper( wrapper : any ):
        return wrapper


# wrapper table

d_ApiWrapperTable = REQApiWrapper

class REQ_Globals:
    d_globalGridSize = int
    d_globalBrushMode = bool
    d_globalEntityMode = bool
    d_globalGridDrawMode = bool
    d_globalGridMin = float
    d_globalGridMax = float
    d_globalBrushSelected = bool
    d_globalDoSmallGrid = bool
    d_globalAutoCaulk = bool
    
    d_globalWin32Scheme = bool
    d_globalBlackScheme = bool
    
def reqFastPointer( req : REQ_Globals ):
    return req

# call to req globals
g_reqglobals = REQ_Globals()

def RequientGridTableGetAPIWhite()->bool:
    return g_reqglobals.d_globalWin32Scheme == True
    
def RequientGridTableGetAPIBlack()->bool:
    return g_reqglobals.d_globalBlackScheme == True


"""*WRITE CLEAR COLOR USING TUPLE*"""
def PixelsWriteColorToGl( color : tuple[4] ):
    col = color
    glClearColor( col[0], col[1], col[2], col[3] )
    
    
COLOR_GRID_BACKGROUND = ( 255.0, 255.0, 255.0, 0.0 )
COLOR_GRID_BLOCK = ( 0.0, 0.0, 0.0, 0.0 )
COLOR_SELBRUSHES = ( 255.0, 0.0, 0.0, 0.65 )
COLOR_SELLINE = ( 255.0, 255.0, 255.0, 0.0 )
COLOR_SELBRUSH2D = ( 255.0, 0.0, 0.0, 0.0 )
COLOR_NOSELBRUSH2D = ( 255.0, 255.0, 255.0, 0.0 )
COLOR_CAMERA_BACKGROUND = ( 0.30, 0.30, 0.30, 0.0 )

REQ_MAX_BRUSH_COUNT = int

VIEW_XY = int
VIEW_XZ = int
VIEW_YZ = int