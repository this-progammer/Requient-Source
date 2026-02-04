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

"""_summary_
Praise The Lord For My Code,

This file is for mouse bindings and other such as grid events, etc.
"""

from mathvec import*
from global_stream import*

MOUSE_BUTTON_MAJOR = 'Mouse Binding'

MB_LEFT = 0x10
MB_RIGHT = 0x20
MB_UP = 0x30
MB_DOWN = 0x40

MB_LEFT_DRAG_CLICK = MB_LEFT + MB_DOWN + 0x300

MOUSE_SCROLL_IN = 0x800
MOUSE_SCROLL_OUT = 0x900

CTRL = 0x50

MOUSE_DRAG_DIR = vec3_t

