# ##### BEGIN MIT LICENSE BLOCK #####
#
# MIT License
#
# Copyright (c) 2022 Steven Garcia
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

import os

from ..file_jms import export_jms
from .process_scene import process_scene

def build_asset(context, JMS_args, version, game_version, root_directory, filename, report):
    JMI = process_scene(context)
    if version >= 8207:
        file = open(root_directory + os.sep + filename, 'w', encoding='utf_8')

        #write header
        version_bounds = '8207-8210'
        if game_version == 'halo3mcc':
            version_bounds = '8207-8213'

        file.write(
            ';### VERSION ###' +
            '\n%s' % (version) +
            '\n;\t<%s>\n' % (version_bounds) +
            '\n'
            )

        file.write(
            ';### TOTAL OBJECTS ###' +
            '\n%s' % (len(JMI.children_sets)) +
            '\n;\t<name>' +
            '\n'
            )

        for world_nodes in JMI.children_sets:
            file.write('\n%s' % (world_nodes[0].name.split('!', 1)[1]))

        file.write('\n')
        file.close()

    for idx, world_nodes in enumerate(JMI.children_sets):
        permutation_name = JMI.world_nodes[idx].jmi.permutation_ce
        lod_setting = JMI.world_nodes[idx].jmi.level_of_detail_ce
        world_name = world_nodes[0].name.split('!', 1)[1]
        world_set = root_directory + os.sep + world_name
        if not os.path.exists(world_set):
            os.makedirs(world_set)

        bulk_output = world_set + os.sep + world_name
        export_jms.command_queue(context, bulk_output, report, JMS_args.jmi_version, JMS_args.jmi_version_ce, JMS_args.jmi_version_h2, JMS_args.jmi_version_h3, True, True, JMS_args.folder_type, JMS_args.apply_modifiers, JMS_args.triangulate_faces, JMS_args.fix_rotations, JMS_args.edge_split, JMS_args.use_edge_angle, JMS_args.use_edge_sharp, JMS_args.split_angle, JMS_args.clean_normalize_weights, JMS_args.scale_enum, JMS_args.scale_float, JMS_args.console, permutation_name, lod_setting, JMS_args.hidden_geo, JMS_args.export_render, JMS_args.export_collision, JMS_args.export_physics, game_version, world_nodes)

    report({'INFO'}, "Export completed successfully")
