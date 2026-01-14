import os


def write_file(working_directory, file_path, content):
    try:
        abspath = os.path.abspath(working_directory)
        fullpath =  os.path.join(abspath, file_path)
        target = os.path.normpath(fullpath)

        if os.path.commonpath([abspath, target]) != abspath:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        parent_dir = os.path.dirname(target)
        os.makedirs(parent_dir, exist_ok=True)

        with open(target, "w") as openfile:
            openfile.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: writing file:{e}"
