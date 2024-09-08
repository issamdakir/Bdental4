import os
from os.path import dirname,basename, join, abspath, expanduser,exists, isfile, isdir
from glob import glob
import zipfile
from importlib import import_module
import socket
import webbrowser
import sys
import json
import shutil
import requests
import tempfile
from requests.exceptions import HTTPError, Timeout, RequestException
import bpy  # type: ignore
import gpu # type: ignore
from gpu_extras.batch import batch_for_shader # type: ignore
import blf # type: ignore




###########################################

BLF_INFO = {
    "fontid" : 0,
    "size" : 18,
}
REPO_URL = "https://github.com/issamdakir/Bdental4/zipball/main"
VERSION_URL = "https://raw.githubusercontent.com/issamdakir/Bdental4/main/Resources/BDENTAL_Version.txt"
ADDON_UPDATE_URL = "https://github.com/issamdakir/Bdental4_update/zipball/main"
UPDATE_VERSION_URL = "https://raw.githubusercontent.com/issamdakir/Bdental4_update/main/data/BDENTAL_Version.txt"
GITHUB_CMD = "curl -L https://github.com/issamdakir/Bdental4/zipball/main"
TELEGRAM_LINK = "https://t.me/bdental3"
REQ_DICT = {
    "SimpleITK": "SimpleITK",
    "vtk": "vtk",
    "cv2.aruco": "opencv-contrib-python",
}
ERROR_PANEL = False
ERROR_MESSAGE = []
ADDON_DIR = dirname(abspath(__file__))
RESOURCES = join(ADDON_DIR, "Resources")
BDENTAL_LIB_NAME='Bdental_Library'
BDENTAL_LIB_ARCHIVE_NAME='Bdental_Library_Archive'

BDENTAL_LIBRARY_PATH = join(ADDON_DIR, BDENTAL_LIB_NAME)
BDENTAL_LIBRARY_ARCHIVE_PATH = join(RESOURCES, BDENTAL_LIB_ARCHIVE_NAME)

ADDON_VER_PATH = join(RESOURCES, "BDENTAL_Version.txt")
ADDON_VER_DATE = "  "
BDENTAL_MODULES = join(ADDON_DIR, "bdental_modules")

DRAW_HANDLERS=[]
BOOL_NODE ="boolean_geonode"
GUIDE_NAME = "Bdental_guide"

def bdental_log(txt_list,header=None,footer=None):
    _header, _footer = header, footer
    if _header is None :
        _header=f"\n{'#'*20} Bdental log :  {'#'*20}\n"
    if _footer is None:
        _footer=f"\n{'#'*20} End log.\  {'#'*20}\n"
    
    print(_header)
    for line in txt_list :
        print(line)
    print(_footer)

def get_bdental_version(filepath=ADDON_VER_PATH):

    try :
        with open(filepath, "r") as rf:
            lines = rf.readlines()
            version = int(lines[0])
            return version
    except Exception as er :
        txt_message = [f""]
        bdental_log(txt_message)
        return 0
def get_update_version(filepath=UPDATE_VERSION_URL)  :
    success = False
    txt_list= []
    update_version = None
    try :
        r = requests.get(filepath)
        success = r.ok
    except Exception as er :
        txt_list.append(f"request github bdental version error : {er}")
        bdental_log(txt_list)
        
    if not success :
        txt_list.append(r.text)
    else :
        update_version = int(r.text)
    return update_version,success,txt_list
    
class BdentalColors():
    white = [0.8,0.8,0.8,1.0]
    black = [0.0,0.0,0.0,1.0]
    trans = [0.8,0.8,0.8,0.0]
    red = [1.0,0.0,0.0,1.0]
    orange = [0.8, 0.258385, 0.041926, 1.0]
    yellow = [0.4,0.4,0.1,1]
    green = [0,1,0.2,0.7]
    blue = [0.2,0.1,1,0.2]
    default = orange

