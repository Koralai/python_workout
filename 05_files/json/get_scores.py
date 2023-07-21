import os
import json

def sort_scores_by_subject(list_of_students):
    """
    Take a list of scores sorted by student; 
    return the scores sorted by school subject.
    """
    scores = {}
    
    for student in list_of_students:
        for subject, score in student.items():
            if subject not in scores:
                scores[subject] = [score]
            else:
                scores[subject].append(score)
            
    return scores
        

def summarize_scores(dir_name):
    """
    Take the name of a directory that should hold json data on student scores.
    Print a summary of the scores found in each json file.
    """
    dir_contents = os.listdir(dir_name)
    
    for item in dir_contents:
        path_full = os.path.join(dir_name, item)
        
        if os.path.isfile(path_full):
            print(f"{path_full}:")
            
            with open(path_full, encoding='utf-8') as f:
                student_data = json.load(f)
                score_data = sort_scores_by_subject(student_data)
                
                for subject, scores in score_data.items():
                    print(f"\t{subject}: min {min(scores)}, max {max(scores)}, "
                          f"average {sum(scores)/len(scores):.2f}")
                

print(summarize_scores('05_files/json/scores/'))
