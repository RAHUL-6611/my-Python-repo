# tell :  tells you the position where it stop reading 
# seek :  able to restart the reading from the position you input
# get : get(key, defaultvalue) if not present then runs defaultvalue

f = open('advanced python/files/a.txt')
print(f.tell())                                     # tells about the character position its on
print(f.readline())
f.seek(0)                                           # resets the position to zero
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
f.seek(14)
print(f.tell())
print(f.readline())

f.close()

dict1 = {1:"rahul", "2":"abhishek"}
print(dict1)
print(dict1.get(1,'nhihaiavailable'))
print(dict1.get(2,'nhihaiavailable'))