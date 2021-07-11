# super() means superclass ,that is using the old class which might be present in above code and using all its variables in your current method or class



class A1:

    cvar1 = "classA1"

    def __init__(self):
        self.instance = " init1"
        self.cvar1 = "init"
        
class A2(A1):

    cvar2 = "classA2"

    def __init__(self):
        super().__init__()
        self.instance = " init2"
        self.cvar2 = "init2"


class B(A1, A2):
    # super().__init__()    # you cannot call super without argument, first make a method and then call super in it
        
    def __init__(self):                           # init overridden in class b
        super().__init__()
        self.cv = "class B , init second"
        print(super().cvar1)         # finds into the class
        print(super().cvar2)         # finds into the class
        

# a = A1()
# print(a.cvar1)    # it finds cvar1 first in init and then in class 
# print(a.instance)    

# def B(self):
    # super().__init__()             # super can only be called in class

b = B()
print(b.cvar1)     # finds cvar1 in instance of class A
print(b.cvar2)     # finds cvar1 in instance of class A
    