def add_bdental_libray() :
    message = []
    success = 0
    if not exists(BDENTAL_LIBRARY_ARCHIVE_PATH):
        message = ["Bdental Library archive not found"]
        return message,success
    _libs_collection_group = bpy.context.preferences.filepaths.asset_libraries
    bdental_lib = _libs_collection_group.get(BDENTAL_LIB_NAME)
    if bdental_lib :
        idx = [i for i,l in enumerate(_libs_collection_group) if l.name==BDENTAL_LIB_NAME][0]
        bpy.ops.preferences.asset_library_remove(index=idx)
    
    if exists(BDENTAL_LIBRARY_PATH):
        shutil.rmtree(BDENTAL_LIBRARY_PATH)
    os.mkdir(BDENTAL_LIBRARY_PATH)

    archive_list = os.listdir(BDENTAL_LIBRARY_ARCHIVE_PATH)
    for _item in archive_list :
        _item_full_path = join(BDENTAL_LIBRARY_ARCHIVE_PATH,_item)
        if _item.endswith('.zip') :
            with zipfile.ZipFile(_item_full_path, 'r') as zip_ref:
                zip_ref.extractall(BDENTAL_LIBRARY_PATH)
        else :
            shutil.copy2(_item_full_path, BDENTAL_LIBRARY_PATH)

    bpy.ops.preferences.asset_library_add(directory=BDENTAL_LIBRARY_PATH)
    success = 1
    return message, success

def ImportReq(REQ_DICT):
    Pkgs = []
    for mod, pkg in REQ_DICT.items():
        try:
            import_module(mod)
        except ImportError:
            Pkgs.append(pkg)

    return Pkgs

def isConnected(test_url="www.google.com",debug=False):
    result = False
    try:
        sock = socket.create_connection((test_url, 80))
        if sock is not None:
            sock.close
            result = True
        
    except OSError:
        pass

    if debug :
        info = "no connexion!"
        if result :
            info = "connected..."
        bdental_log([info])
    return result

def browse(url) :
    success = 0
    try :
        webbrowser.open(url)
        success = 1
        return success
    except Exception as er :
        print(f"open telegram link error :\n{er}")
        return success

def start_blender_session():
    # print(f"binary path : {bpy.app.binary_path}")
    os.system(f'"{bpy.app.binary_path}"')



def set_modules_path(modules_path=BDENTAL_MODULES):
    if not modules_path in sys.path :
        sys.path.insert(0,BDENTAL_MODULES)
def write_json(Dict,outPath) :
    jsonString = json.dumps(Dict,indent=4)
    with open(outPath, 'w') as wf :
        wf.write(jsonString)

def open_json(jsonPath) :
    with open(jsonPath, "r") as f:
        dataDict = json.load(f)
    return dataDict

    
def addon_update_preinstall(update_root):
    
    update_data_map_json = join(update_root, "update_data_map.json")
    update_data_map_dict = open_json(update_data_map_json)
    update_data_dir = join(update_root, "data")
    items = os.listdir(update_data_dir)
    
    update_data_dict = {join(update_data_dir,i) : join(ADDON_DIR,*update_data_map_dict.get(i)) for i in items}
    for src,dst in update_data_dict.items():
        
        if "bdental_modules" in src.lower() :
            resources = join(ADDON_DIR, "Resources")
            shutil.move(src, resources)
        else :
            if not exists(dirname(dst)) :
                os.makedirs(dirname(dst))

            if exists(dst) :
                os.remove(dst) if isfile(dst) else shutil.rmtree(dst)
            
            shutil.move(src, dirname(dst))
        

