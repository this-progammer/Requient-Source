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

TEXTURE_FLAG_CAULK = 27
TEXTURE_FLAG_BOT_CLIP = 37
TEXTURE_FLAG_BOT_ZONE = 67 # haha, get it

class TextureFlagsDomain:
    def getTextureFlag( flag : int )->int:
        return flag
    
    
def getTextureFlagDomain( domain : TextureFlagsDomain ):
    return domain