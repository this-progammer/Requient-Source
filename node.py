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
"""node.py"""

from OpenGL.GL import*
from OpenGL.GLU import*

class Node:
    
    """
     *NOTE: Nice thing about nodes is they can be edited or scaled, so no faces or planes need just coords
    """
    
    def createPrimitNode():
        glTranslatef(1.0, -1.0, -5.0)
        glRotatef(90.0, 1.0, -1.0, -5.0)
        
        glColor3f(1.0, 0.4, 0.7)
        
        vertices = [
            [ 0.25,  0.25,  0.25], [ 0.25,  0.25, -0.25], [ 0.25, -0.25, -0.25], [ 0.25, -0.25,  0.25],
            [-0.25,  0.25,  0.25], [-0.25,  0.25, -0.25], [-0.25, -0.25, -0.25], [-0.25, -0.25,  0.25]
        ]
        faces = [
            [0, 1, 2, 3], [4, 5, 6, 7],
            [0, 4, 7, 3], [1, 5, 6, 2],
            [0, 1, 5, 4], [3, 2, 6, 7]
        ]

        
        glBegin(GL_POLYGON)
        for face in faces:
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()


def getNode( node : Node ):
    return node

def createPrimitiveNodeDummy( node : Node ):
    node.createPrimitNode()