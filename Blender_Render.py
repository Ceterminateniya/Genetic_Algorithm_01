from turtle import left
import bpy
import csv
import sys
import os

select_object = bpy.context.active_object

def set_parameters():# 获取blender几何节点面板的参数
    
    # get evaluated cube object
    evaluated_object = bpy.data.objects["cube"].evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    # read the first value in the shouldGrow output attribute of the object
    should_grow = evaluated_object.attributes['shouldGrow'].data[0].value
    
    bpy.ops.object.modifier_set_active(modifier="GeometryNodes")
    flower_width=bpy.context.object.modifiers["GeometryNodes"].Input_2 # 花瓣宽度
    flower_height=bpy.context.object.modifiers["GeometryNodes"].Input_3 # 花瓣高度
    petals_number=bpy.context.object.modifiers["GeometryNodes"].Input_4 #花瓣片数
    leaf_number=bpy.context.object.modifiers["GeometryNodes"].Input_5 #叶子数
    petal_open_close_degree_y=bpy.context.object.modifiers["GeometryNodes"].Input_6[1] #开闭花瓣的程度
    leaf_open_close_degree_y=bpy.context.object.modifiers["GeometryNodes"].Input_7[1] #开闭叶子的程度
    petal_smoothness=bpy.context.object.modifiers["GeometryNodes"].Input_8 #花瓣平滑程度
    
    from_min_x=bpy.context.object.modifiers["GeometryNodes"].Input_9[0] #花瓣起始位置
    from_min_y=bpy.context.object.modifiers["GeometryNodes"].Input_9[1] 
    from_min_z=bpy.context.object.modifiers["GeometryNodes"].Input_9[2]
     
    from_max_x  = bpy.context.object.modifiers["GeometryNodes"].Input_10[0] #花瓣结束位置
    from_max_y  = bpy.context.object.modifiers["GeometryNodes"].Input_10[1]
    from_max_z  = bpy.context.object.modifiers["GeometryNodes"].Input_10[2]
    
    to_min_x=bpy.context.object.modifiers["GeometryNodes"].Input_11[0] #花瓣结束位置
    to_min_y=bpy.context.object.modifiers["GeometryNodes"].Input_11[1]
    to_min_z=bpy.context.object.modifiers["GeometryNodes"].Input_11[2]
    
    to_max_x=bpy.context.object.modifiers["GeometryNodes"].Input_12[0] #花瓣结束位置
    to_max_y=bpy.context.object.modifiers["GeometryNodes"].Input_12[1]
    to_max_z=bpy.context.object.modifiers["GeometryNodes"].Input_12[2]

def render_screenshot(output_path): # 渲染截图
    bpy.context.scene.render.filepath = output_path # 渲染路径
# Select objects that will be rendered  # 选择渲染的对象
for obj in bpy.context.scene.objects:   # 遍历所有对象
   obj.select_set(False)            # 取消选择
for obj in bpy.context.visible_objects: # 遍历可见的对象
    if not obj.hide_get():        # 可见的对象
        obj.select_set(True)    # 选择

bpy.ops.view3d.camera_to_view_selected()    # 把相机移到选择的对象的中心
bpy.ops.render.render(write_still=True)     # 渲染

argv = sys.argv[sys.argv.index("--") + 1:] # get all args after "--"    # 获取所有参数后"--"
output_dir = argv[0]                    # get output dir               # 获取输出路径
render_screenshot(os.path.join(output_dir, 'render%d.jpeg'))    # 渲染截图

