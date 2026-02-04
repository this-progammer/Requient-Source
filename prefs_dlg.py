
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

"""*THE PAGE TO SET GLOBAL PREFERENCES*"""

from PyQt5.QtWidgets import*
from qesmatictypes import*

class PrefsPage(QWidget):
    
    X= int
    Y= int
    W= int
    H= int
    
    bPopup= bool
    
    def RequientSchemeWin32()->bool:
        g_reqglobals.d_globalWin32Scheme = True
        
    def RequientSchemeBlack()->bool:
        g_reqglobals.d_globalBlackScheme = True
        
        
    m_pageCaption = "Requient Preferences"    
        
    m_win32SchemeBox = QCheckBox()
    m_blackSchemeBox = QCheckBox()
    
    def m_funcCreatePage( self ):
        
        self.setWindowTitle(self.m_pageCaption)
        self.setFixedSize(400, 400)
        
        winBox = QCheckBox(self, "Win32 Scheme")
        winBox = self.m_win32SchemeBox
        
        
        self.show()