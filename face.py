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

from plane3 import*

class Face:
    
    facePlane1 = Plane3()
    facePlane2 = Plane3()
    
    winding = Winding()
    
    points = vec4_t
    
    texdef_literal = ("")
    
    """face points"""
    facePoints = [0, 0, 0, 0]
    pointA = facePoints[0]
    pointB = facePoints[1]
    pointC = facePoints[2]
    pointD = facePoints[3]
    faceBounds = vec3_t
    faceFlipped = bool
    """does the point go inside the bounds???"""
    facePointEpsilonBounds = bool
    
    fvectors = facePlane1.plnvecs and facePlane2.plnvecs
    
    faceTexCoords = vec2_t
    face_sel = bool
    
    planes = [facePlane1, facePlane2]
    
    
def free_face( f : Face ):
    del( f )
    
"""face winding order"""
def Face_BeginPlaneWinding(pF : Face):
        chopped = pF.winding.bChopped
        p1 = pF.facePlane1 # face plane 1
        p2 = pF.facePlane2 # face plane 2
        
        # make the planes first
        Winding_MakePlane( p1 )
        Winding_MakePlane( p2 )
        
        # now get their normal using the cross product method
        cross_product( p1.vA, p1.vB, p1.vC ) == p1.normal
        cross_product( p2.vA, p2.vB, p2.vC ) == p2.normal
        
        # now take plane 2 ( j ), winding it 90 degree's then take plane point[2] and snap it to plane 1 points[0]
        # then plane 2 point [0] and snap it to plane 1 point [2]
        """
            LOOKS LIKE THIS * 
            
            
            snap points 0 and 2 together
            
            [2]\     [0]_________[]
             | \     \           |
             |  \     \          |
             |   \     \         |
             |    \     \        |
             |     \     \       |
             |      \     \      |
             |       \     \     |  plane ( j )
             |        \     \    |
             []________[0]   [2]|   
            
            plane ( i )
             
            snap points 2 and 0 together
        """
        w = Winding()
        
        for i in range( 11 ):
                
            pnts = w.windingPoints[i]
            
            pnts[i][0] = p1.plnpnts[i][2][0]
            pnts[i][1] = p1.plnpnts[i][1][2]
            pnts[i][2] = p2.plnpnts[i][2][0]
            pnts[i][3] = p2.plnpnts[i][1][2]
            
        return pF
    
def getFace( f : Face ):
    return f

def Alloc_Face():
    f = Face
    sys.getsizeof( [ f ] )
    getFace( f )
    
    return f

def Do_FaceWinding( f : Face ):
    Face_BeginPlaneWinding( f )
        
    