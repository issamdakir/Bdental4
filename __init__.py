# ----------------------------------------------------------
# File __init__.py
# ----------------------------------------------------------

#    Addon info
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
#  as published by the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

# Please check the LICENSE file for the full license
#
#  You should have received a copy of the GNU General Public License Version 3, 29 June 2007
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
##############################################################################################
#In addition to the GPL license, the following terms apply to all files in the "bdental_3_modules" folder:
#This program use the following modules:
#vtk :
# /*=========================================================================

#   Program:   Visualization Toolkit
#   Module:    Copyright.txt

# Copyright (c) 1993-2015 Ken Martin, Will Schroeder, Bill Lorensen
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

#  * Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.

#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

#  * Neither name of Ken Martin, Will Schroeder, or Bill Lorensen nor the names
#    of any contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# =========================================================================*/
#
# SimpleITK & OpenCV :
# Apache License
#                            Version 2.0, January 2004
#                         http://www.apache.org/licenses/

#    TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

#    1. Definitions.

#       "License" shall mean the terms and conditions for use, reproduction,
#       and distribution as defined by Sections 1 through 9 of this document.

#       "Licensor" shall mean the copyright owner or entity authorized by
#       the copyright owner that is granting the License.

#       "Legal Entity" shall mean the union of the acting entity and all
#       other entities that control, are controlled by, or are under common
#       control with that entity. For the purposes of this definition,
#       "control" means (i) the power, direct or indirect, to cause the
#       direction or management of such entity, whether by contract or
#       otherwise, or (ii) ownership of fifty percent (50%) or more of the
#       outstanding shares, or (iii) beneficial ownership of such entity.

#       "You" (or "Your") shall mean an individual or Legal Entity
#       exercising permissions granted by this License.

#       "Source" form shall mean the preferred form for making modifications,
#       including but not limited to software source code, documentation
#       source, and configuration files.

#       "Object" form shall mean any form resulting from mechanical
#       transformation or translation of a Source form, including but
#       not limited to compiled object code, generated documentation,
#       and conversions to other media types.

#       "Work" shall mean the work of authorship, whether in Source or
#       Object form, made available under the License, as indicated by a
#       copyright notice that is included in or attached to the work
#       (an example is provided in the Appendix below).

#       "Derivative Works" shall mean any work, whether in Source or Object
#       form, that is based on (or derived from) the Work and for which the
#       editorial revisions, annotations, elaborations, or other modifications
#       represent, as a whole, an original work of authorship. For the purposes
#       of this License, Derivative Works shall not include works that remain
#       separable from, or merely link (or bind by name) to the interfaces of,
#       the Work and Derivative Works thereof.

#       "Contribution" shall mean any work of authorship, including
#       the original version of the Work and any modifications or additions
#       to that Work or Derivative Works thereof, that is intentionally
#       submitted to Licensor for inclusion in the Work by the copyright owner
#       or by an individual or Legal Entity authorized to submit on behalf of
#       the copyright owner. For the purposes of this definition, "submitted"
#       means any form of electronic, verbal, or written communication sent
#       to the Licensor or its representatives, including but not limited to
#       communication on electronic mailing lists, source code control systems,
#       and issue tracking systems that are managed by, or on behalf of, the
#       Licensor for the purpose of discussing and improving the Work, but
#       excluding communication that is conspicuously marked or otherwise
#       designated in writing by the copyright owner as "Not a Contribution."

#       "Contributor" shall mean Licensor and any individual or Legal Entity
#       on behalf of whom a Contribution has been received by Licensor and
#       subsequently incorporated within the Work.

#    2. Grant of Copyright License. Subject to the terms and conditions of
#       this License, each Contributor hereby grants to You a perpetual,
#       worldwide, non-exclusive, no-charge, royalty-free, irrevocable
#       copyright license to reproduce, prepare Derivative Works of,
#       publicly display, publicly perform, sublicense, and distribute the
#       Work and such Derivative Works in Source or Object form.

