a = input("Enter a number : ")
b =  input("Enter a second number : ")

print(b < a)
sum = a + b            #this is correct
# avg = (a +b)/2         #but this is wrong before input is a string


a =int(a)
b =int(b)
avg = (a +b)/2

print(avg)         #now it is correct
#-------------------------------------
                        
c = input()
c =int(c)
square = (c*c)
print(square)