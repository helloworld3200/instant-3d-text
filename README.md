# instant-3d-text
> Instantly generate 3d text models using blender API.

### Dependencies

- Blender (with API)

### How to Use

1. Create a **new project** in blender. This will delete everything in the project before creating the text, so make sure the project is new.

2. Paste the contents of `instant-3d-text.py` into the Scripting section.

3. At the top of the script, change the folder to save the models to. **Make sure that the path to the folder uses forwards slashes (these /) and not backward slashes (these \\).** Optionally, change size and depth to the ones that you want.  

4. For the text you actually want to create, create a `source.txt` file in the folder you chose for the models to be saved in - each line is an individual object. For example, if you have `Hello World` this will count as one object but  
 `Hello`  
 `World` will be 2 objects. I have included an `example-source.txt` file with all uppercase/lowercase letters of the alphabet and all digits from 0-9 for convenience.

4. Run the program and enjoy!

### Use from Command Line

To use this from the CLI, ensure you are using the CLI in the folder of where the code is stored.
Then, run the command: `blender -b -P "instant-3d-text.py"`

### Limitations

- Currently, this only exports to an OBJ format.
- This does not support different fonts
- It can't make italic/bold text.
- You can only include text that is also an acceptable filename.

If people actually use this project, I might add these features eventually.
