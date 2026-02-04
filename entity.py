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

from collision import*

class EntityWorldClass:
    
    entityId = int
    entityOwner = [1] # brush owner or model owner
    entitydef = ""

def getEntity( entity : EntityWorldClass ):
    return entity

"""*get the entity id*"""
def entityNumericalValue( entity : EntityWorldClass, id : int ):
    return entity.entityId == id

"""*link the entity to the entity*"""
def entityOwnerLink( entity : EntityWorldClass, owner : EntityWorldClass ):
    return entity.entityId == owner.entityId

"""*increment reference*"""
def entityRefInc( entity : EntityWorldClass ):
    return ++entity.entityId

"""*decrement reference*"""
def entityRefDec( entity : EntityWorldClass ):
    return --entity.entityId

"""*entity model extension*"""
def entity_extension_def( entity : EntityWorldClass )->str:
    return entity.entitydef == ".fbx"

def entity_collsionDetection( entity : EntityWorldClass ):
    epsilon = 00.1 # just barely touching
    m_Collision = Collision()
    
    getEntity( entity )
    getCollisionClass( m_Collision )

    
    
    