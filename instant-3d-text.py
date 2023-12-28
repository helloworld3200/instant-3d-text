import bpy
import os
from subprocess import run
from re import search

# Modify these variables
SIZE = 1
EXTRUDE_DEPTH = 0.1
# This is the folder where the text will be saved.
OUTPUT_PATH = "C:/Users/You/Documents"

# Change this to False if you want to keep the material files associated with the OBJ. Otherwise, it'll delete them by default.
REMOVE_MTL = True

# Shouldn't need to change these
TEXT_SOURCE = "source.txt"
MATCH_ENDS_REGEX = ".*_\\d+\.obj$"

def remove_file_with_ext(path: str, ext: str) -> None:
    index = len(ext)
    for file in os.listdir(path):
        if file[-index:].lower() == ext:
            path_to_remove = os.path.join(path, file)
            os.remove(path_to_remove)

def save_to_file(filename: str, output_path: str) -> None:
    duplicates = check_duplicate_filenames(output_path, filename+".obj")
    if duplicates:
        filename = filename+"_"+str(duplicates)
    filename += ".obj"
    
    filepath = os.path.join(output_path, filename)
    
    bpy.ops.export_scene.obj(filepath=filepath, check_existing=True)

# Don't need this anymore, Windows limitation
def remove_dup_ends(path: str) -> None:
    for file in os.listdir(path):
        if search(MATCH_ENDS_REGEX, file):
            index = file.find("_")
            new_file = file[:index]
            new_file += ".obj"
            old_path = os.path.join(path, file)
            new_path = os.path.join(path, new_file)
            os.rename(old_path, new_path)

def check_duplicate_filenames(path: str, target: str) -> int:
    files = os.listdir(path)
    
    lower_target = target.lower()
    
    duplicates = [file for file in files if file.lower() == lower_target]
    duplicates_len = len(duplicates)
    
    return duplicates_len

def delete_all() -> None:
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def write_text(text: str, size: int=SIZE, extrude_depth: float=EXTRUDE_DEPTH, font_type: str="FONT", output_path: str=OUTPUT_PATH, remove_mtl: str=REMOVE_MTL) -> None:
    # These ones don't need to be modified
    POS = (0, 0, 0)
    SCALE = (size, size, 1)
    
    delete_all()
    
    text_data = bpy.data.curves.new(type=font_type, name="Instant3DText_text")
    text_data.body = text
    text_data.extrude = extrude_depth
    
    text_obj = bpy.data.objects.new(name="Instant3DText_object", object_data=text_data)
    
    bpy.context.scene.collection.objects.link(text_obj)
    text_obj.data = text_data
    
    text_obj.scale = SCALE
    text_obj.location = POS
    
    # Optional - for debugging purposes
    bpy.context.view_layer.update()
    
    output_path = os.path.abspath(output_path)
    save_to_file(text, output_path)
    
    if remove_mtl:
        remove_file_with_ext(output_path, ".mtl")
    
def main() -> None:
    with open(os.path.join(OUTPUT_PATH, TEXT_SOURCE), "r") as src:
        lines = src.read().splitlines()
        
        for line in lines:
            write_text(line)
            
        delete_all()

if __name__ == "__main__":
    main()

