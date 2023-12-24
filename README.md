# instant-3d-text
> Instantly generate 3d text models using blender API.

### Dependencies

- Blender (with API)

### How to Use

1. Create a **new project** in blender. This will delete everything in the project before creating the text, so make sure the project is new.

2. Paste the contents of `instant-3d-text.py` into the Scripting section.

3. At the top of the script, change the folder to save the models to (this is the OUTPUT_PATH variable), size and depth to the ones that you want.  

4. For the text you actually want to create, create a `source.txt` file in the folder you chose for the models to be saved in - each line is an individual object. For example, if you have `Hello World` this will count as one object but  
 `Hello`  
 `World` will be 2 objects.

4. Run the program and enjoy!

### Limitations

- Currently, this only exports to an OBJ format.  
- This does not support different fonts or italic/bold.

If people actually use this project, I might add these features eventually. 
