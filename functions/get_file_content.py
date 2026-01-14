import os

def get_file_content(working_directory, file_path):
    try:
        abspath = os.path.abspath(working_directory)
        fullpath =  os.path.join(abspath, file_path)
        target = os.path.normpath(fullpath)

        if os.path.commonpath([abspath, target]) != abspath:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target) as openfile:
            file_content = openfile.read(10000)
            if openfile.read(1):
                file_content += f'[...File "{file_path}" truncated at 10000 characters]'
        return file_content
    
    except Exception as e:
        return f"Error: getting file contents: {e}"
