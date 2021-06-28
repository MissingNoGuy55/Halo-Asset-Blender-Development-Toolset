# ##### BEGIN MIT LICENSE BLOCK #####
#
# MIT License
#
# Copyright (c) 2020 Steven Garcia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# ##### END MIT LICENSE BLOCK #####

import re
import bpy

from io_scene_halo.global_functions import global_functions

def rename_prefix(prefix_string):
    node_prefix_tuple = ('b ', 'b_', 'bone ','bone_', 'frame', 'frame ','frame_', 'bip01', 'bip01 ', 'bip01_')

    selected_objects_list = bpy.context.selected_objects

    if not selected_objects_list == None:
        for object in selected_objects_list:
            if object.type == 'ARMATURE':
                for bone in object.data.bones:
                    bone_name = bone.name
                    if bone.name.lower().startswith(node_prefix_tuple):
                        for prefix in node_prefix_tuple:
                            if bone.name.lower().startswith(prefix):
                                prefix_letter_list = list(prefix)
                                prefix_limiter = ''
                                for letter in prefix_letter_list:
                                    prefix_limiter += ("[{}]".format(letter))
                                bone_name = re.split(prefix_limiter, bone.name, flags=re.IGNORECASE)[1]

                        bone.name = prefix_string + bone_name
            else:
                object_name = object.name
                if object.name.lower().startswith(node_prefix_tuple):
                    for prefix in node_prefix_tuple:
                        if object.name.lower().startswith(prefix):
                            prefix_letter_list = list(prefix)
                            prefix_limiter = ''
                            for letter in prefix_letter_list:
                                prefix_limiter += ("[{}]".format(letter))
                            object_name = re.split(prefix_limiter, object.name, flags=re.IGNORECASE)[1]

                    object.name = prefix_string + object_name

    return {'FINISHED'}

if __name__ == '__main__':
    bpy.ops.halo_bulk.bulk_node_prefix()