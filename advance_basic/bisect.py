import bisect


num1 = 5
num2 = 10

a = [1,2,3,4,6,7,8,9,11]

# print(bisect.bisect(a, num1))       # tell the comp where on which index should it put the num
bisect.insort(a,num1)               # insort actually innsert the num there ,while the list is sorted  
print(a)

