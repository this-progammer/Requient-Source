
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
#do sum imports
from camwnd import*
from xywnd import*
from yzwnd import*
from xzwnd import*
from map import*
from subprocess import*
import sys
from PyQt5.QtWidgets import*
from bsp import*
from aabb import*
from collision import*
from caulk import*
from scenegraph import*
from brush_primit import*
from brushlist import*
from texflagswindow import*

DARK_STYLESHEET = """
/* Base */
QWidget {
background-color: #255, 255, 255;
color: #RGB;
font-family: Requiem;
font-size: 10.5pt;
}
}
"""

#=========*APP INSTANCE*========
d_AppInstance = QApplication([])    # *MUST INIT APP FIRST OR WINDOW WILL NOT SHOW*



#=========*APP STYLE*===========
d_AppInstance.setStyle('Fusion')




#==============*GLOBALS*================
g_MapDocHandler = MapDocument()





#========*APP WIDGETS*==========
d_MainWindow = QWidget()

d_CameraWindow = CameraWnd()

d_XYWindow = XYWnd()


d_XZWindow = XZWnd()


d_YZWindow = YZWnd()

d_Menubar = QMenuBar( d_MainWindow )
d_ConsoleWindow = QWidget()


"""
*ENABLE EVENTS FOR THE GRID WINDOWS TO BE ALLOWED*
"""
def EnableXYWindow():
    d_XYWindow.setEnabled( True )
    d_XYWindow.setMouseTracking( True )
    d_XZWindow.setEnabled( True )
    d_XZWindow.setMouseTracking( True )
    d_YZWindow.setEnabled( True )
    d_YZWindow.setMouseTracking( True )
    
# ENABLE XY DRAW
EnableXYWindow()

#===========*MAINWINDOW CODE*=============
d_MainWindow.setWindowTitle( 'Requient' )
d_MainWindow.resize( 1000, 1000 )
d_AppInstance.setStyleSheet( DARK_STYLESHEET )


#===========*ADD ALL WIDGETS TO MAIN*=================
#FIRST MAKE PANES, SO WE CAN RESIZE THE WINDOWS
layout = QVBoxLayout()
d_MainWindow.setLayout( layout )

# --- Original 4-view splitter ---
views_splitter = QSplitter( Qt.Vertical )

top_pane = QSplitter( Qt.Horizontal )
top_pane.addWidget( d_XYWindow )
top_pane.addWidget( d_CameraWindow )
top_pane.setFrameStyle( QFrame.Panel | QFrame.Sunken )
top_pane.setLineWidth(1)

bottom_pane = QSplitter( Qt.Horizontal )
bottom_pane.addWidget( d_XZWindow )
bottom_pane.addWidget( d_YZWindow )
bottom_pane.setFrameStyle( QFrame.Panel | QFrame.Sunken )
bottom_pane.setLineWidth(1)

views_splitter.addWidget( top_pane )
views_splitter.addWidget( bottom_pane )
views_splitter.setFrameStyle( QFrame.Panel | QFrame.Sunken )
views_splitter.setLineWidth(1)

# --- Main splitter: top = views, bottom = console ---
main_splitter = QSplitter( Qt.Vertical )
main_splitter.addWidget( views_splitter )  # Top: 4 views

d_ConsoleWindow = QTextEdit()
d_ConsoleWindow.setPlaceholderText("Requient Console...")
d_ConsoleWindow.setReadOnly(False)  # Optional: make it read-only
d_ConsoleWindow.setFrameStyle( QFrame.Panel | QFrame.Sunken )
d_ConsoleWindow.setLineWidth(1)
d_ConsoleWindow.acceptRichText() == True

iotext = sys.stdout

main_splitter.addWidget( d_Menubar )
main_splitter.addWidget( d_ConsoleWindow )  # Bottom: console

# Optional: set initial sizes (top bigger than console)
main_splitter.setSizes( [600, 150] )

# Add main splitter to the layout
layout.addWidget( main_splitter )
#=======================*=========================
d_ConsoleWindow.insertPlainText('XY Active\n')
d_ConsoleWindow.insertPlainText('XZ Active\n')
d_ConsoleWindow.insertPlainText('YZ Active\n')
d_ConsoleWindow.insertPlainText('No Brushes Selected... Select A Brush\n')

def GL_PrintChk():
    if(d_CameraWindow == 0):
        d_ConsoleWindow.insertPlainText('GL Paint Context Failed...\n')
    else:
        d_ConsoleWindow.insertPlainText('GL Paint Context Enabled...\n')
        d_ConsoleWindow.insertPlainText('GL_DEPTH Running...\n')
        d_ConsoleWindow.insertPlainText('GL_CLEAR_COLOR | GL_DEPTH_BUFFER_BIT Running...\n')
        d_ConsoleWindow.insertPlainText('GL Queueing Brush Drawing...\n')
        d_ConsoleWindow.insertPlainText("glClearColor(r, g, b, 1.0), glEnable(GL_DEPTH_TEST) glDepthFunc(GL_LEQUAL) glDisable(GL_CULL_FACE) glEnable(GL_BLEND) glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA) glEnable(GL_LINE_SMOOTH) glHint(GL_LINE_SMOOTH_HINT, GL_NICEST) glEnable(GL_POLYGON_SMOOTH) glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)")

