# TO DO - ADD LOGIC TO THE UTILITIES

# module - utility functions for the todo list which takes in parameters from the task and task list

# add a task - if date i included, parse with datetime.date in YYYY-MM-DD format - error handling to let user know
def add_task(task_list, title, due_date=None):
    print("Adding task")

# complete a task - task at index marked completed - error handling if index doesn't exist
def complete_task(task_list, index):
    print("Completing task")
# delete a task - remove at index - error handling
def delete_task(task_list, index):
    print("Deleting task")

# show all tasks - formatted list with all info - index, status, title, due date
# needs to also show if due date is after today's date, then say how many days in between
def list_tasks(task_list):
    print("Listing all task")