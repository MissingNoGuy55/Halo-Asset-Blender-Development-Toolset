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

from .format import JMIAsset
from ..global_functions import mesh_processing, global_functions

def process_scene(context):
    JMI = JMIAsset()

    collections = []
    layer_collections = list(context.view_layer.layer_collection.children)

    while len(layer_collections) > 0:
        collection_batch = layer_collections
        layer_collections = []
        for collection in collection_batch:
            collections.append(collection)
            for collection_child in collection.children:
                layer_collections.append(collection_child)

    scene = context.scene
    object_list = list(scene.objects)

    for obj in object_list:
        if obj.name[0:1].lower() == '!':
            mesh_processing.unhide_object(collections, obj)
            JMI.world_nodes.append(obj)

    for node in JMI.world_nodes:
        JMI.children_sets.append(global_functions.get_children(node))

    return JMI
