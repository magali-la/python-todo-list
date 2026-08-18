# this is the user interface for the to do list - needs to be a while loop so it continues until the user selects to quit
# import os module to check file
import os

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
        if user_upper == 'Q':
            print("Exiting todo list!")
            # break to quit the loop
            break
    else:
        print(f"{user_choice} is not a valid option. Try again")
        # continue the loop to start over again
        continue