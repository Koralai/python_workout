import os

def read_files_in_dir(dir_name):
    dir_contents = [one_file 
                    for one_file in os.listdir(dir_name) 
                    if os.path.isfile(dir_name + one_file)]
    print(dir_contents)
    
read_files_in_dir('08_modules_and_packages/')
