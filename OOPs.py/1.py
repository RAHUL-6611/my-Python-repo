class Employee:
    # class properties
    no_of_employee = 0
    increment = 1.25
    # inital function
    def __init__(self, fname, lname,salary):     # Dunder method
        self.fname = fname
        self.lname = lname
        self.salary = salary
        # self.email = self.fname + self.lname + "@gmail.com" 
        self.increment = 1.5
        Employee.no_of_employee += 1 
    
    @property
    def email(self):
        if self.fname == None:
            return 'email not found'
        else:    
            return self.fname + self.lname + "@gmail.com"

    @email.setter
    def email(self, given_email):
        name_list = given_email.split('@')[0].split('.')
        print(name_list)
        self.fname = name_list[0]                       #now last name is first name
        # print(self.fname) 
        self.lname = name_list[1]                       #and first name is last
        # print(self.lname)

    # @email.deleter
    # def email(self):
    #     self.fname = None
    #     self.lname = None

    def increments(self):
        # self.salary = int(self.salary*self.increment)       # finds in function
        self.salary = int(self.salary*Employee.increment)     # finds in class
    
    @classmethod                                        # now, cls is class employee
    def change_increment(cls, percent_increase):        # this will change class properties
        cls.increment = percent_increase                # but cant change self/functions propertied
    
    @classmethod               # alternative constructor
    def from_str(cls, emp_string):                      
        fname, lname, salary = emp_string.split("/")       # class method decorator
        return cls(fname, lname, salary)

    @staticmethod                                      # for simple use outside of class
    def isavailable(day):
        if day == "sunday" or day == "saturday":
            return False
        elif day == "Sunday" or day == "Saturday": 
            return False   
        else:
            return True


print(Employee.no_of_employee)                
rahul = Employee('rahul', 'parmar',50000)         # rahul and raghav are two instance of class Employee
print(Employee.no_of_employee)
raghav = Employee('raghav', 'dutta',40000)
print(Employee.no_of_employee)

# c =Employee.from_str("ajay/sable/19000")      #taking vlues from from_str (class method)
# print(c.fname, c.lname)

# print(rahul.fname, rahul.lname)
# print(rahul)                      #gives address
# print(rahul.__dict__)
# print(Employee.__dict__)

# print(raghav.email, rahul.email)                      # from init
# print(raghav.email(), rahul.email())                  # now using separate function
print(raghav.email, rahul.email)                        # after using @property for function
# raghav.lname = "ambedkar"
print(raghav.email)                                      # surname change
raghav.email = "ambedkar.raghav@gmail.com"               # apply changes of email.setter
print(raghav.email)                                      # surname change
# del raghav.email
# print(raghav.email)                                      



# print(rahul.isavailable('saturday'))
# print(rahul.salary)
# Employee.change_increment(2)
# rahul.increments()
# print(rahul.salary)


# class programmer(Employee):                              # subclass of Employee
#     def __init__(self, fname, lname, salary, prolang, exp):  # overide init in this class
#         super().__init__(self, fname, lname, salary)     # inherits the init functiontakes and run all mentioned
#         self.prolang = prolang                 # takes and run all mentioned properties of init
#         self.exp = exp

#     def increments(self):
#         # self.salary = int(self.salary*self.increment)       # finds in function
#         self.salary = int(self.salary*(Employee.increment + 0.2))     # finds in class


# help(programmer)             # shows all descriptions and work flow
# print(help(programmer))      # no need of print, help prints as it is 

