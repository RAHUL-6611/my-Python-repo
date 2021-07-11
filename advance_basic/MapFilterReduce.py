# map(function, inputs)
# map is used to

def cube(n):
    return n**3


def square(n):
    return n**2

def evenfinder(n):
    if n%2 == 0:
        return (str(n) +' is Even')    

h1 = [1,2,3,5,7]
h2 = {9,8,7,6,5,}

# cuber = tuple(map(cube, h1))
# print(cuber)

# squarer = list(map(square, h2))
# print(squarer)

# evens = set(map(evenfinder, h2))
# print(evens)

#-----------------------------------
# FILTER

# def idiot_number(i):
#     if i != 3 or i != 7 or i != 13 or i != 17 or i != 51:
#         return True
#     else:
#         return False  

def greater_than_2(n):
    if n<=2:
        return False
    else:
        return True


num = [1,2,3,4,45,7,8,9,8,6,4,-4,3,2,56,8,7,-5,3,-2]

filtering_num = list(filter(greater_than_2, num))
# print(filtering_num)

#----------------------------------------------------
# Reduce
from functools import reduce

def sum(a, b):
    return a+b

def mul(a, b):
    return a*b


data = [123,7,8,35,73,24,7,34,]
data1 = [123,7,8,35,73,24,7,34,]
final0 = reduce(sum,data)
final1 = reduce(mul,data)
print(final0)
print(final1)
