# #Sample

# def percent(marks):

#    p = (((sum(marks))/600)*100)
#    return p

#     #1.Rahul
# m1 = int(input("Rahul \n: "))
# m2 = int(input(": "))
# m3 = int(input(": "))
# m4 = int(input(": "))
# m5 = int(input(": "))
# m6 = int(input(": "))

# Mark1 = [m1,m2,m3,m4,m5,m6]
# Percentage1 = (percent(Mark1))


#     #2.Preeti
# m01 = int(input("Preeti \n: "))
# m02 = int(input(": "))
# m03 =int(input(": "))
# m04 = int(input(": "))
# m05 = int(input(": "))
# m06 = int(input(": "))

# Mark2 = [m01,m02,m03,m04,m05,m06]
# Percentage2 =(percent(Mark2))

# print(Percentage1,Percentage2)

# -----------------------------------------------------
# Greeting card

# def Greet(name= 'Bhartiya'):
#     print("WELCOME, " + name)

# Greet()                       #const
# Greet("Rahul")                #system defined
# Greet(input(""))              #user defined

# ------------------------------------------------------------

# Recursive :
# simple
# n = int(input(""))

# Fac = 1

# for i in range(n):
#         Fac = Fac * (i + 1)
# print(Fac)

# -----------------------------------------
# #with function
# def Fac(n):
#     Faci = 1
#     for i in range(n):
#         Faci = Faci * (i + 1)
#     print(Faci)
#     # return Faci

# Fac(n)
# ---------------------------------------------
# #with Recursion

# def recursion(q):
#     if q ==1 or q == 0:
#         return 1
#     return q * recursion(q-1)


# f = recursion(int(input("")))
# print(f)
# --------------------------------------------------

# Greatest of 3:

# def greatest(n1, n2, n3):

#    if(n1 > n2):
#        if(n1 > n3):
#            print("Greatest :", n1)
#        else:
#            print("Greatest :", n3)

#    else:
#          if(n2 > n3):
#            print("Greatest :", n2)
#          else:
#            print("Greatest :", n3)

# n1 = int(input(""))
# n2 = int(input(""))
# n3 = int(input(""))

# greatest(n1,n2,n3)

# -----------------------------------------------

#sum of n natural numbers

# def sums(d):             #works till 998 
#     if d <= 1:
#         return 1
#     else:

#         return d + sums(d-1)

# h= sums(int(input()))
# print(h)


#----------------------------------------
# inch to cm
def conv(inch):
    if (inch == 1):
        return 2.54
    else:
        return inch*2.54    

i = conv(int(input("inches: ")))
print(i,"cm")

#------------------------------------------