#    3. Grant of Patent License. Subject to the terms and conditions of
#       this License, each Contributor hereby grants to You a perpetual,
#       worldwide, non-exclusive, no-charge, royalty-free, irrevocable
#       (except as stated in this section) patent license to make, have made,
#       use, offer to sell, sell, import, and otherwise transfer the Work,
#       where such license applies only to those patent claims licensable
#       by such Contributor that are necessarily infringed by their
#       Contribution(s) alone or by combination of their Contribution(s)
#       with the Work to which such Contribution(s) was submitted. If You
#       institute patent litigation against any entity (including a
#       cross-claim or counterclaim in a lawsuit) alleging that the Work
#       or a Contribution incorporated within the Work constitutes direct
#       or contributory patent infringement, then any patent licenses
#       granted to You under this License for that Work shall terminate
#       as of the date such litigation is filed.

#    4. Redistribution. You may reproduce and distribute copies of the
#       Work or Derivative Works thereof in any medium, with or without
#       modifications, and in Source or Object form, provided that You
#       meet the following conditions:

#       (a) You must give any other recipients of the Work or
#           Derivative Works a copy of this License; and

#       (b) You must cause any modified files to carry prominent notices
#           stating that You changed the files; and

#       (c) You must retain, in the Source form of any Derivative Works
#           that You distribute, all copyright, patent, trademark, and
#           attribution notices from the Source form of the Work,
#           excluding those notices that do not pertain to any part of
#           the Derivative Works; and

#       (d) If the Work includes a "NOTICE" text file as part of its
#           distribution, then any Derivative Works that You distribute must
#           include a readable copy of the attribution notices contained
#           within such NOTICE file, excluding those notices that do not
#           pertain to any part of the Derivative Works, in at least one
#           of the following places: within a NOTICE text file distributed
#           as part of the Derivative Works; within the Source form or
#           documentation, if provided along with the Derivative Works; or,
#           within a display generated by the Derivative Works, if and
#           wherever such third-party notices normally appear. The contents
#           of the NOTICE file are for informational purposes only and
#           do not modify the License. You may add Your own attribution
#           notices within Derivative Works that You distribute, alongside
#           or as an addendum to the NOTICE text from the Work, provided
#           that such additional attribution notices cannot be construed
#           as modifying the License.

#       You may add Your own copyright statement to Your modifications and
#       may provide additional or different license terms and conditions
#       for use, reproduction, or distribution of Your modifications, or
#       for any such Derivative Works as a whole, provided Your use,
#       reproduction, and distribution of the Work otherwise complies with
#       the conditions stated in this License.

#    5. Submission of Contributions. Unless You explicitly state otherwise,
#       any Contribution intentionally submitted for inclusion in the Work
#       by You to the Licensor shall be under the terms and conditions of
#       this License, without any additional terms or conditions.
#       Notwithstanding the above, nothing herein shall supersede or modify
#       the terms of any separate license agreement you may have executed
#       with Licensor regarding such Contributions.

#    6. Trademarks. This License does not grant permission to use the trade
#       names, trademarks, service marks, or product names of the Licensor,
#       except as required for reasonable and customary use in describing the
#       origin of the Work and reproducing the content of the NOTICE file.

#    7. Disclaimer of Warranty. Unless required by applicable law or
#       agreed to in writing, Licensor provides the Work (and each
#       Contributor provides its Contributions) on an "AS IS" BASIS,
#       WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#       implied, including, without limitation, any warranties or conditions
#       of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
#       PARTICULAR PURPOSE. You are solely responsible for determining the
#       appropriateness of using or redistributing the Work and assume any
#       risks associated with Your exercise of permissions under this License.

#    8. Limitation of Liability. In no event and under no legal theory,
#       whether in tort (including negligence), contract, or otherwise,
#       unless required by applicable law (such as deliberate and grossly
#       negligent acts) or agreed to in writing, shall any Contributor be
#       liable to You for damages, including any direct, indirect, special,
#       incidental, or consequential damages of any character arising as a
#       result of this License or out of the use or inability to use the
#       Work (including but not limited to damages for loss of goodwill,
#       work stoppage, computer failure or malfunction, or any and all
#       other commercial damages or losses), even if such Contributor
#       has been advised of the possibility of such damages.

