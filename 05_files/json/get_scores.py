import os
import json

def get_scores(dir_name):
    """
    Take the name of a directory that should hold data on student scores.
    Return a summary of the scores found in the directory.
    """
    dir_contents = os.listdir(dir_name)
    
    for item in dir_contents:
        path_full = os.path.join(dir_name, item)
        
        if os.path.isfile(path_full):
            with open(path_full, encoding='utf-8') as f:
                print(json.load(f))

print(get_scores('05_files/json/scores/'))
