from employee import Employee
from database import *
import sqlite3


def display_menu():
    print("\n EMPLOYEE MANAGEMENT SYSTEM")
    print("1.Add Employee")
    print("2.Update Employee")
    print("3.Delete Employee")
    print("4.view Employee")
    print("5.Exit")
    
    
def get_employee_inputs():
    emp_id = int(input("Entre employee ID: "))
    Name = input("Entre Employee name: ")
    age = int(input("Enter Employee age: "))
    department = input("Entre Employee department: ")
    salary = float(input("Entre Emplooyee salary: "))
    
def main():
    db = Database()
    
    while True:
        display_menu()
        choices = input("Entre Your Choice: ")
            
        if choices =='1':
            employee = get_employee_inputs()
            db.add_employee(employee)
            print("Employee added successfuly")
            
        elif choices =='2':
            emp_id  = int(input("Entre Employee ID to update: "))
            name = input("Entre name to update (leave blank to skip): ")
            age = int(input("Entre age to update (leave blank to update): "))
            department = input("Entre departmnet to update (leave blank to skip): ")
            salary = float(input("Entre Age to update (leave blank to skip): "))
            
            db.update_employee(emp_id,name if name else None,age if age else None,department if department else None,salary if salary else None)
            print("employee Updated Successfully")
            
        elif choices == '3':
            emp_id = int(input("Entre ID of the Employee you wish you wish to update: "))
            db.delete_employee(emp_id)
            
            print('Employee Deleted Successfully')
            
        elif choices == '4':
            emp_id = int(input("Entre Employee Id you want to view: "))
            
            employee = db.get_employee(emp_id)
            
            if employee:
                print(f"ID:{employee[0]},Name:{employee[1]},Department:{employee[2]},Salary:{employee[3]}")
            else:
                print("Employee Not Found")
                
        elif choices == '5':
            print("exiting...")
            break
        
        else:
            print("Invalid Choice.Please Try Again")
            
            
if __name__ =="__main__":
    main()
             
                