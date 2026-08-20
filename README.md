# Python To-Do List
This script uses modules, file operations, and error handling methods in python for a to-do list with menu items for different operations

## Menu Selection
### Case Normalization
Case normlization used to accept upper or lowercase valid menu options. Set is used for O(1) lookups to check if the uppercase version of the user input is in the set. 

![alt text](/assets/image2.png)

### Error Handling
Users are gracefully notified when menu selection does not match the options (A, C, D, L, Q). A continuous loop will restore the menu rather than stop the script

![alt text](/assets/image.png)

## Add a Task
### No Errors
![alt text](/assets/image3.png)

### Missing Title or Incorrect Date Format
Due dates are optional. User are notified if they input an incorrect format, the date will be omitted.
Titles not inputted default to 'Task'.

![alt text](/assets/image4.png)


## Completing Tasks
### Success
Ternary updates the string to include an `X` for completed tasks

![alt text](/assets/image14.png)

### Error Handling - Index Error
Errors caught in `main.py` for invalid user input for index

![alt text](/assets/image13.png)

## Deleting Tasks
### Success

![alt text](/assets/image11.png)

### Error Handling - Index Error
If the user inputs 0, the script automatically asks user to use the numbered list and will subtract 1 to pull the correct index. Error message will print.

![alt text](/assets/image9.png)

Alternatively, if the user inputs an out of bounds index, the `delete_task` utility will bubble up to the `IndexError` in `main.py`

![alt text](/assets/image10.png)


## List All Tasks
Tasks are enumerated.

![alt text](/assets/image5.png)

### Overdue Tasks Flag
Display tasks with an additional flag if a task isn't completed, a task has a due date, and that today's date is after the due date listed.

![alt text](/assets/image12.png)


## Saving and Loading Logic
The script saves last known task_list array state within a text file and uses error handling for OSErrors. Loading properly converts potential 'None' strings within the .txt file into None for date and similarly for 'True' or 'False' strings into booleans for Task instance creation

### Once the user quits
If the .txt is created if it doesn't exist with the tasks in the array

![alt text](/assets/image6.png)

Tasks are stored as pure strings with `|` as a separation.

![alt text](/assets/image7.png)

Saving example with no due date

![alt text](/assets/image15.png)

### Once the user boots the script
Conditional statement checks if a file exists, reads each line, then creates a new `Task` instance to append to the array. User is notified that a file exists with saved tasks.

![alt text](/assets/image8.png)