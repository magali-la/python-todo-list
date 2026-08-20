# this is the user interface for the to do list - needs to be a while loop so it continues until the user selects to quit
# import os module to check file
import os
import datetime

# import the Task Class
from task import Task
# import utility functions
from todolist import add_task, complete_task, delete_task, list_tasks

# set up an empty task list
task_list = []

# if the data exists, then fill the task_list array line by line
if os.path.isfile('tasks.txt'):


    # use try except for file ops
    try: 
        # read the file - use read mode
        with open('tasks.txt', 'r') as file:
            # loop through the file to extract the data
            for line in file:
                # use destructuring logic to pull each part by splitting by the '|' character, strip removes the \n that was used to make the line keeping it clean before splitting
                title, date_string, completed_string = line.strip().split('|')

                # now need to use a conditional for the date because the "None" if no due date is a string, needs to actually be None so it can be added to the task object correctly
                if date_string == "None":
                    parsed_date = None
                else:
                    # need it in the right format for the Task object - replicate logic
                    parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()

                # need to use conditional for the boolean to put an actual boolean and not True or False as strings for completed
                if completed_string == "True":
                    parsed_completed = True
                else: 
                    parsed_completed = False

                # create the task wth the info
                loaded_task = Task(title, parsed_date, parsed_completed)

                # add it to the array
                task_list.append(loaded_task)    

            # the file exists, notify user successfully saved tasks
            print("You have saved tasks! Loading...")
    except OSError:
        print("Error loading saved tasks.")

# the else is implied, we are starting with an empty list

# create a set with the menu choices for easy lookups and invalid error handling
menu_options = {'A', 'C', 'D', 'L', 'Q'}

# while loop to keep going until quit explicitly breaks the loop
while True:
    # check if it's valid or in the set
    user_choice = input("Todo List Menu:\n\n A. Add Task \n C. Mark Completed Task \n D. Delete Task \n L. List All Tasks \n Q. Quit \n\n Enter your choice (A, C, D, L, or Q): ")

    user_upper = user_choice.upper()

    if user_upper in menu_options:
        # ADD TASK
        if user_upper == 'A':
            # remove the trailing spaces - this is to make sure if they do empty input it can be handled properly instead of having to include other logic
            title = input("Enter a task title: ").strip()

            # if the title is "" then make up stock as title
            if title == "":
                title = "Task"

            due_date = input("Enter due date (YYYY-MM-DD, or press Enter to skip): ").strip()

            if due_date == "":
                # this is the default anyways 
                due_date = None

            # now use the add utility function with the input
            add_task(task_list, title, due_date)

        # PICK AN INDEX - COMPLETE A TASK 
        elif user_upper == 'C':
            # use a try except in case it's not an integer or doesn't exist in the list
            try:
                # do -1 bc list i 0-indexed, it'll be stored by number
                index = int(input("Enter a task number to complete: ")) - 1

                # because of python, a negative will just loop from the back so raise an error if the user puts in 0 - the list should start at 1 anyways
                if index < 0:
                    raise IndexError

                # the function will catch the error when it tries to access the index and it'll be flagged as a value error here
                complete_task(task_list, index)

            except (ValueError, IndexError):
                print("Not a valid task number.")

        # PICK AN INDEX - DELETE A TASK
        elif user_upper == 'D':
            try:
                index = int(input("Enter a task number to delete: ")) - 1

                if index < 0:
                    raise IndexError

                # will catch false index when function attempts to use it
                delete_task(task_list, index)

            except (ValueError, IndexError):
                print("Not a valid task number.")

        # VIEW ALL TASKS
        elif user_upper == 'L':
            list_tasks(task_list)

        elif user_upper == 'Q':
            # TO DO: eventually overwrite the data into the .txt file to save it before quitting
            print("Saving your todo.\n Exiting todo list!")
            try:
                # open in write mode
                with open('tasks.txt', 'w') as file:
                    # loop through and add it to file per task object
                    for task in task_list:
                        # best to separate the data by some character so that loading is successful splitting
                        file.write(f"{task.title}|{task.due_date}|{task.completed}\n")              
            except OSError:
                print(f"Issue saving file. Returning to menu")
                # continue so it doesn't quit without saving anything
                continue
            # break to quit the loop
            break
    else:
        print(f"{user_choice} is not a valid option. Try again")
        # continue the loop to start over again
        continue