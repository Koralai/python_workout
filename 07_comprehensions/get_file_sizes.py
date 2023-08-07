import os

def get_file_sizes(dir_path):
    """
    Return a dictionary that shows the files in a directory 
    and the size of each file.
    """
    directory = os.listdir(path=dir_path)
    return {file_name: os.stat(f"{dir_path}{file_name}").st_size
            for file_name in directory
            if os.path.isfile(f"{dir_path}{file_name}")}
    
print(get_file_sizes('05_files/'))