#    9. Accepting Warranty or Additional Liability. While redistributing
#       the Work or Derivative Works thereof, You may choose to offer,
#       and charge a fee for, acceptance of support, warranty, indemnity,
#       or other liability obligations and/or rights consistent with this
#       License. However, in accepting such obligations, You may act only
#       on Your own behalf and on Your sole responsibility, not on behalf
#       of any other Contributor, and only if You agree to indemnify,
#       defend, and hold each Contributor harmless for any liability
#       incurred by, or claims asserted against, such Contributor by reason
#       of your accepting any such warranty or additional liability.

#    END OF TERMS AND CONDITIONS

#    APPENDIX: How to apply the Apache License to your work.

#       To apply the Apache License to your work, attach the following
#       boilerplate notice, with the fields enclosed by brackets "[]"
#       replaced with your own identifying information. (Don't include
#       the brackets!)  The text should be enclosed in the appropriate
#       comment syntax for the file format. We also recommend that a
#       file or class name and description of purpose be included on the
#       same "printed page" as the copyright notice for easier
#       identification within third-party archives.

#    Copyright [yyyy] [name of copyright owner]

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
bl_info = {
    "name": "Bdental4",  
    "author": "Dr. Essaid Issam Dakir DMD\n,Dr. Ilya Fomenco DMD\n, Dr. Krasouski Dmitry DMD",
    "version": (4, 2, 0),
    "blender": (4, 2, 0),  
    "location": "3D View -> UI SIDE PANEL ",
    "description": "3D Digital Dentistry",  
    "warning": "",
    "doc_url": "",
    # "tracker_url": "https://t.me/bdental3",
    "category": "Dental",  
}
#############################################################################################
# IMPORTS :
#############################################################################################
# Python imports :

import sys
import shutil
import os
import bpy # type: ignore
import zipfile

from importlib import import_module
from os.path import dirname,basename, join, abspath, expanduser,exists, isfile, isdir
from time import sleep
import threading

import tempfile
from glob import glob
import requests
from requests.exceptions import HTTPError, Timeout, RequestException
import gpu # type: ignore
from gpu_extras.batch import batch_for_shader # type: ignore
import blf # type: ignore

from .utils import (
    bdental_log,
    BDENTAL_MODULES,
    add_bdental_libray,
    set_modules_path,
    isConnected,
    BdentalColors,
    BDENTAL_GpuDrawText,
    browse,
    get_bdental_version,
    ERROR_MESSAGE,
    ERROR_PANEL,
    ImportReq,
    addon_update_preinstall,
    get_update_version,
    BLF_INFO,
    ADDON_DIR,
    RESOURCES,
    REQ_DICT,
    TELEGRAM_LINK,
    ADDON_VER_PATH,
    UPDATE_VERSION_URL,
    REPO_URL,
    addon_update_download,
    write_json,
    open_json,
)

# DRAW_HANDLERS=[]
addon_version = get_bdental_version(filepath=ADDON_VER_PATH)
set_modules_path()

# def gpu_info_footer(rect_color, text_list, button=False, btn_txt="", pourcentage=100):
#     global BLF_INFO
#     if pourcentage <= 0:
#         pourcentage = 1
#     if pourcentage > 100:
#         pourcentage = 100

#     def draw_callback_function():

#         w = int(bpy.context.area.width * (pourcentage/100))
#         for i, txt in enumerate((reversed(text_list))):

#             h = 30
#             # color = [0.4, 0.4, 0.8, 1.000000]
#             # color =[0.9, 0.5, 0.000000, 1.000000]
#             draw_gpu_rect(0, h*i, w, h, rect_color)
#             blf.position(0, 10, 10 + (h*i), 0)
#             blf.size(BLF_INFO.get("fontid"), BLF_INFO.get("size")) # 3.6 api blf.size(0, 40, 30) -> blf.size(fontid, size)
#             r, g, b, a = (0.0, 0.0, 0.0, 1.0)
#             blf.color(0, r, g, b, a)
#             blf.draw(0, txt)

