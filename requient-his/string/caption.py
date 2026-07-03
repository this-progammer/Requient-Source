"""*caption.py*"""
"""*july 3 2026*"""

CAPTION_MAJOR = 'caption'
CAPTION_VERSION = '1.0.0'

class Caption:
  def __init__( self, lbl : str ):
    self.lbl = lbl

  def createNewCaption( self, label : str ):
    self.__init__( label )

  def getCaption( self ):
    return self
