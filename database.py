import sqlite3
from employee import Employee


class Database:
    def __init__(self,db_name = "employees.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()
        
        def create_table(self):
            query = '''
            CREATE TABLE IF NOT EXISTS employees(
                emp_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                departmnet TEXT NOT NULL,
                salary REAL NOT NULL
                
                )
            '''
            self.conn.execute(query)
            self.conn.commit()
            
            
        def add_employee(self,employee):
            query = ''' 
            
            INSERT INTO employeess(emp_id,name,age,department,salary)VALUES(?,?,?,?,?)
            '''
            self.conn.execute(query,(employees.emp_id,employees.name,employees.age,employees.department,employees._salary))
            self.conn.commit()
            
        def get_employee(self,emp_id):
            query = "SELECT * FROM employees WHERE  emp_id = ?"
            cursor = self.conn.execute(query,(emp_id,))
            return cursor.fetchone()
        
        
        def update_employee(self,emp_id,name = None,age=None,department=None,salary=None):
            current_data=get_employee(emp_id)
            if current_data:
                updated_data = {
                    "name":name if name else current_data[1],
                    "age":age if age else current_data[2],
                    "department":departmnet if department else current_data[3],
                    "salary":salary if salary else current_data[4],
                    
                }
                
                query = ''' UPDATE employees SET name=?,age=?,department=?,salary=? WHERE emp_id=? '''
                
                self.conn.execute = (query,(updated_data['name'],
                updated_data['age'],
                updated_data['departmnet'],
                updated_data['salary'],emp_id))
                
                
                self.conn.commit()
                
                
        def delete_employee(self,emp_id):
            query = "DELETE employees WHERE emp_id = ?"
            
            self.conn.execute(query,(emp_id,))
            self.conn.commit()
            
            
            