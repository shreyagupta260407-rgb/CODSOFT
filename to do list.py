import json
import os
from datetime import datetime
TASKS_FILE = "my_tasks.json"
def load_tasks():
    """This function loads all tasks from the json file"""
    print("Loading your tasks...")  # Just for feedback
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as file:
                tasks = json.load(file)
                print("Tasks loaded successfully!")
                return tasks
        except Exception as e:
            print("Sorry, something went wrong while loading tasks.")
            print("Starting with empty list.")
            return []
    else:
        print("No previous tasks found. Starting fresh!")
        return []

def save_tasks(tasks):
    """This function saves all tasks to the json file"""
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
        # print("Tasks saved successfully!")  # Uncomment if you want to see this message
    except Exception as e:
        print("Warning: Could not save your tasks this time.")
def add_task(tasks):
    """Add a new task to the list"""
    print("\n--- ADD NEW TASK ---")
    task_name = input("What is the task you want to add? : ").strip()
    
    if task_name == "":
        print("Task name cannot be empty!")
        return
    
    new_task = {
        "id": len(tasks) + 1,
        "description": task_name,
        "status": "Pending",
        "created_date": datetime.now().strftime("%d-%m-%Y %H:%M")
    }
    
    tasks.append(new_task)
    print(f"Task added successfully: '{task_name}'")

def view_tasks(tasks):
    """Display all tasks in a nice way"""
    print("\n" + "="*60)
    print(" " * 20 + "YOUR TO-DO LIST")
    print("="*60)
    
    if not tasks:
        print("No tasks available yet.")
        print("Add some tasks to get started!")
        return
    
    for i, task in enumerate(tasks, 1):
        print(f"{i}. ", end="")
        
        if task["status"] == "Completed":
            print("✅ ", end="")
        else:
            print("⭕ ", end="")
            
        print(task["description"])
        print(f"   Status     : {task['status']}")
        print(f"   Created on : {task['created_date']}")
        print("-" * 50)

def mark_completed(tasks):
    """Mark any task as completed"""
    view_tasks(tasks)
    
    if not tasks:
        return
    
    print("\n--- MARK TASK AS COMPLETED ---")
    try:
        task_no = input("Enter task number to mark as completed: ").strip()
        task_index = int(task_no) - 1
        
        if 0 <= task_index < len(tasks):
            tasks[task_index]["status"] = "Completed"
            print("Task marked as Completed! Well done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number only.")

def delete_task(tasks):
    """Delete a task from the list"""
    view_tasks(tasks)
    
    if not tasks:
        return
    
    print("\n--- DELETE A TASK ---")
    try:
        task_no = input("Enter task number to delete: ").strip()
        task_index = int(task_no) - 1
        
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f"Task deleted: '{deleted_task['description']}'")
            
            # Update the id of remaining tasks
            for index, task in enumerate(tasks):
                task["id"] = index + 1
        else:
            print("Invalid task number entered!")
    except ValueError:
        print("Please enter a valid number.")

def show_menu():
    """Display the main menu options"""
    print("\n" + "-"*50)
    print("              MAIN MENU")
    print("-"*50)
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete a Task")
    print("5. Exit Program")
    print("-"*50)


def main():
    """This is the main function that runs the whole program"""
    print("\n" + "="*70)
    print("   WELCOME TO SIMPLE TO-DO LIST")
    print("   Built for Codsoft Internship")
    print("   Let's organize your tasks!")
    print("="*70)
    
    # Load tasks at the beginning
    tasks = load_tasks()
    
    while True:
        show_menu()
        
        choice = input("\nPlease enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("\nThank you for using the To-Do List!")
            print("Your tasks have been saved.")
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option! Please choose a number between 1 to 5.")
        
        # Save tasks after every operation
        save_tasks(tasks)


# This is how we run the program
if __name__ == "__main__":
    main()