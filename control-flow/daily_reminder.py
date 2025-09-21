# Personal Daily Reminder
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
timebound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        reminder = (f" {task} is a high priority task and should be done first. ")
    
    case "medium":
        
        reminder = (f" {task} is a medium priority task and should be done after high priority tasks. ")
    case "low":
     
        reminder = (f" {task} is a low priority task and can be done later. ")  
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")

if timebound.lower() == "yes":
    reminder = (f" {task} Since it is time-bound, complete it as soon as possible!")
else:
    reminder = (f" {task} is a low priority task. Consider completing it when you have free time. ")
    print(reminder)

# This script helps users manage their daily tasks by prioritizing them based on urgency and importance.
