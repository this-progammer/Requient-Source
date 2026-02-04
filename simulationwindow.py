
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

from subprocess import*
from map import*

# not its own seperate app, opens a terminal
class SimulationWindow:
     #uses command prompt
    terminal_app_name = 'C:\\WINDOWS\\system32\\cmd.exe'
    terminal_proc = Popen(terminal_app_name, shell= True)


def getSimulationWindow( window : SimulationWindow ):
    return window

    
def runMapTerminal(map : MapDocument, simulation : SimulationWindow):
        # open map
        for map in simulation:
            simulation.terminal_proc.stdout == "app\\openmap.bat"