#         if button:

#             h = 30
#             color = [0.8, 0.258385, 0.041926, 1.0]
#             draw_gpu_rect(w-110, 2, 100, h-4, color)
#             blf.position(0, w-85, 10, 0)
#             blf.size(BLF_INFO.get("fontid"), BLF_INFO.get("size")) # 3.6 api blf.size(0, 40, 30) -> blf.size(fontid, size)
#             r, g, b, a = (0.0, 0.0, 0.0, 1.0)
#             blf.color(0, r, g, b, a)
#             blf.draw(0, btn_txt)

#     info_handler = bpy.types.SpaceView3D.draw_handler_add(
#         draw_callback_function, (), "WINDOW", "POST_PIXEL"
#     )
#     # redraw scene
#     # bpy.ops.wm.redraw_timer(type = 'DRAW_WIN_SWAP', iterations = 1)
#     # for area in bpy.context.window.screen.areas:
#     #     if area.type == "VIEW_3D":
#     #         area.tag_redraw()

#     return info_handler

# def get_btn_bb(btn_index=0, btn_width=100, btn_height=26, padding_x=10, padding_y=2, safe_area=5):
#     area3d = None
#     area3d_check = [
#         area for area in bpy.context.screen.areas if area.type == "VIEW_3D"]
#     if area3d_check:
#         area3d = area3d_check[0]
#     if area3d:
#         w = area3d.width
#         x_min = w - padding_x - (btn_width*(btn_index+1)) - \
#             (padding_x*btn_index) - safe_area
#         x_max = w - padding_x - (btn_width*(btn_index)) - \
#             (padding_x*btn_index) + safe_area
#         y_min = 0
#         y_max = btn_height+safe_area
#         btn_bb = {
#             "x_min": x_min,
#             "x_max": x_max,
#             "y_min": y_min,
#             "y_max": y_max
#         }
#         return btn_bb
#     else:
#         return None

# def draw_gpu_rect(x, y, w, h, rect_color):

#     vertices = (
#         (x, y), (x, y + h),
#         (x + w, y + h), (x + w, y))

#     indices = (
#         (0, 1, 2), (0, 2, 3)
#     )

#     gpu.state.blend_set('ALPHA')
#     shader = gpu.shader.from_builtin('UNIFORM_COLOR') # 3.6 api '2D_UNIFORM_COLOR'
#     batch = batch_for_shader(
#         shader, 'TRIS', {"pos": vertices}, indices=indices)
#     shader.bind()
#     shader.uniform_float("color", rect_color)
#     batch.draw(shader)

# def update_info(message=[], remove_handlers=True, button=False, btn_txt="", pourcentage=100, redraw_timer=True, rect_color=BdentalColors.default):
#     global DRAW_HANDLERS

#     if remove_handlers:
#         for _h in DRAW_HANDLERS:
#             bpy.types.SpaceView3D.draw_handler_remove(_h, "WINDOW")
#         DRAW_HANDLERS = []
#     if message:
#         info_handler = gpu_info_footer(
#             text_list=message, button=False, btn_txt="", pourcentage=100, rect_color=rect_color)
#         DRAW_HANDLERS.append(info_handler)
#     if redraw_timer:
#         bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
# class BDENTAL_GpuDrawText() :
#     """gpu draw text in active area 3d"""
    
    

#     def __init__(self,
#                 message_list = [],
#                 remove_handlers=True,
#                 button=False,
#                 pourcentage=100,
#                 redraw_timer=True,
#                 rect_color=BdentalColors.default,
#                 rect_height = 30,
#                 txt_color = BdentalColors.black,
#                 btn_txt = "OK",
#                 info_handler = None
#                 ):
        
#         global DRAW_HANDLERS
#         self.message_list=message_list
#         self.remove_handlers=remove_handlers
#         self.button=button
#         self.pourcentage=pourcentage
#         self.redraw_timer=redraw_timer
#         self.rect_color=rect_color
#         self.rect_height=rect_height
#         self.txt_color=txt_color
#         self.btn_txt=btn_txt
#         self.info_handler=info_handler

