class Trial:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # self.display()
        
    def display(self):
        return f"{self.name} is {self.age} years old"
    
    
obj = Trial("Solomon",23)

print(obj.display())