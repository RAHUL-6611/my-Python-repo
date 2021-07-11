from functools import reduce
# lambda is just a s shorthand for function
# def add(a,b):
#     s =a +b 
#     return s

add = lambda x,y:x+y
# print(add(3,2))

s1 = [1,4,6,7,4,3,8,56,4,3,5,67]
s2 = [1,4,6,7,4,3,8,56,4,3,5,67]

add2 = reduce(add,s1)                            # tally s1
# print(add2)

add3 = list(map(add, s1,s2))                     #used map to add list serial wise
print(add3)

a = [(1,2),(555,2),(8,2),(9,18)]
a1 = [(4,6),(3,7),(34,7),(2,4),(1,3),(64,68),(642,23),(35,1)]
a1.sort(key=lambda x:x[0])                       # sorted according to first element
a1.sort(key=lambda x:x[1])                       # sorted according to second element
print(a1)
# print(a.sort())


# b = [1,2,3,4,5,6,2,4,8,3,2]
# b.sort()
# print(b)