#         if self.remove_handlers:
#             for _h in DRAW_HANDLERS:
#                 bpy.types.SpaceView3D.draw_handler_remove(_h, "WINDOW")
#             DRAW_HANDLERS = []
#         if self.message_list:
#             self.gpu_info_footer()
#             DRAW_HANDLERS.append(self.info_handler)
#         bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)   
        

#     def gpu_info_footer(self):
        
#         if self.pourcentage <= 0:
#             self.pourcentage = 1
#         if self.pourcentage > 100:
#             self.pourcentage = 100

#         def draw_callback_function():

#             w = int(bpy.context.area.width * (self.pourcentage/100))
#             for i, txt in enumerate((reversed(self.message_list))):

#                 self.draw_gpu_rect(0, self.rect_height*i, w, self.rect_height, self.rect_color)
#                 blf.position(0, 10, 10 + (self.rect_height*i), 0)
#                 blf.size(BLF_INFO.get("fontid"), BLF_INFO.get("size")) # 3.6 api blf.size(0, 40, 30) -> blf.size(fontid, size)
#                 r, g, b, a = self.txt_color
#                 blf.color(0, r, g, b, a)
#                 blf.draw(0, txt)

#             if self.button:
#                 self.draw_gpu_rect(w-110, 2, 100, self.rect_height-4, BdentalColors.yellow)
#                 blf.position(0, w-85, 10, 0)
#                 blf.size(BLF_INFO.get("fontid"), BLF_INFO.get("size")) # 3.6 api blf.size(0, 40, 30) -> blf.size(fontid, size)
#                 r, g, b, a = self.txt_color
#                 blf.color(0, r, g, b, a)
#                 blf.draw(0, self.btn_txt)

#         self.info_handler = bpy.types.SpaceView3D.draw_handler_add(
#             draw_callback_function, (), "WINDOW", "POST_PIXEL"
#         )
#         bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

#     def draw_gpu_rect(self,x, y, w, h, rect_color):

#         vertices = (
#             (x, y), (x, y + h),
#             (x + w, y + h), (x + w, y))

#         indices = (
#             (0, 1, 2), (0, 2, 3)
#         )

#         gpu.state.blend_set('ALPHA')
#         shader = gpu.shader.from_builtin('UNIFORM_COLOR') # 3.6 api '2D_UNIFORM_COLOR'
#         batch = batch_for_shader(
#             shader, 'TRIS', {"pos": vertices}, indices=indices)
#         shader.bind()
#         shader.uniform_float("color", rect_color)
#         batch.draw(shader)



