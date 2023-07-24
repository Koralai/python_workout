import os

def describe_dir_contents(dir_name):
    """
    Take a directory name. Return information about each file in that directory
    (i.e., file name, file size, modification timestamp).
    """
    
    dir_data = []
    
    dir_contents = os.listdir(dir_name)
    for item in dir_contents:
        item_path = os.path.join(dir_name, item)
        
        if os.path.isfile(item_path):
            file_data = {}
            file_data['file_name'] = item
            file_data['file_size'] = os.stat(item_path).st_size
            file_data['mod_timestamp'] = os.stat(item_path).st_mtime
            dir_data.append(file_data)
    
    return dir_data 
    
print(describe_dir_contents('02_strings/'))
