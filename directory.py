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
#app directory

class AppFileDirectory():
    FolderDirectory = str
    FolderSize = int
    FolderName = str
    FolderOpened = bool

class File:
    FileName = str
    FileExtension = str
    FileSize = int
    FileOpened = bool
    FileIcon = str