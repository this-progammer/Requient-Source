"""*login.py*"""
"""*july 3 2026*"""

debug_kernel_gui()

class Login:
  def __init__( self, window ):
    self.window = dkg().api.Window

  def createLoginPage( self ):
    return self.__init__( self, _PTR )

  m_stringUsername = str
  m_stringPassword = str
  m_boolLoginCredintialsValid = bool

  def getLoginPage( self ):
    return self

  def checkUserLogin( self ):
    if self.m_stringUsername != True:
      return assert( -1 )
      
    if self.m_stringPassword != True:
      return assert( -1 )

    else:
      pageNextWindow()