def addon_update_download():
    
    message = []
    update_root = None 
    try :
        temp_dir = tempfile.mkdtemp()
        os.chdir(temp_dir)
        _update_zip_local = join(temp_dir,'Bdental_4_update.zip')

        # Download the file
        with requests.get(ADDON_UPDATE_URL, stream=True, timeout=10) as r:
            try:
                r.raise_for_status()
            except HTTPError as http_err:
                txt = "HTTP error occurred"
                bdental_log([f"{txt} : {http_err}"])
                message.extend([txt])
                return message,update_root
            except ConnectionError as conn_err:
                txt = "Connection error occurred"
                bdental_log([f"{txt} : {conn_err}"])
                message.extend([txt])
                return message,update_root
            except Timeout as timeout_err:
                txt = "Timeout error occurred"
                bdental_log([f"{txt} : {timeout_err}"])
                message.extend([txt])
                return message,update_root
            except RequestException as req_err:
                txt = f"Error during requests to {REPO_URL}"
                bdental_log([f"{txt} : {req_err}"])
                message.extend([txt])
                return message,update_root
            
            with open(_update_zip_local, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        
        
        try :
            with zipfile.ZipFile(_update_zip_local, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
        except zipfile.BadZipFile as zip_err:
            txt = "Error occurred while extracting the downloaded addon ZIP file"
            bdental_log([f"{txt} : {zip_err}"])
            message.extend([txt])
            return message,update_root
        
        src = [abspath(e) for e in os.listdir(temp_dir) if isdir(abspath(e))][0]
        update_root = join(temp_dir,"Bdental-4-update")
        os.rename(src,update_root)
        return message,update_root

    except OSError as os_err:
        bdental_log([f"OS error occurred: {os_err}"])
        message.extend([txt])
        return message,update_root
    except Exception as err:
        bdental_log([f"An unexpected error occurred: {err}"]) 
        message.extend([txt])
        return message,update_root

def write_json(Dict,outPath) :
    jsonString = json.dumps(Dict,indent=4)
    with open(outPath, 'w') as wf :
        wf.write(jsonString)

def open_json(jsonPath) :
    with open(jsonPath, "r") as f:
        dataDict = json.load(f)
    return dataDict


class BDENTAL_GpuDrawText() :
    """gpu draw text in active area 3d"""
    
    

    def __init__(self,
                message_list = [],
                remove_handlers=True,
                button=False,
                percentage=100,
                redraw_timer=True,
                rect_color=BdentalColors.default,
                txt_color = BdentalColors.black,
                btn_txt = "OK",
                info_handler = None
                ):
        
        global DRAW_HANDLERS
        self.message_list=message_list
        self.remove_handlers=remove_handlers
        self.button=button
        self.percentage=percentage
        self.redraw_timer=redraw_timer
        self.rect_color=rect_color
        
        self.txt_color=txt_color
        self.btn_txt=btn_txt
        self.info_handler=info_handler
        self.rect_height=30
        self.offset_vertical=35
        self.offset_horizontal=50

        if self.remove_handlers:
            for _h in DRAW_HANDLERS:
                bpy.types.SpaceView3D.draw_handler_remove(_h, "WINDOW")
            DRAW_HANDLERS = []
        if self.message_list:
            self.gpu_info_footer()
            DRAW_HANDLERS.append(self.info_handler)
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)   
        

    def gpu_info_footer(self):
        
        if self.percentage <= 0:
            self.percentage = 1
        if self.percentage > 100:
            self.percentage = 100

        def draw_callback_function():

            w = int(bpy.context.area.width * (self.percentage/100))
            for i, txt in enumerate((reversed(self.message_list))):

                self.draw_gpu_rect(self.offset_horizontal, (self.rect_height*i)+self.offset_vertical, w-self.offset_horizontal, self.rect_height, self.rect_color)
                blf.position(BLF_INFO.get('fontid'), self.offset_horizontal+10, 10 + (self.rect_height*i)+self.offset_vertical, 0)
                blf.size(BLF_INFO.get("fontid"), BLF_INFO.get("size")) # 3.6 api blf.size(0, 40, 30) -> blf.size(fontid, size)
                r, g, b, a = self.txt_color
                blf.color(0, r, g, b, a)
                blf.draw(0, txt)

            if self.button:
                self.draw_gpu_rect(w-110, 2, 100, self.rect_height-4, BdentalColors.yellow)
                blf.position(0, w-85, 10, 0)
                blf.size(BLF_INFO.get("fontid"), BLF_INFO.get("size")) # 3.6 api blf.size(0, 40, 30) -> blf.size(fontid, size)
                r, g, b, a = self.txt_color
                blf.color(0, r, g, b, a)
                blf.draw(0, self.btn_txt)

        self.info_handler = bpy.types.SpaceView3D.draw_handler_add(
            draw_callback_function, (), "WINDOW", "POST_PIXEL"
        )
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

    def draw_gpu_rect(self,x, y, w, h, rect_color):

        vertices = (
            (x, y), (x, y + h),
            (x + w, y + h), (x + w, y))

        indices = (
            (0, 1, 2), (0, 2, 3)
        )

        gpu.state.blend_set('ALPHA')
        shader = gpu.shader.from_builtin('UNIFORM_COLOR') # 3.6 api '2D_UNIFORM_COLOR'
        batch = batch_for_shader(
            shader, 'TRIS', {"pos": vertices}, indices=indices)
        shader.bind()
        shader.uniform_float("color", rect_color)
        batch.draw(shader)

