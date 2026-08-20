# TO DO - ADD LOGIC TO THE UTILITIES

# module - utility functions for the todo list which takes in parameters from the task and task list
# import datetime
import datetime
# import Task class
from task import Task

# add a task - if date i included, parse with datetime.date in YYYY-MM-DD format - error handling to let user know
def add_task(task_list, title, due_date=None):
    print("Adding task")

    # need to get the date first and initialise it to None as is the default to avoid typeerrors
    parsed_date = None

    # only try if the due date isn't none
    if due_date != None:
        # the date needs to be in the right format do a try except to catch the issue
        try:
            # reassign it
            parsed_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()

        # this is just a warning - it's going to append anyways
        except ValueError:
            print("Incorrect date format, creating task without a due date.")

    # assuming this didn't catch an error or assuming it was always None, then used the parsed_date
    new_task = Task(title, parsed_date)
    # add the task to the list without due date
    task_list.append(new_task)


# complete a task - task at index marked completed - error handling if index doesn't exist
def complete_task(task_list, index):
    print("Completing task")


# delete a task - remove at index - error handling
def delete_task(task_list, index):
    # the error handling in main.py handles it o if it has an error, it'll use main.py message
    # use index and try to pop it - store it to use the title in the string
    deleted_task = task_list.pop(index)

    # the task is deleted, but notify user - the index should be correct if it gets to this point
    print(f"Deleting task #{index + 1}. {deleted_task.title}")

# show all tasks - formatted list with all info - index, status, title, due date
# needs to also show if due date is after today's date, then say how many days in between
def list_tasks(task_list):
    print("Listing all task")

    # conditional, if there's no tasks print a message
    if len(task_list) == 0:
        print("No tasks in the list")
        # return needed to stop this loop
        return
    # otherwise use enumerate method to number the tasks in the array as they are printed
    for i, task in enumerate(task_list, start=1):
        # the task has already been formatted with the string method, just input it
        print(f"{i}. {task}")