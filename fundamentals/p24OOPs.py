# class Number:                           # 1. class
#     def sum(self):                      # 2. function
#         return self.a + self.b          # 3. logic

# num = Number()                          # assinging class to var
# num.a = 32                              # inputing values
# num.b = 42                

# s = num.sum()                          # defining function to run
# print(s)                               # output


#-----------------------------------------------------
# what is (self ), why to use self
#self is a parameter

# class Daan:
#     def Trust():
#         print('sabko daan milega')

# Baba = Daan()
# Baba.Trust()                         #this wont work bcz Trust takes no argument ,as it has no argument already


      
    # def Trust(self):
        # print('sabko daan milega')

# Baba = Daan()
# Baba.Trust()                         #this wont work bcz Trust takes no argument ,as it has no argument already
#  or
# Daan.Trust(Baba)










# railway




class RailwayForm:
    formType = 'RailwayForm'
    def printData(self):
      print(f"NAME is {self.name}")
      print(f"Train is {self.train}")

    
firstApplication = RailwayForm()                   # Class
firstApplication.name = 'Rahul'                    # Variable 
firstApplication.train = 'Jodhpur Express' 
firstApplication.printData()                       # Function

#-----------------------------------------------------

#Hrjob:----------------------------------

class Employee:
    Company = "Persistent"
    Salary = "19000"
    def getSalary(self,comp):
      print(f"The salary of Employee working in {self.Company} is {self.Salary}\n {comp}")

    
    @staticmethod        #now , no need of self
    def Greet():
      print("Hey,\n wish you happy salary")


Rahul = Employee()
Rahul.Greet()
# print(Rahul.Greet())
Rahul.getSalary('Ok Noted')            # class defined

Rahul.Salary = 96000
Rahul.Company = "Nokia"
Rahul.getSalary('Ok Noted')            # instance defined


Rahul.Company = "Samsung"
Rahul.Salary = 56000
# print(Rahul.Company)                # Instance attribute
Rahul.getSalary("'Ok Noted'")            # Instance attribute
                    


Aditi = Employee()
Saee = Employee()


print(Aditi.Company)                # Class attribute
print(Aditi.Salary)                 # Class attribute
print(Saee.Company)                 # Class attribute
print(Saee.Salary)                  # Class attribute

#-----------------------------------------------------
#Instructor

class Auto:
   def __init__(self,name,salary,message) :
       print("Init function runs automatically doesnt require any call")
       self.name = name      
       self.salary = salary      
       self.message = message      
       print("Employee Created!")

   def getDetails(self):
     print(f"The name of the Employee is {self.name} ")
     print(f"The name of the Employee is {self.salary} ")
     print(f"The name of the Employee is {self.message} ")


a = Auto("rahul",2500,'thankyou sir!') 
print(a.name)
print(a.salary)
print(a.message)
# print(a)      


a.getDetails()





