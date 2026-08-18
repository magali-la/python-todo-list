# this is the user interface for the to do list - needs to be a while loop so it continues until the user selects to quit
# import os module to check file
import os

# import the Task Class
from task import Task
# import utility functions
from todolist import add_task, complete_task, delete_task, list_tasks

# set up an empty task list
task_list = []

# if the data exists, then fill the task_list array line by line
if os.path.isfile('tasks.txt'):
    # loop through the file to extract the data
    # todo - actually get the file and perform operations to import it into task list
    print("You have saved tasks!")

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
            print("Exiting todo list!")
            # break to quit the loop
            break
    else:
        print(f"{user_choice} is not a valid option. Try again")
        # continue the loop to start over again
        continue