# *args and **kwargs
# *vars and **kvars


# def function(name, age, rollno):
    # print("The name of the student is ", name, "who is ", age, " year old", " and roll no is ",rollno)

# def function(*args):
#     print("The name of the student is ", args[0], "who is ",args[1], " year old", " and roll no is ",args[2])
#     print(type(args)) 
#     print("By default args is a tuple and you can use args to define multiple variable easily")


# a = str(input("Enter name: "))
# b = int(input("Enter Rollno: "))
# c = int(input("Enter Age: "))

# def fun2(*argofrahuk):           # the name args is not compulsory
#     if (len(argofrahuk) == 3):
#         print("name: ", argofrahuk[0], ", Rollno: ", argofrahuk[1], ", Age: ", argofrahuk[2])    
#     else:
#         print("name: ", argofrahuk[0], ", Age: ", argofrahuk[2])    

# or you can also define a tuple/list
lis = ['ron', 26, 19]

# def printmarks(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#     print(type(kwargs))                  # by default dict

marklist = {"name: " : "frogi", "rollno: " : 26}

def combined(normal, *args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for i, j in kwargs:
        print(i, j)    

if (__name__ == "__main__"):
    # function("Rahul", 19, 26)
    # fun2(a, b, c)
    # fun2(*lis)
    # printmarks(**marklist)    
    combined("tum siddhe ho", lis, marklist)
