# Personal Daily Reminder
task = input("Enter your task: ")
timebound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")
match priority:
    case "high":
        print(f"Finish: {task} is a high priority task and should be done first. ")
    case "medium":
        print(f"Finish: {task} is a medium priority task and should be done after high priority tasks. ")
    case "low":
        print(f"Finish: {task} is a low priority task and can be done later. ")  
if task is not None and timebound.lower() == "no":
    print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    