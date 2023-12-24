import bpy
import os

# Modify these variables
SIZE = 2
EXTRUDE_DEPTH = 1
# This is the folder where the text will be saved.
OUTPUT_PATH = "C:/Users/You/Documents/"

# Shouldn't need to change this
TEXT_SOURCE = "source.txt"

def delete_all():
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def write_text(text, size, extrude_depth):
    # These ones don't need to be modified
    POS = (0, 0, 0)
    SCALE = (size, size, 1)
    FONT_TYPE = "FONT"
    
    delete_all()
    
    text_data = bpy.data.curves.new(type=FONT_TYPE ,name="Instant3DText_text")
    text_data.body = TEXT
    text_data.extrude = EXTRUDE_DEPTH
    
    text_obj = bpy.data.objects.new(name="Instant3DText_object", object_data=text_data)
    
    bpy.context.scene.collection.objects.link(text_obj)
    text_obj.data = text_data
    
    text_obj.scale = SCALE
    text_obj.location = POS
    
    # Optional - for debugging purposes
    bpy.context.view_layer.update()
    
    bpy.ops.export_scene.obj(filepath=os.path.join(OUTPUT_PATH, text+".obj"))
    
def main():
    with open(os.path.join(OUTPUT_PATH, TEXT_SOURCE), "r") as src:
        lines = src.splitlines()
        
        for line in lines:
            write_text(line, SIZE, EXTRUDE_DEPTH)

if __name__ == "__main__":
    main()