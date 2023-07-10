def get_final_line(file):
    """Return the final line in a file"""
    
    with open(file, encoding="utf-8") as f:
        file_content = f.read()
        file_lines = file_content.splitlines()
    
    return file_lines[-1]

print(get_final_line('02_strings/pig_latin.py'))
