import os

def get_file_sizes(dir_path):
    """
    Return a dictionary that shows the files in a directory 
    and the size of each file.
    """
    directory = os.listdir(path=dir_path)
    return {file_name: "placeholder"
            for file_name in directory}
    
print(get_file_sizes('07_comprehensions/'))
