def run_timing():
    """Takes user inputs for 10K run times and returns the average time"""
    
    total_time = 0
    number_of_runs = 0
    
    # take and store user inputs until the user presses 'enter' 
         
    while True:    
        new_time = input("Enter 10K run time (in minutes): ")
        
        if not new_time:
            break
        
        number_of_runs += 1
        total_time += float(new_time)
        
    # return the average of all the inputs
        
    avg_time = total_time/number_of_runs
    
    return f"Average of {avg_time:.2f} over {number_of_runs} runs."

print(run_timing())