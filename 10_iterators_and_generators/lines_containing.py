import os

def all_lines_with(dir_name, phrase):
    """
    A generator that yields every line from every file in a directory
    if it contains a certain string.
    """
    
    dir_contents = (one_file 
                    for one_file in os.listdir(dir_name) 
                    if os.path.isfile(os.path.join(dir_name, one_file)))
    
    for one_file in dir_contents:
        file_path = os.path.join(dir_name, one_file)
        
        with open(file_path, encoding="utf-8") as current_file:
            for one_line in current_file:
                if phrase in one_line:
                    yield one_line.strip()
    
for a_line in all_lines_with('02_strings/', 'careful'):
    print(a_line)
