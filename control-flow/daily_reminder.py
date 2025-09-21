# Personal Daily Reminder
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
timebound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        if task is timebound.lower() == "yes":
                print(f" {task} is a high priority and time-bound task. Complete it as soon as possible! ")
        print(f" {task} is a high priority task and should be done first. ")
    case "medium":
        if task is timebound.lower() == "yes":
                print(f" {task} is a medium priority and time-bound task. Complete it soon! ")   
        print(f" {task} is a medium priority task and should be done after high priority tasks. ")
    case "low":
        if task is timebound.lower() == "yes":
                print(f" {task} is a low priority and time-bound task. Complete it when possible! ")
        print(f" {task} is a low priority task and can be done later. ")  
if task is not None and timebound.lower() == "no":
    print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
# This script helps users manage their daily tasks by prioritizing them based on urgency and importance.
    