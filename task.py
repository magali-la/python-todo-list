# Task class with attributes
class Task:
    # define variable and attributes - set false automatically for completed
    def __init__(self, title, due_date=None, completed=False):
        self.title = title
        self.due_date = due_date
        # boolean
        self.completed = completed

    # str method with a formatted string for each task
    def __str__(self):
        # create a check using ternary logic
        check = "X" if self.completed == True else "-"

        # use ternary logic for if a duedate is present or not
        due_string = f"(due {self.due_date})" if self.due_date else ""

        return f"[{check}] {self.title} {due_string}"