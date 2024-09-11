import os
import shutil
import py_compile

# List of files and folders to check
files = [
    'main.py',
    'icon.ico',
    'requirements.txt',
    ('UI', 'UI/'),  # Here you place the path of your folders
]

# Create the dist folder if it doesn't exist
dist_dir = 'dist'
if not os.path.exists(dist_dir):
    os.makedirs(dist_dir)


def compile_and_move(file_path: str):
    """
    The function `compile_and_move` compiles a Python file and moves the compiled file to a specified
    directory.

    :param file_path: 
        The `file_path` parameter in the `compile_and_move` function is the path to the
        Python file that you want to compile and move to a specified destination directory
    """
    try:
        # Create the directory structure in dist
        relative_path = os.path.relpath(file_path)
        dist_path = os.path.join(dist_dir, relative_path)
        dist_folder = os.path.dirname(dist_path)
        if not os.path.exists(dist_folder):
            os.makedirs(dist_folder)

        # Compile the Python file
        py_compile.compile(file_path, cfile=dist_path + 'c')
        print(f"Compiled: {file_path}")
    except py_compile.PyCompileError as e:
        print(f"Failed to compile: {file_path}\nError: {e}")


def move_file(file_path: str):
    """
    The function `move_file` copies a file to a specified destination directory while creating the
    necessary directory structure.
    
    :param file_path: 
        The `file_path` parameter in the `move_file` function is the path to the file that
        you want to move to a destination directory. This function creates the necessary directory structure
        in the destination directory and then moves the file to that location using `shutil.copy2`. If any
        errors occur during
    :type file_path: str
    """
    try:
        # Create the directory structure in dist
        relative_path = os.path.relpath(file_path)
        dist_path = os.path.join(dist_dir, relative_path)
        dist_folder = os.path.dirname(dist_path)
        if not os.path.exists(dist_folder):
            os.makedirs(dist_folder)

        # Move the file
        shutil.copy2(file_path, dist_path)
        print(f"Moved: {file_path}")
    except Exception as e:
        print(f"Failed to move: {file_path}\nError: {e}")


def process_files(files):
    for item in files:
        if isinstance(item, tuple):
            # It is a folder
            folder_path = item[1]
            for root, _, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(root, filename)
                    if filename.endswith('.py'):
                        compile_and_move(file_path)
                    else:
                        move_file(file_path)
        else:
            # It is a file
            if item.endswith('.py'):
                compile_and_move(item)
            else:
                move_file(item)


# Process the files and folders
process_files(files)