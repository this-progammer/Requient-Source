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

from box import*

# uses the brush box class, cause nodes are colors and not textured
class EntityNodeTypePath(BrushBox):
    m_NodeBox = BrushBox()
    m_fNodeColor = vec3_t
    m_fNodePosition = vec3_t
    m_bNodeScalable = bool # should always be false
    m_bSelNode = bool
    m_bTransformable = bool
    m_bTransformed = bool # note : nodes cannot be scaled
    
    # get the node brush box
    def getNodeBrushBox( box : BrushBox ):
        return box
    
    
def getNodeColor( node : EntityNodeTypePath ):
    return node.m_fNodeColor

def getNodePosition( node : EntityNodeTypePath ):
    return node.m_fNodePosition

# box's dont use the winding class
def queueNodeDraw( node : EntityNodeTypePath ):
    return node.boxpoints

# select node
def selectNode( node : EntityNodeTypePath ):
    return node.m_bSelNode == True

def getNode( node : EntityNodeTypePath ):
    return node
