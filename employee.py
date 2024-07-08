class Employee:
    def __init__(self,emp_id,name,age,department,salary):
        self.emp_id = emp_id
        self.name = name
        self.age= age
        self.department = department
        self._salary = salary
        
        def get_details(self):
            return{
                "ID":self.emp_id,
                "ID":self.name,
                "ID":self.age,
                "ID":self.department,
                "ID":self._salary
            }
            
        def update_details(self,name=None,age = None,department = None,salary = None):
            if name:
                self.name = name
            if age:
                self.age = age
            if department:
                self.department = department
            if salary:
                self._salary = salary
        
        