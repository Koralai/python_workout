def run_timing():
    """Takes user inputs for 10K run times and returns the average time"""
    
    run_time_data = []
    entering_data = True
    
    # take and store user inputs until the user presses 'enter'      
    while entering_data is True:
        
        new_time = input("Enter 10K run time (in minutes): ")
        
        if new_time == '':
            entering_data = False
        else:
            run_time_data.append(float(new_time))
        
    # return the average of all the inputs
    run_time_sum = 0
    for time in run_time_data:
        run_time_sum += time
    
    number_of_runs = len(run_time_data)
    
    avg_time = run_time_sum/number_of_runs
    
    return f"Average of {avg_time} minutes over {number_of_runs} runs."

print(run_timing())