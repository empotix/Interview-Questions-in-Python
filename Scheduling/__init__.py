'''
Task schedule: given a sequence of task like A B C(means 3 different tasks), 
and a coldtime, which means you need to wait for that much time to start 
next [same] task. 

Input: string, n 
Output: the best task-finishing sequence. 

eg. input: AAABBB, 2 
Output: AB_AB_AB 
( "_" represents do nothing and wait)
'''

from collections import Counter

def schedule(tasks, n):
    
    #Gives us the tasks in the descending order of frequency
    tasks = Counter(tasks)
    tasks = sorted(tasks.items(), key=lambda x: x[1], reverse=True)
    
    #Keeps track of the last time a task was performed
    check_last = {}
    i = 0
    
    while len(tasks) != 0:
        current_task = findNextPossibleTask(tasks, check_last, i)
        
        if current_task:
            tasks.remove(current_task)
            print(current_task[0])
            remaining_count = current_task[1] - 1
            
            check_last[current_task[0]] = i
            
            #If we still have more of the current task to complete, add it to
            #the end of the list
            if remaining_count > 0:
                tasks.append((current_task[0], remaining_count))
        else:
            print("_")
            
        i += 1
          
            
def findNextPossibleTask(tasks, check_last, i):
    
    for task in tasks:
        current_task = task[0]
        last_time_of_task = check_last.get(current_task, -n-1)
        
        #If we have satisfied the criteria of waiting for time n, we can now 
        #do this task
        if i - last_time_of_task > n:
            return task
    
    return None
        
    
tasks = "AAABBB"
n = 2
schedule(tasks, 2)