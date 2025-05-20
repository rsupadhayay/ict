Personal Expense Tracker – Documentation
 Overview
The Personal Expense Tracker is a command-line Python application designed to help users manage their daily expenses efficiently. It allows users to log expenses, categorize them, track spending against a monthly budget, and persist data using CSV files for future reference.
Objectives
•	Enable users to add and categorize expenses
•	Allow users to set and monitor a monthly budget
•	Provide persistent storage using CSV files
•	Offer a menu-driven interface for ease of use
Key Features
1. Add Expense
•	Prompts the user for:
•	Date (YYYY-MM-DD)
•	Category (e.g., Food, Travel)
•	Amount
•	Description
•	Stores each expense as a dictionary in a list:
2. View Expenses
•	Displays all recorded expenses in a readable format.
•	Skips or warning about incomplete entries.
•	Ensures data integrity before displaying.
3. Track Budget
•	Allows the user to input a monthly budget.
•	Calculates total expenses and compares them with the budget.
•	Displays:
•	A warning if the budget is exceeded.
•	The remaining balance if within budget.
4. Save and Load Expenses
•	Save: Writes all expenses to a CSV file (expenses.csv) with headers.
•	Load: Reads from the CSV file at startup to restore previous data.
5. Interactive Menu
•	Provides a user-friendly menu with options:
1.	Add expense
2.	View expenses
3.	Track budget
4.	Save expenses
5.	Exit
•	Ensures smooth navigation and functionality execution based on user input.
Technologies Used
•	Python 3
•	CSV module for file handling
•	Standard input/output for user interaction
File Structure
•	expense_tracker.py: Main script containing all logic
•	expenses.csv: File used to store and retrieve expense data
 How to Run
1.	Ensure Python 3 is installed.
2.	Save the script as expense_tracker.py.
3.	Run the script using:
python3 personal-expense-tracker.py
