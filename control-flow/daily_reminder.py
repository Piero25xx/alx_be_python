# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("priority (high/medium/low): ").lower()

# Prompt if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
reminder = ""

# Use a match case statement to react differently based on the task's priority
match priority:
    case "high":
        reminder = f"Reminder: Finish {task} is high priority task'"
    case "medium":
        reminder = f"Reminder: Your {task} task is Medium priority"
    case "low":
        reminder = f"Reminder: Your {task} task is low priority"
    case _:
        reminder = f"Task: {task} (priority not specified)"

# Use an if statement to modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += "that requires immediate attention today!"

# Provide a customized reminder
print(reminder)
