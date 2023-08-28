import os

def read_files_in_dir(dir_name):
    dir_contents = [one_file 
                    for one_file in os.listdir(dir_name) 
                    if os.path.isfile(dir_name + one_file)]
    
    for one_file in dir_contents:
        file_path = dir_name + one_file
        with open(file_path, encoding="utf-8") as current_file:
            for one_line in current_file:
                print(one_line.strip())
    
read_files_in_dir('08_modules_and_packages/')
