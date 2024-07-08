# EMC

Sure, here's a README draft for your project:

---

# Employee Management System

## Overview

This Python project is an Employee Management System using SQLite for data storage. It allows users to perform CRUD (Create, Read, Update, Delete) operations on employee records.

## Features

- **SQLite Database**: Stores employee data persistently.
- **Employee Class**: Represents individual employees with attributes like name, age, department, and salary.
- **Database Class**: Manages interactions with the SQLite database, including methods for adding, retrieving, updating, and deleting employee records.
- **CLI Interface**: Basic command-line interface (CLI) to demonstrate usage.

## Requirements

- Python 3.x
- SQLite 3 (usually comes bundled with Python)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your/repository.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Usage

### Adding an Employee

To add a new employee, run the application and choose the option to add an employee. Enter the employee details when prompted.

### Viewing Employee Details

You can view details of a specific employee by selecting the option to view employees and entering the employee ID.

### Updating Employee Details

To update employee details, choose the update option, enter the employee ID, and provide the new details for name, age, department, or salary.

### Deleting an Employee

To delete an employee record, select the delete option, and enter the employee ID of the employee you want to remove from the database.

## Example

```python
# Example usage in Python script
from employee import Employee
from database import Database

# Create a new employee instance
emp1 = Employee("John Doe", 30, "IT", 50000.0)

# Create a database instance
db = Database()

# Add employee to database
db.add_employee(emp1)

# Get employee details
employee_details = db.get_employee(emp1.emp_id)
print("Employee Details:", employee_details)

# Update employee details
db.update_employee(emp1.emp_id, name="John Smith", salary=55000.0)

# Delete employee from database
db.delete_employee(emp1.emp_id)
```

## Credits

Created by solo925

---
