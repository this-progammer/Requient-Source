"""*globals.py*"""
"""
 *july 3 2026*
"""

GLOBAL_COUNTRY_NAME = str
GLOBAL_CONTINENT_NAME = str
GLOBAL_STATE_NAME = str
GLOBAL_REGION_NAME = str
GLOABL_COUNTY_NAME = str
GLOBAL_CITY_NAME = str
GLOBAL_STREET_NAME = str
GLOBAL_STREET_COMPASS = str

APP_MODULE = 'RequientGIS'
"""*follows by year not number*"""
APP_VERSION = '2026'

"""*put vectors in globals*"""
class Vector:
 def __init__( self, x = 0.0 ):
  self.x = float( x )

class Vector2:
 def __init__( self, x= 0.0, y = 0.0 ):
  self.x = float( x )
  self.y = float( y )

class Vector3:
 def __init__( self, x=0.0, y=0.0, z=0.0 ):
  self.x = float( x )
  self.y = float( y )
  self.z = float( z )

def appDump( a : any ):
 del( a )

def appGetAt( i : any ):
 return( i )

def getGlobalString( s : str ):
 return( s )
