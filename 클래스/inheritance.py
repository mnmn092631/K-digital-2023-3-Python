class Person:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def getName(self): 
        print(self.name) 

    def getAge(self): 
        print(self.age) 

class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self.employeeID = employeeID
    
    def getID(self):
        print(self.employeeID)

employee1 = Employee("동양", 65, 2019)
employee1.getName()
employee1.getAge()
employee1.getID()