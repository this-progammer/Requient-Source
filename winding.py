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
from mathvec import vec3_t, vec4_t, vec2_t, vec_t

class Winding:
    
    windingPoints = [8.0]
    numpoints = int
    
    winding_x = vec3_t
    winding_y = vec3_t
    winding_z = vec3_t
    
    # winding order cw, ccw
    winding_order_cw = int
    winding_order_ccw = int

    rotation = vec3_t
    
    plane_texcoords = vec2_t
    
    bChopped = bool
    # what angle is the plane winding
    w_ang = vec3_t
    
    m_nSelVertex = int # select vertex
    
    bIsBounded = bool
    
    
    """select plane vertex"""
    def SelVertex( vert ):
        #quick chck
        if vert == 0:
            return #dont get degenerate point
        else:
            for vert in range( 0 ):
                print( vert )                
    
    """free the winding"""    
    def Free_Winding( self ):
        del( self )
    
    
def getWinding( w : Winding ):
    return w

def getWindingNumericId( w : Winding )->int:
    return w.windingId
