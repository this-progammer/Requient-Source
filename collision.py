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

#Jesus loves you, Amen

#is the robot just barely colliding to a surface???
NEAR_COLLISION_EPSILLION = 00.1

class Collision:
    
    collisionId = 0
    bCollided = bool
    
    def SetCollision():
        any()

    def SetPhysics():
        any()
        
def getCollisionClass( c : Collision ):
    return c

def getCollisionId( c : Collision)->int:
    return c.collisionId

def checkCollisionRayHit( c : Collision )->bool:
    return c.bCollided == True

def signalSetCollisionEvent( cxl : Collision ):
    cxl.SetCollision()
    
def signalSetPhysicsEvent( cxl : Collision ):
    cxl.SetPhysics()
