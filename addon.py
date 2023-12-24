import bpy
import bmesh 


class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "NGon Finder"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "NGon Finder"

    def draw(self, context):
        self.layout.row().operator("object.simple_operator")


class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Find"

    def execute(self, context):
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='FACE')

        # Get the active mesh
        obj = bpy.context.edit_object
        me = obj.data


        # Get a BMesh representation
        bm = bmesh.from_edit_mesh(me)


        for face in bm.faces:
            if len(face.verts) == 4:
                face.select_set(False)
            else:
                face.select_set(True)


        # Show the updates in the viewport
        # and recalculate n-gon tessellation.
        bmesh.update_edit_mesh(me, loop_triangles=True)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(HelloWorldPanel)
    bpy.utils.register_class(SimpleOperator)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)
    bpy.utils.unregister_class(SimpleOperator)


if __name__ == "__main__":
    register()