GL_PrintChk()

#===========*MENU_ACTIONS*===================

def __CODE_WHT()->str:
    return "WHITE"

def __CODE_BLK()->str:
    return "BLACK"


def XYPaintWhite():
    g_reqglobals.d_globalWin32Scheme = True
    
def XYPaintBlack():
    g_reqglobals.d_globalBlackScheme = True


def SenderMenuMessage():
    print("MESSAGE SENT TO MENU")

#==================*MENU*=========================
menu = d_Menubar
    
file_menu = menu.addMenu("&File")
edit_menu = menu.addMenu("&Edit")
misc_menu = menu.addMenu("&Misc")
grid_menu = menu.addMenu("&Grid")    
textures_menu = menu.addMenu("&Textures")
brush_menu = menu.addMenu("&Brush")
selection_menu = menu.addMenu("&Selection")
primit_menu = menu.addMenu("&Primitive")
spawn_menu = menu.addMenu("&Spawn")
help_menu = menu.addMenu("&Help")
flags_menu = menu.addMenu("&Flags")
    
    #===========*FILE_MENU*===================
open_map = QAction("Open Map File", file_menu)
file_menu.addAction( open_map )
    
save_map = QAction("Save Map File", file_menu)
file_menu.addAction( save_map )
    
exit_map = QAction("Exit Map", file_menu)
file_menu.addAction( exit_map )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #================*EDIT_MENU*==============
robotic_mdl_format = QAction( "Robotic Model Format", edit_menu )
edit_menu.addAction( robotic_mdl_format )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #===============*MISC_MENU*===============
    
grid_color = QMenu( misc_menu )
misc_menu.addMenu( grid_color )
grid_color.setTitle("Grid Background Color")
bkgrnd_w_col = QAction( "White", grid_color )    
grid_color.addAction( bkgrnd_w_col )
    
    
bkgrnd_b_col = QAction( "Black", grid_color )
grid_color.addAction( bkgrnd_b_col ) 
    
    #==========================================
    
grid_block_color = QAction( "Grid Block Color", misc_menu )
misc_menu.addAction( grid_block_color )

brush_sel_color = QAction( "Brush Selection Color", misc_menu )
misc_menu.addAction ( brush_sel_color )
    
camera_color = QAction( "Camera Background Color", misc_menu )
misc_menu.addAction( camera_color )
    
model_sel_color = QAction( "Model Selection Color", misc_menu )
misc_menu.addAction( model_sel_color )    
    
workzone_color = QAction( "Workzone Block Color", misc_menu )
misc_menu.addAction( workzone_color )
    
    
    
    
    
    
    #================*GRID_MENU*==================
grid_8 = QAction( "Grid 8", grid_menu )
grid_menu.addAction( grid_8 )
    
    
    
    
    
    
    
    
    
    
    
    
    #=====================*SPAWN_MENU*===================
spawn_path_node = QAction("Path Node", spawn_menu)
spawn_path_node.triggered.connect(d_CameraWindow.update)
spawn_menu.addAction(spawn_path_node)    
    
spawn_script_node = QAction("Script Node", spawn_menu)
spawn_script_node.triggered.connect(d_CameraWindow.update)
spawn_menu.addAction(spawn_script_node)
    
spawn_esp = QAction("ESP MaxArm Robotic", spawn_menu)
spawn_esp.triggered.connect(d_CameraWindow.update)
spawn_menu.addAction( spawn_esp )
    
    #=========*TEXTURES_MENU*======================
texture_dir = QAction( "Texture Directory", textures_menu )
textures_menu.addAction( texture_dir )
    
caulk_tex = QAction( "Caulk Texture", textures_menu )
textures_menu.addAction( caulk_tex )


tex_wnd = QAction( "Texture Window", textures_menu )
textures_menu.addAction( tex_wnd )
        
        
        
        
    #===========*BRUSH_MENU*=======================
auto_caulk_brush = QAction( "Auto Caulk Brushes", brush_menu )
brush_menu.addAction( auto_caulk_brush )
    
brush_no_collision = QAction( "Brush No Collision", brush_menu )
brush_menu.addAction( brush_no_collision )

    #===============*SELECTION_MENU*================================
sel_all_brushes = QAction( "Select All Brushes", selection_menu )
selection_menu.addAction( sel_all_brushes )
    
dis_sel = QAction( "Disable Selecting", selection_menu )
selection_menu.addAction( dis_sel )
    
    #====================*FLAGS_MENU*===============================
clip_flag = QAction( "TEX_FLAG_CLIP", flags_menu )
flags_menu.addAction( clip_flag )
    
trigger_flag = QAction( "TEX_FLAG_TRIGGER", flags_menu )
flags_menu.addAction( trigger_flag )
    
    #==================PRIMIT MENU==========================
cube = QAction( "Cube", primit_menu )
primit_menu.addAction( cube )
    
box = QAction( "Bounding Box", primit_menu )
primit_menu.addAction( box )
    
#=========*CALL MENU CONSTRUCTION EVENT*==========

def EnableConsoleOutput():
    console = d_ConsoleWindow
    

d_MainWindow.show()
d_AppInstance.exec()