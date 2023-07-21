import os
import json

def sort_scores_by_subject(list_of_students):
    """
    Take a list of student scores and return the scores sorted by subject
    """
    scores = {}
    
    for student in list_of_students:
        for subject, score in student.items():
            if subject not in scores:
                scores[subject] = [score]
            else:
                scores[subject].append(score)
            
    return scores
        

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
                student_data = json.load(f)
                print(sort_scores_by_subject(student_data))
                

print(get_scores('05_files/json/scores/'))
