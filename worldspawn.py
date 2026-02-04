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

from map import*

WORLDSPAWN_CLASS_BRUSH = 32
WORLDSPAWN_CLASS_ENTITY = 64
WORLDSPAWN_CLASS_NODE = 86


class WorldSpawnClass:
    
    m_pWrldSpwnLiteral = ''
    m_pWrldSpwnKey = ''
    m_PWrldSpwnValue = ''
    
def getWorldClassBrush()->int:
    return WORLDSPAWN_CLASS_BRUSH

def getWorldClassEntity()->int:
    return WORLDSPAWN_CLASS_ENTITY

def getWorldClassNode()->int:
    return WORLDSPAWN_CLASS_NODE

def getWorldClassModule( spawner : WorldSpawnClass ):
    return spawner

def getWorldClassLiteral( spawner : WorldSpawnClass )->str:
    return spawner.m_pWrldSpwnLiteral

def getWorldClassKey( spawner : WorldSpawnClass )->str:
    return spawner.m_pWrldSpwnKey

def getWorldClassValue( spawner : WorldSpawnClass )->str:
    return spawner.m_PWrldSpwnValue

def setWorldTypeLiteral( spawner : WorldSpawnClass, literal : str ):
    spawner.m_pWrldSpwnLiteral == literal
    
def setWorldTypeKey( spawner : WorldSpawnClass, key : str ):
    spawner.m_pWrldSpwnKey == key
    
def setWorldTypeValue( spawner : WorldSpawnClass, value : str ):
    spawner.m_PWrldSpwnValue == value

