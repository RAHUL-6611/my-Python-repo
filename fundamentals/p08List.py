# LIST AND ITS FEATURES

#you can update a list , mutable
#------------------------------------
x = [1,2,3,4,5,6,7,8,99,0]

print(x)
print(x[8])

#------------------------------------
# 1.replace items
x[9] = 23
print(x)

#------------------------------------
# 2.list of diff items
y = [ 0, 0.9 ,True, "okay", 'l',10e4567]
print(y)

#------------------------------------
#3. slicing
print(y[0:4])
print(y[-4:])
#------------------------------------

#4. sorting, reversed
z = [1,9,5,3,7,6,2,4,8,0]
print(z)

z.sort()                 #sorted
print((z)) 

z.reverse()             
print((z))               #reversed
#------------------------------------

#5. append
q = [12,34,56,78,90]

q.append(91)
print(q)
#------------------------------------

#6. insert
r = [62,24,56,2,87,3,8]
r.insert(3,999)                #inserting 999  at 4th position between 3rd and initial 4th
print(r)

#7. pop and remove
r.pop(2)                       # removes element at index 2
r.pop()                        # removes last element           
print(r)                       

r.remove(999)                  #removes 999
#r.remove()                     #removes everything causing eror
print(r)

#------------------------------------

#------------------------------------

#------------------------------------
#exercise

# f1 = input(" enter fruit name : ")
# f2 = input(" enter fruit name : ")
# f3 = input(" enter fruit name : ")
# f4 = input(" enter fruit name : ")
# f5 = input(" enter fruit name : ")
# f6 = input(" enter fruit name : ")
# f7 = input(" enter fruit name : ")

# #also sorted them in alpahabetical manner
# fruits = [ f1,f2,f3,f4,f5,f6,f7]
# fruits.sort()
# print(fruits)
# #------------------------------------

yo = [2,45,6,3,45,44,2,90]

print(yo[1]+ yo[0]+ yo[1]+ yo[2]+ yo[4]+ yo[5])
#or
print(sum(yo))

print(yo.count(45))


#------------------------------------









#------------------------------------






#------------------------------------







#------------------------------------












#------------------------------------













#------------------------------------










#------------------------------------








 