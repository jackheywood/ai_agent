import os


def get_files_info(working_directory, directory=None):

    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir

    if directory:
        target_dir = os.path.abspath(
            os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    try:
        files = []

        for entry in os.listdir(target_dir):
            path = os.path.join(target_dir, entry)
            size = os.path.getsize(path)
            is_dir = os.path.isdir(path)
            files.append(f"- {entry}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(files)

    except Exception as e:
        return f"Error: {e}"
