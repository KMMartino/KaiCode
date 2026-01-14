import os

def get_files_info(working_directory, directory="."):
    try:
        abspath = os.path.abspath(working_directory)
        fullpath =  os.path.join(abspath, directory)
        target = os.path.normpath(fullpath)

        if os.path.commonpath([abspath, target]) != abspath:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target):
            return f'Error: "{directory}" is not a directory'
        
        files = []
        for path in os.listdir(target):
            fullpath = os.path.join(target, path)
            filesize = os.path.getsize(fullpath)
            is_dir = os.path.isdir(fullpath)
            files.append(f"- {path}: file_size={filesize} bytes, is_dir={is_dir}")
        result = "\n".join(files)

        return result
    
    except Exception as e:
        return f"Error: getting file info: {e}"