def addon_download():
    global REPO_URL
    message = []
    _dir = None 
    try :
        temp_dir = tempfile.mkdtemp()
        os.chdir(temp_dir)
        bdental_zip_local = join(temp_dir,'Bdental-3.zip')

        # Download the file
        with requests.get(REPO_URL, stream=True, timeout=10) as r:
            try:
                r.raise_for_status()
            except HTTPError as http_err:
                txt = "HTTP error occurred"
                print(f"{txt} : {http_err}")
                message.extend([txt])
                return message,_dir
            except ConnectionError as conn_err:
                txt = "Connection error occurred"
                print(f"{txt} : {conn_err}")
                message.extend([txt])
                return message,_dir
            except Timeout as timeout_err:
                txt = "Timeout error occurred"
                print(f"{txt} : {timeout_err}")
                message.extend([txt])
                return message,_dir
            except RequestException as req_err:
                txt = f"Error during requests to {REPO_URL}"
                print(f"{txt} : {req_err}")
                message.extend([txt])
                return message,_dir
            
            with open(bdental_zip_local, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        
        
        try :
            with zipfile.ZipFile(bdental_zip_local, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
        except zipfile.BadZipFile as zip_err:
            txt = "Error occurred while extracting the downloaded addon ZIP file"
            print(f"{txt} : {zip_err}")
            message.extend([txt])
            return message,_dir
        
        src = [abspath(e) for e in os.listdir(temp_dir) if isdir(abspath(e))][0]
        _dir = join(temp_dir,"Bdental-3")
        os.rename(src,_dir)

    except OSError as os_err:
        print(f"OS error occurred: {os_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}") 
    return message,_dir



class BDENTAL_OT_SupportTelegram(bpy.types.Operator):
        """ open telegram bdental support link"""

        bl_idname = "wm.bdental_support_telegram"
        bl_label = "Bdental Support (Telegram)"

        #### this freezes blender ui !! ###
        # @classmethod
        # def poll(cls, context):
        #     return isConnected()
        ###################################


        def execute(self, context):
            browse(TELEGRAM_LINK)
            
            return{"FINISHED"}
class BDENTAL_OT_AddBdentalLibrary(bpy.types.Operator):
    """ add bdental library """

    bl_idname = "wm.bdental_add_bdental_library"
    bl_label = "Add Bdental Library"
    def execute(self, context):
        with context.temp_override(window=context.window_manager.windows[0]):
            message = ["Adding Bdental library..."]
            BDENTAL_GpuDrawText(message)
            sleep(1)
            message, success = add_bdental_libray()
            if not success and message :
                BDENTAL_GpuDrawText(message_list=message,rect_color=BdentalColors.red)
                sleep(3)
                BDENTAL_GpuDrawText()
                return {"CANCELLED"}


            message = ["FINISHED"]
            BDENTAL_GpuDrawText(message_list=message,rect_color=BdentalColors.green)
            sleep(2)
            BDENTAL_GpuDrawText()
            return {"FINISHED"}
    
class BdentalAddonPreferences(bpy.types.AddonPreferences):
        bl_idname = __name__

        def draw(self, context):
            layout = self.layout
            box = layout.box()
            row = box.row()
            row.operator("wm.bdental_add_app_template", text="Bdental as template",icon="SETTINGS")
            row = box.row()
            row.operator("wm.bdental_set_config", text="Bdental as default", icon="TOOL_SETTINGS")
            row = box.row()
            row.operator("wm.bdental_add_bdental_library", text="Add Bdental Library", icon="TOOL_SETTINGS")

class BDENTAL_OT_checkUpdate(bpy.types.Operator):
    """ check addon update """

    bl_idname = "wm.bdental_checkupdate"
    bl_label = "check update"
    bl_options = {"REGISTER", "UNDO"}

    txt = []
    restart = 0
    
    def modal(self, context, event):
        if not event.type in {'ESC', 'RET'}:
            return {'PASS_THROUGH'}

        elif event.type in {'ESC'}:
            BDENTAL_GpuDrawText(message_list=["Bdental update Cancelled./"], rect_color=BdentalColors.red)
            # update_info(["Bdental update Cancelled./"], rect_color=BdentalColors.red)
            sleep(1)
            BDENTAL_GpuDrawText()
            return {'CANCELLED'}
        
        elif event.type in {'RET'} and event.value == "PRESS":
            BDENTAL_GpuDrawText(message_list=["Downloading..."])
            _message, update_root = addon_update_download()
            if _message :
                bdental_log(_message)
                BDENTAL_GpuDrawText(message=_message, rect_color=BdentalColors.red)
                sleep(3)
                BDENTAL_GpuDrawText()
                return{"CANCELLED"}
            
            BDENTAL_GpuDrawText(message_list=["Preparing update..."])
            addon_update_preinstall(update_root)
            add_bdental_libray()
            BDENTAL_GpuDrawText(message_list=["Please restart blender to finalize Bdental update."], rect_color=BdentalColors.green)
            # sleep(5)
            # update_info()
            
            return {'FINISHED'}
        return {'RUNNING_MODAL'}
        

    def invoke(self, context, event):
        if not isConnected() :
            BDENTAL_GpuDrawText(message_list=["Bdental update : Please check internet connexion !"], rect_color=BdentalColors.red)
            sleep(3)
            BDENTAL_GpuDrawText()
            return{"CANCELLED"}
        
        addon_version = get_bdental_version(filepath=ADDON_VER_PATH)
        update_version,success,txt_list = get_update_version()
        if not addon_version :
            addon_version = "unknown"
            
        if not success :
            BDENTAL_GpuDrawText(message_list=txt_list, rect_color=BdentalColors.red)
            sleep(3)
            BDENTAL_GpuDrawText()
            return{"CANCELLED"}
        
        
        txt_list = [f"Bdental addon update check : Current version = {addon_version} / update version = {update_version}"]
        
        
        if update_version <= addon_version :
            txt_list = ["Bdental is up to date."]
            bdental_log(txt_list)
            BDENTAL_GpuDrawText(message_list=txt_list, rect_color=BdentalColors.green)
            sleep(3)
            BDENTAL_GpuDrawText()
            return{"CANCELLED"}

        BDENTAL_GpuDrawText(message_list=txt_list+["<ENTER> : to install last update / <ESC> : to cancel"], rect_color=BdentalColors.yellow)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}


class BDENTAL_PT_ModulesErrorPanel(bpy.types.Panel):
        """ Modules error panel"""

        bl_idname = "BDENTAL_PT_ModulesErrorPanel"
        bl_space_type = "VIEW_3D"
        bl_region_type = "UI" 
        bl_category = "BDENTAL"
        bl_label = f"BDENTAL (ver. {addon_version})"

        def draw(self, context):

            layout = self.layout
            
            box = layout.box()
            grid = box.grid_flow(columns=1, align=True)
            grid.alert = True
            for l in ERROR_MESSAGE :
                grid.label(text=l)
            grid = box.grid_flow(columns=2, align=True)
            grid.operator("wm.bdental_checkupdate")
            grid.operator("wm.bdental_support_telegram")


###################################################
txt_list = [f"{bl_info.get('name')} started version : {addon_version if addon_version else 'unknown!'}"]
bdental_log(txt_list)

new_modules = join(RESOURCES, "bdental_modules")
if exists(new_modules) :
    sleep(3)
    if exists(BDENTAL_MODULES):
        shutil.rmtree(BDENTAL_MODULES)

    shutil.move(new_modules, ADDON_DIR)



if not exists(BDENTAL_MODULES) :
    ERROR_PANEL = True
    ERROR_MESSAGE.extend([
            "Bdental Modules are not installed properly",
            "Please update the addon or",
            "contact support",
        ])

if not ERROR_PANEL :
    
    NotFoundPkgs = ImportReq(REQ_DICT)
    if NotFoundPkgs :
        ERROR_PANEL = True
        ERROR_MESSAGE.extend([
            "Bdental Modules are not installed properly",
            "Please update the addon or",
            "contact support",
        ])

if ERROR_PANEL :
    addon_modules = []
    init_classes = [
            BDENTAL_OT_SupportTelegram,
            BDENTAL_OT_checkUpdate,
            BDENTAL_PT_ModulesErrorPanel,
            
        ]
    def register():
        
        for module in addon_modules:
            module.register()
        for cl in init_classes:
            bpy.utils.register_class(cl)

    def unregister():
        
        for cl in reversed(init_classes):
            bpy.utils.unregister_class(cl)
        for module in reversed(addon_modules):
            module.unregister()
else:
    
    from . import BDENTAL_Props, BDENTAL_Panel
    from .Operators import (
        BDENTAL_Operators, looptools
    )
    addon_modules = [
    BDENTAL_Props,
    BDENTAL_Panel,
    BDENTAL_Operators,
    looptools
    
    ]
    init_classes = [
        BDENTAL_OT_SupportTelegram,
        BDENTAL_OT_AddBdentalLibrary,
        BDENTAL_OT_checkUpdate,
        BdentalAddonPreferences,
        
        ]

    def register():
        
        for module in addon_modules:
            module.register()
        for cl in init_classes:
            bpy.utils.register_class(cl)

    def unregister():
        for cl in reversed(init_classes):
            bpy.utils.unregister_class(cl)
        for module in reversed(addon_modules):
            module.unregister()
        

if __name__ == "__main__":
    register()
