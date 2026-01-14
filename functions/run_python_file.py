import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    try:
        abspath = os.path.abspath(working_directory)
        fullpath =  os.path.join(abspath, file_path)
        target = os.path.normpath(fullpath)

        if os.path.commonpath([abspath, target]) != abspath:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target]
        if args:
            command.extend(args)
        completed = subprocess.run(command, cwd = abspath, capture_output = True, text = True, timeout = 30)

        returnstring = ""
        if completed.stdout != "":
            returnstring += f"STDOUT: {completed.stdout}\n"
        if completed.stderr != "":
            returnstring += f"STDERR: {completed.stderr}\n"
        if completed.stdout == "" and completed.stderr == "":
            returnstring += f"No output produced"
        if completed.returncode != 0:
            returnstring = f"Process exited with code {completed.returncode}\n" + returnstring
        return returnstring
    

    except Exception as e:
        return f"Error: executing Python file: {e}"
