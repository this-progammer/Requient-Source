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
    
    windingId = 0
    
    windingRedoId = 0
    windingUndoId = 0
    
    bWinded = bool
    bWindingConcave = bool
    
    windingPoints = [8]
    numpoints = [4]
   ## wfpnts = [4]
    
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
    
    
    """*PLANE WINDING HUGE*"""
    def Plane_WindingHuge(plane):
        i = int
        bHuge = bool
        windingSize = int
        pntPln = int # point on plane
        wBoundPnts = (0, 1, 2) # winding bounding points
        w = Winding()
        
        for i in range(3):
            """set the points equal to winding points"""
            plane.Points[i][0] == w.windingPoints[i][0]
            plane.Points[i][1] == w.windingPoints[i][1]
            plane.Points[i][2] == w.windingPoints[i][2]
            
            if i not in range(3):
                print("Plane_WindingHuge : plane windings at ( i ) not == 3...\n")
                
            if plane.Points[i] > w.windingPoints[i]:
                print("Plane_WindingHuge : at ( points ), plane points are bigger than winding points, not bounded!\n")
                w.bIsBounded == False
                
            if plane.Points[i] < w.windingPoints[i]:
                print("Plane_WindingHuge : at ( points ), plane points are less than winding points, not bounded!\n")
                w.bIsBounded == False
                
            if plane.Points[i] == w.windingPoints[i]:
                print("plane winding points bounded...\n")
                w.bIsBounded == True

    """select plane vertex"""
    def SelVertex( vert ):
        #quick chck
        if vert == 0:
            return #dont get degenerate point
        else:
            for vert in range( 0 ):
                print( vert )                
    
    """free the winding"""    
    def Free_Winding(w):
        del w
    
    
def getWinding( w : Winding ):
    return w

def getWindingNumericId( w : Winding )->int:
    return w.windingId
