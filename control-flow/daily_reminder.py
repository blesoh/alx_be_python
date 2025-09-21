
# Personal Daily Reminder
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Match case for priority and  If statement to modify reminder

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task and requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task and requires immediate attention today!")
        else:   
            print(f"Reminder: '{task}' is a medium priority task. This task is not time-bound, you can schedule it more flexibly.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task and requires immediate attention today!") 
        else:   
            print(f"Reminder: '{task}' is a low priority task. This task is not time-bound, you can schedule it more flexibly.")
    case _:
        print(f"'{task}' has an unknown priority.")


