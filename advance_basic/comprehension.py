#-----------------------------------------------------------------------------------------------------
from typing import Generator


list1 = [0,1,2,3,4,5,6,7,8,9]
list2 = [1,2,3,4,5,6,7,8,9,13,54,57,397,53,47,323,65,256,87]
list3 = [1,2,3,4,5,6,7,8,9,23,5,46,67,45,786,8,6,533,75,7,23,56,87,4,7,223,8,452,56664]

# print("Finding even numbers Using comprehension for list",[item for item in list1 if item%2 == 0 ])
# print("Mutliple of 3 Using comprehension for list",[item for item in list2 if item%3 == 0 ])
# print("Prime numbers Using comprehension for list",[item for item in list3 if item%2 == 1 and item != 1 or item == 2])

#-----------------------------------------------------------------------------------------------------
dict1 = {'a': 45, 'b': 12, 'A': 44, 'B':12, 'c':36}

# print({k.lower():dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})
# print({k.upper():dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})

# first we made a string named k which will take all lower case keys as lower and then add it to those SIMILAR upper case once and store it
#  as lower one
# and in the end k gets printed where dict1 is unchanged
# for eg. a and A are same then add those
#-----------------------------------------------------------------------------------------------------
# set1 = {x**2 for x in [1,2,3,4,5,6,7,7,7,8,10,9,9,9]}
# print(set1)

#first it will separate all dupilcates and then print squares of the originals 
#-----------------------------------------------------------------------------------------------------

# comprehension Generator
# gen1  = {i for i in range(50) if i%2 == 0}
# gen2  = [j for j in range(50) if j%(2*j +1)== 0]
# gen3  = (k for k in range(50) if k%10 ==5)

print({i for i in range(50) if i%2 == 0})
print([j for j in range(50) if j%3== 0 ])
print([k for k in range(50) if k/10 == 4])
