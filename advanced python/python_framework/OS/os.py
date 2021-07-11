import os

#1 know what all you can do
# print(dir(os))

#2 gives you file location/directory
# print(os.getcwd())

#3 current working directory change
# os.chdir("C://")
# print(os.getcwd())

#4 
# f = open("advanced python/files/a.txt")
# print(os.getcwd())

#4
# print(os.listdir())
# print(os.listdir("C://"))    // it's a list , you can insert, delete, traverse as it is

#5
# os.mkdir("advanced python/httpserver/a.html")
# os.makedirs("main/tum/vo")
print(os.getcwd())

#6
# os.rename("advanced python/httpserver/a.html", "advanced python/httpserver/b.html")
# os.remove("advanced python/httpserver/b.html")

#7 get all environment variables
# print(os.environ.get('path'))

#8 why use this to join name of a directory,  bcz it helps to cancel out extra '/' which may cause problem if you do in usual way
print(os.path.join("C://","a.txt"))

#9 to check if a path exits, is it a file or directory or link or is it a absolute path or not, is it a mount or not
print(os.path.exists("C://"))
print(os.path.isfile("advanced python\OS\os.py"))
print(os.path.isdir("advanced python\OS\os.py"))
print(os.path.isabs("advanced python\OS\os.py"))
print(os.path.islink("advanced python\OS\os.py"))
print(os.path.ismount("advanced python\OS\os.py"))
print(os.path.ismount("C://"))

