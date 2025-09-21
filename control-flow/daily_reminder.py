# Personal Daily Reminder
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Match case for priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Note: '{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unknown priority."

# If statement to modify reminder
if time_bound == "yes":
    reminder = reminder + " It requires immediate attention today!"
else:
    if priority == "low":
        reminder = reminder + " Consider completing it when you have free time."
    else:
        reminder = reminder + " This task is not time-bound, you can schedule it more flexibly."

# Final output
print(reminder)
