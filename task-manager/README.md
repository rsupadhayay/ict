Overview
The Task Manager is a simple command-line application designed to help users manage their daily tasks efficiently. It includes user authentication, allowing each user to log in with a username and password. Once logged in, users can create, view, update, and delete their tasks. Each user's tasks are stored separately, ensuring privacy and security.
Objectives
1. Design and implement a user authentication system (login and registration).
2. Create a task management system that allows users to:
   a. Add, view, mark as completed, and delete tasks.
3. Use file handling to store user credentials and tasks persistently.
4. Create an interactive menu-driven interface to manage tasks.
Key Features
1. User Authentication:
   - Registration: Users can create a new account with a username and password.
   - Login: Users must log in to access their tasks.
   - Credentials are stored in a file named '{username}_credentials.csv'.
2. Task Management:
   - Add Task: Users can add new tasks.
   - View Tasks: Lists all tasks with their status.
   - Mark as Completed: Updates task status to 'Completed'.
   - Delete Task: Removes a task from the list.
   - Tasks are stored in '{username}_tasks.csv'.
3. Interactive Menu:
   - Provides a user-friendly menu with options to add, view, mark as completed, and delete tasks, as well as logout.
Technologies Used
The Task Manager application is built using Python 3. It utilizes the CSV module for file handling and standard input/output for user interaction.
File Structure
The application consists of the following files:
1. task_manager.py: Main script containing all logic.
2. {username}_credentials.csv: File used to store user credentials.
3. {username}_tasks.csv: File used to store user tasks.
How to Run
1. Ensure Python 3 is installed on your system.
2. Save the script as task_manager.py.
3. Run the script using the command: python task_manager.py.
4. Follow the on-screen prompts to register, log in, and manage tasks.
