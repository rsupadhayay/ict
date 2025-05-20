import csv
import os

# Function to register a new user
def register():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    
    with open(f"{username}_credentials.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    
    print("✅ Registration successful!")

# Function to login an existing user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    try:
        with open(f"{username}_credentials.csv", 'r') as file:
            reader = csv.reader(file)
            stored_username, stored_password = next(reader)
            if username == stored_username and password == stored_password:
                print("✅ Login successful!")
                return username
            else:
                print("❌ Invalid credentials. Please try again.")
                return None
    except FileNotFoundError:
        print("❌ User not found. Please register first.")
        return None

# Function to add a task
def add_task(username):
    task = input("Enter the task: ")
    status = "Pending"
    
    with open(f"{username}_tasks.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([task, status])
    
    print("✅ Task added successfully!")

# Function to view tasks
def view_tasks(username):
    try:
        with open(f"{username}_tasks.csv", 'r') as file:
            reader = csv.reader(file)
            tasks = list(reader)
            if not tasks:
                print("📭 No tasks found.")
                return
            
            for i, (task, status) in enumerate(tasks, start=1):
                print(f"{i}. 📝 {task} | Status: {status}")
    except FileNotFoundError:
        print("📭 No tasks found.")

# Function to mark a task as completed
def mark_task_completed(username):
    view_tasks(username)
    task_number = int(input("Enter the task number to mark as completed: "))
    
    try:
        with open(f"{username}_tasks.csv", 'r') as file:
            reader = csv.reader(file)
            tasks = list(reader)
        
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1][1] = "Completed"
            
            with open(f"{username}_tasks.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(tasks)
            
            print("✅ Task marked as completed!")
        else:
            print("❌ Invalid task number.")
    except FileNotFoundError:
        print("📭 No tasks found.")

# Function to delete a task
def delete_task(username):
    view_tasks(username)
    task_number = int(input("Enter the task number to delete: "))
    
    try:
        with open(f"{username}_tasks.csv", 'r') as file:
            reader = csv.reader(file)
            tasks = list(reader)
        
        if 1 <= task_number <= len(tasks):
            tasks.pop(task_number - 1)
            
            with open(f"{username}_tasks.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(tasks)
            
            print("✅ Task deleted!")
        else:
            print("❌ Invalid task number.")
    except FileNotFoundError:
        print("📭 No tasks found.")

# Function to display the menu
def display_menu():
    print("\n📋 Task Manager")
    print("1. ➕ Add task")
    print("2. 📋 View tasks")
    print("3. ✅ Mark task as completed")
    print("4. ❌ Delete task")
    print("5. 🔐 Logout")

# Main function to run the task manager
def main():
    print("🔐 Welcome to the Task Manager")
    while True:
        print("1. 📝 Register")
        print("2. 🔑 Login")
        print("3. ❌ Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username:
                while True:
                    display_menu()
                    choice = input("Enter your choice: ")
                    
                    if choice == '1':
                        add_task(username)
                    elif choice == '2':
                        view_tasks(username)
                    elif choice == '3':
                        mark_task_completed(username)
                    elif choice == '4':
                        delete_task(username)
                    elif choice == '5':
                        print("🔐 Logging out...")
                        break
                    else:
                        print("❗ Invalid choice. Please try again.")
        elif choice == '3':
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()