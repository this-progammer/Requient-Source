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
    faceSelected = bool
    
    planes = [facePlane1, facePlane2]
    
    # may discard or use for other things
    def WindingMakeFace(self):
        
        """*Make 2 planes*"""
        planeA = Plane3()
        planeB = Plane3()
        
        """set them equal to face planes"""
        planeA = self.facePlane1
        planeB = self.facePlane2
        
        """*set points equal to the winding points*"""
        for i in range( 18 ):
            planeA.Points[i][3] == planeA.winding.windingPoints[i][3]
            planeB.Points[i][6] == planeB.winding.windingPoints[i][6]
            self.pointA[i][0] == planeA.Points[i][0]
            self.pointB[i][1] == planeA.Points[i][1]
            self.pointC[i][2] == planeA.Points[i][2]
            self.pointD[i][3] == planeB.points[i][6]
    
    
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
    


#==================
#   BrushWinding_Face( )
def BrushWinding_Face( face : Face ):
    # point list
    plst_ptr = ( [ int ] )
    
    pFaceLeftBound = vec3_t
    pFaceRightBound = vec3_t
    
    P = Plane3
    FACE = face
    
    FACE = Alloc_Face()
    
    w = Winding
    
    for i in range( 4 ):
        w.wfpnts[i][0] = FACE.facePoints[i][0]
        w.wfpnts[i][1] = FACE.facePoints[i][1]
        w.wfpnts[i][2] = FACE.facePoints[i][2]
        w.wfpnts[i][3] = FACE.facePoints[i][3]
        
        # stor points in list
        plst_ptr[w.wfpnts[i][4]]      
                    
                
        
    