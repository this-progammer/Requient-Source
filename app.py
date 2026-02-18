
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
font-family: Consolas;
font-size: 10.5pt;
}
}
"""


GRIDPOWER_32 = 32
GRIDPOWER_64 = 64
GRID_POWER_86 = 86
GRID_POWER_1024 = 1024




#=========*APP INSTANCE*========
d_AppInstance = QApplication([])    # *MUST INIT APP FIRST OR WINDOW WILL NOT SHOW*



#=========*APP STYLE*===========
d_AppInstance.setStyle("Fusion")




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
main_splitter.setLineWidth(6)

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
        d_ConsoleWindow.insertPlainText("glClearColor(r, g, b, 1.0), \nglEnable(GL_DEPTH_TEST) \nglDepthFunc(GL_LEQUAL) \nglDisable(GL_CULL_FACE) \nglEnable(GL_BLEND) \nglBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA) \nglEnable(GL_LINE_SMOOTH) \nglHint(GL_LINE_SMOOTH_HINT, GL_NICEST)\n glEnable(GL_POLYGON_SMOOTH) \nglHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)\n")

GL_PrintChk()


"*Key Handler*"
class MainFrameSender( QWidget ):
    
    _sender = set()
    
    def keyPressEvent(self, a0):
        self._sender.add(a0.key())
    
    def keyReleaseEvent(self, a0):
        self._sender.discard(a0.key())
        
    def KeyPressL( self ):
        return Qt.Key.Key_L
                    

#===========*MENU_ACTIONS*===================

def __CODE_WHT()->str:
    return "WHITE"

def __CODE_BLK()->str:
    return "BLACK"


def XYPaintWhite():
    globalREQGlobalsManager().d_globalWin32Scheme = True
    
def XYPaintBlack():
    globalREQGlobalsManager().d_globalBlackScheme = True


def SenderMenuMessage():
    print("MESSAGE SENT TO MENU")

#==================*MENU*=========================
menu = d_Menubar
    
file_menu = menu.addMenu("&File")
edit_menu = menu.addMenu("&Edit")
map_menu = menu.addMenu("&Map")
misc_menu = menu.addMenu("&Misc")
grid_menu = menu.addMenu("&Grid")    
textures_menu = menu.addMenu("&Textures")
brush_menu = menu.addMenu("&Brush")
selection_menu = menu.addMenu("&Selection")
primit_menu = menu.addMenu("&Primitive")
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
"""*need to seriously organize my code, but in a hurry per usual"""
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
"""The Do_() funcs just a quick cut to change grid size past normal zoom"""
def Do_XY32():
    d_XYWindow.cell_size = globalXYManager().cell_size = 32
    UpdateGLWindow( d_XYWindow )
    d_ConsoleWindow.insertPlainText("XY Grid Size : 32\n")
    
    d_XZWindow.cell_size = globalXZManager().cell_size = 32
    UpdateGLWindow( d_XZWindow )
    d_ConsoleWindow.insertPlainText("XZ Grid Size : 32\n")
    
    d_YZWindow.cell_size = globalYZManager().cell_size = 32
    UpdateGLWindow( d_YZWindow )
    d_ConsoleWindow.insertPlainText("YZ Grid Size : 32\n")
    
def Do_XY16():
    d_XYWindow.cell_size = globalXYManager().cell_size = 16
    UpdateGLWindow( d_XYWindow )
    d_ConsoleWindow.insertPlainText("XY Grid Size : 16\n")
    
    d_XZWindow.cell_size = globalXZManager().cell_size = 16
    UpdateGLWindow( d_XZWindow )
    d_ConsoleWindow.insertPlainText("XZ Grid Size : 16\n")
    
    d_YZWindow.cell_size = globalYZManager().cell_size = 16
    UpdateGLWindow( d_YZWindow )
    d_ConsoleWindow.insertPlainText("YZ Grid Size : 16\n")
    
def Do_XY64():
    d_XYWindow.cell_size = globalXYManager().cell_size = 64
    UpdateGLWindow( d_XYWindow )
    d_ConsoleWindow.insertPlainText("XY Grid Size : 64\n")
    
    d_XZWindow.cell_size = globalXZManager().cell_size = 64
    UpdateGLWindow( d_XZWindow )
    d_ConsoleWindow.insertPlainText("XZ Grid Size : 64\n")
    
    d_YZWindow.cell_size = globalYZManager().cell_size = 64
    UpdateGLWindow( d_YZWindow )
    d_ConsoleWindow.insertPlainText("YZ Grid Size : 64\n")

def Do_XY128():
    d_XYWindow.cell_size = globalXYManager().cell_size = 128
    UpdateGLWindow( d_XYWindow )
    d_ConsoleWindow.insertPlainText("XY Grid Size : 128\n")
    
    d_XZWindow.cell_size = globalXZManager().cell_size = 128
    UpdateGLWindow( d_XZWindow )
    d_ConsoleWindow.insertPlainText("XZ Grid Size : 128\n")
    
    d_YZWindow.cell_size = globalYZManager().cell_size = 128
    UpdateGLWindow( d_YZWindow )
    d_ConsoleWindow.insertPlainText("YZ Grid Size : 128\n")
    
def Do_XY1024():
    d_XYWindow.cell_size = globalXYManager().cell_size = 1024 / 2
    UpdateGLWindow( d_XYWindow )
    d_ConsoleWindow.insertPlainText("XY Grid Size : 1024\n")
    
    d_XZWindow.cell_size = globalXZManager().cell_size = 1024 /2 
    UpdateGLWindow( d_XZWindow )
    d_ConsoleWindow.insertPlainText("XZ Grid Size : 1024\n")
    
    d_YZWindow.cell_size = globalYZManager().cell_size = 1024 /2 
    UpdateGLWindow( d_YZWindow )
    d_ConsoleWindow.insertPlainText("YZ Grid Size : 1024\n")

# connect Do_() funcs
grid_32 = QAction( "Grid 32", grid_menu )
grid_menu.triggered.connect( Do_XY32 )
grid_menu.addAction( grid_32 )

grid_16 = QAction("Grid 16", grid_menu)
grid_menu.triggered.connect( Do_XY16 )
grid_menu.addAction( grid_16 )

grid_64 = QAction("Grid 64", grid_menu)
grid_menu.triggered.connect( Do_XY64 )
grid_menu.addAction( grid_64 )

grid_128 = QAction("Grid 128", grid_menu)
grid_menu.triggered.connect( Do_XY128 )
grid_menu.addAction( grid_128 )

grid_1024 = QAction("Grid 1024", grid_menu)
grid_menu.triggered.connect( Do_XY1024 )
grid_menu.addAction( grid_1024 )
    
    
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

def Auto_Caulk_Brushes_Command():pass

def _sender_do_auto_caulk_print():
    Auto_Caulk_Brushes_Command()
    d_ConsoleWindow.insertPlainText("Auto Caulking For Brushes : On...\n")

def Do_AutoCaulk_BrushConsole():
    if auto_caulk_brush.triggered.connect(_sender_do_auto_caulk_print):
        return
        
Do_AutoCaulk_BrushConsole()
    
brush_no_collision = QAction( "Brush No Collision", brush_menu )
brush_menu.addAction( brush_no_collision )

def Brush_No_Collision_Command():pass

def _sender_do_no_collision_print():
    Brush_No_Collision_Command()
    d_ConsoleWindow.insertPlainText("Brush Set No Collision...\n")

def Do_NoCollisionBrush_Console():
    if brush_no_collision.triggered.connect(_sender_do_no_collision_print):
        return

Do_NoCollisionBrush_Console()
    #===============*SELECTION_MENU*================================
sel_all_brushes = QAction( "Select All Brushes", selection_menu )
selection_menu.addAction( sel_all_brushes )

def Select_All_Brushes_Command():pass

def _sender_sel_brushes_print():
    Select_All_Brushes_Command()
    d_ConsoleWindow.insertPlainText("Selected All Brushes...\n")

def Do_SelAllBrushes_Console():
    if sel_all_brushes.triggered.connect(_sender_sel_brushes_print):
        return
    
Do_SelAllBrushes_Console()
    
dis_sel = QAction( "Disable Selecting", selection_menu )
selection_menu.addAction( dis_sel )

def Disable_Selection_Command(): pass

def _sender_dis_sel_print():
    Disable_Selection_Command()
    d_ConsoleWindow.insertPlainText("Disables Brush And Entity Selecting...\n")
    
def Do_DisSelection_Console():
    if dis_sel.triggered.connect(_sender_dis_sel_print):
        return
    
Do_DisSelection_Console()
    #====================*FLAGS_MENU*===============================
clip_flag = QAction( "TEX_FLAG_CLIP", flags_menu )
flags_menu.addAction( clip_flag )

def Texture_Flag_Clip_Command():pass

def _sender_clip_flag_print():
    Texture_Flag_Clip_Command()
    d_ConsoleWindow.insertPlainText("Brush Texture Flag << Clip...\n")
    
def Do_TexFlagClip_Console():
    if clip_flag.triggered.connect(_sender_clip_flag_print):
        return
    
Do_TexFlagClip_Console()
    
trigger_flag = QAction( "TEX_FLAG_TRIGGER", flags_menu )
flags_menu.addAction( trigger_flag )

def Texture_Flag_Trigger_Command():pass

def _sender_trig_flag_print():
    Texture_Flag_Trigger_Command()
    d_ConsoleWindow.insertPlainText("Brush Texture Flag << Trigger...\n")

def Do_TexFlagTrig_Console():
    if trigger_flag.triggered.connect(_sender_trig_flag_print):
        return
    
Do_TexFlagTrig_Console()

caulk_flag = QAction( "TEX_FLAG_CAULK", flags_menu )
flags_menu.addAction( caulk_flag )

def Texture_Flag_Caulk_Command():pass

def _sender_caulk_flag_print():
    Texture_Flag_Caulk_Command()
    d_ConsoleWindow.insertPlainText("Brush Texture Flag << Caulk...\n")
    
def Do_TexFlagCaulk_Console():
    if caulk_flag.triggered.connect(_sender_caulk_flag_print):
        return
    
Do_TexFlagCaulk_Console()
    
    #==================PRIMIT MENU==========================
cube = QAction( "Cube", primit_menu )
primit_menu.addAction( cube )
    
box = QAction( "Bounding Box", primit_menu )
primit_menu.addAction( box )
    
#=========*CALL MENU CONSTRUCTION EVENT*==========

def EnableConsoleOutput():
    console = d_ConsoleWindow
    




"""
/*
=================================
    SetViews()
=================================
*/
"""
def SetViews():
    
    if VIEW_XY:
        ( d_XYWindow ).setEnabled(True)
        REQUIENT_MESSAGE("VIEWTYPE XY ", d_XYWindow)
    if VIEW_XZ:
        ( d_XZWindow ).setEnabled(True)
        REQUIENT_MESSAGE("VIEWTYPE XZ", d_XZWindow)
        
    if VIEW_YZ:
        ( d_YZWindow ).setEnabled(True)
        REQUIENT_MESSAGE("VIEWTYPE YZ", d_YZWindow)

SetViews()

def AquirePath_Requient():
    if Requient_ShadersPath != "Requient//common//textures//":
        d_ConsoleWindow.insertPlainText("Requient Path Error : Texture Directory, Directory Should Be, (Requient//common//textures//)\n")

AquirePath_Requient()

def Do_WorldCoordConsole():
    if g_MinWorldCoord == g_MaxWorldCoord:
        d_ConsoleWindow.insertPlainText("Map Error : Min_World Coordinates == Max_World Coordinates\n")
    else:
        d_ConsoleWindow.insertPlainText("Global World Coordinates : Min_World Coord : -65536.0, Max_World Coord : 65536.0 \n")
        
Do_WorldCoordConsole()

def OrthoResizes_Console():
    if d_XYWindow != [(d_XYWindow)]:
        d_ConsoleWindow.insertPlainText("globalXYManger().XYOrthoViewport Resized...\n")

#Allow user to zoom in grids with console
def Console_ZoomInPrompt()->str:
    return "ZoomIn"

# not working dont have time to debug.. in a hurry... Gomez
def OrthoZoom_InDoConsole():
    if d_ConsoleWindow.textChanged == ( Console_ZoomInPrompt ):
        d_XYWindow.XYZoomIn()
        
OrthoZoom_InDoConsole()

# do_hard_push of map directory
Requient_MapPath = "C://Requient//maps//"

def MainFrame_AquireMapPath( p : str ):
    def_path = "C://Requient//maps//"
    if p != def_path:
        REQUIENT_MESSAGE("Mainframe::MapPath::Failed()", p)
        d_ConsoleWindow.insertPlainText("Requient : Mainframe::MapPath::Failed()...\n")
    
    if p == def_path:
        d_MainWindow.setWindowTitle( def_path )
        d_ConsoleWindow.insertPlainText("Requient : Mainframe::MapPath::In::Use == C://Requient//maps//()... \n")
    if globalMapManager().mapDocName != ( 1 ):
        d_MainWindow.setWindowTitle( def_path + "unamed.reqmap1" )
        d_ConsoleWindow.insertPlainText("Map Unamed... Map Likely Not Saved...\n")
    else:
        d_MainWindow.setWindowTitle( def_path + g_CurrentMap.mapDocName )
    
MainFrame_AquireMapPath( Requient_MapPath )

def MapGet_Extension():
    return ".reqmap1"

# current map
g_CurrentMap = globalMapManager().mapDocName

# work in progress, open map, then display, then set title == map
def Do_MapDialog():
    m_dlg = QFileDialog( d_MainWindow )
    m_title = "Open Map File..."
    m_dir = Requient_MapPath
    m_name = globalMapManager().mapDocName
    
    m_dlg.setNameFilter("*.reqmap1")
    m_dlg.AcceptMode.AcceptOpen
    m_dlg.getOpenFileName( d_MainWindow, "Open Map File...", m_dir, "*.reqmap1" )
    m_dlg.setDirectory( m_dir )

    
def Command_OpenMapDialog():
    if open_map.triggered.connect( Do_MapDialog ): 
        return
    
Command_OpenMapDialog()

def Do_CaulkToolMessage():
    d_ConsoleWindow.insertPlainText("Caulk-Tool : Active...\n")
    
Do_CaulkToolMessage()

def Do_EntityToolMessage():
    d_ConsoleWindow.insertPlainText("Entity-Tool : Active...\n")

Do_EntityToolMessage()

def Do_BrushToolMessage():
    d_ConsoleWindow.insertPlainText("Brush-Tool : Active...\n")
    
Do_BrushToolMessage()

def Do_SelectToolMessage():
    d_ConsoleWindow.insertPlainText("Selection-Tool : Active...\n")
    
Do_SelectToolMessage()

def Do_OrthoToolMessage():
    d_ConsoleWindow.insertPlainText("Ortho-Tool( XY, XZ, YZ ) : Active...\n")
    
Do_OrthoToolMessage()

def Do_CameraToolMessage():
    d_ConsoleWindow.insertPlainText("Camera-Tool : Active...\n")
    
Do_CameraToolMessage()

def Do_MouseToolMessage():
    d_ConsoleWindow.insertPlainText("Mouse-Tool : Active...\n")
    
Do_MouseToolMessage()

def XY_MouseDragToolSender():
    return
    
XY_MouseDragToolSender()

"""*Map Layers Window Class*"""
class MapLayers:
    number_layers = int
    layers_view = QDialog( d_MainWindow )
    layers_view_title = "Map Layers"
    layer_item = QTextItem()

globalMapLayersManager = MapLayers

"""*Create Layer Command*"""
def Do_LayerCommand():
    m_dlg = QInputDialog( d_MainWindow )
    m_dlg.resize( 400, 400 )
    m_dlg.setWindowTitle("New Map Layer")
    m_dlg.setLabelText("New Map Layer Name...")
    m_dlg.show()
    
def MapLayer_MenuAppendSender():
    m_sender = QAction("New Layer", map_menu)
    map_menu.addAction( m_sender )
    m_sender.triggered.connect( Do_LayerCommand )
    
MapLayer_MenuAppendSender()
    

g_XYWidth = int
g_XYHeight = int
g_XZWidth = int
g_YZWidth = int

d_MainWindow.show()
d_AppInstance.exec()