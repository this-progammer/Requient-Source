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

class Camera:
    
    buf = 2048
    
    """
                |
                |    
                |
                |    
                |   y
                |
                |
                |
                |
                |
                |               x
                |_________________________________
               /
              /
             /
            /   z
           /             
          /
    """
    
    # position = 0.0, 0.0, 0.0
    
    #is x, y, z, pick one
    orientation = float
    
    #field of view
    fieldOfView = 45.0
    
    #depth view, like cubic clipping
    depthView = 100.0
    
    
    def MouseCameraWheelZoomIn():
        return
    
    def MouseCameraWheelZoomOut():
        return
    
    def MouseCameraLeftButton():
        return
    
    def MouseCameraRightButton():
        return
    
    def MouseCameraLeftDownButton():
        return
    
    def MouseCameraRightUpButton():
        return
    
    def DrawPlanes():
        any
    def DrawFaces():
        any
    def DrawBrushes():
        any
        
    def Sender(_func):
        _func
        
    # *!-dimensions-!*
    X = int
    Y = int
    W = int
    H = int
    
    origin = 0.0, 0.0, 0.0
    
    bFreeze = bool
    
    mouse_movposition = 0.0, 0.0, 0.0
    
    
    
    

def getCamera( camera : Camera ):
    return camera

def cameraGetOrigin( camera : Camera )->float:
    return camera.origin

def cameraSetOrigin( camera : Camera, ori : float ):
    camera.origin = ori
    
def cameraGetBuffer( camera : Camera )->int:
    return camera.cameraBuffer

def cameraSetBuffer( camera : Camera, buf : int ):
    camera.cameraBuffer = buf
    
def signalDestroyCamera( camera : Camera ):
    del camera
    
def signalCameraStateQueue( camera : Camera )->bool:
    return camera.bFreeze == True or False