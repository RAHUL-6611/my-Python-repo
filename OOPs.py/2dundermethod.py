# Dunder / Magic methods
# Dunder means double underscores at prefix and suffix
# used for operator overloading

class Employee:
    # class properties
    no_of_employee = 0
    increment = 1.25
    # inital function
    def __init__(self, fname, lname,salary):     # Dunder method
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 1.5
        Employee.no_of_employee += 1 


print(Employee.no_of_employee)                
a = Employee('rahul', 'parmar',50000)         # a and b are two instance of class Employee
print(Employee.no_of_employee)
b = Employee('raghav', 'dutta',40000)
print(Employee.no_of_employee)

# __init__,__add__,rapr ,str, etc 