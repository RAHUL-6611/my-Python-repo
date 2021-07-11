import os
# Types of files : (1. .txt, .c )                     RAM is volatile , HDD is non volatile 
                 # (2. .jpg .png)


#   r - read for reading
#   w - open for writing
#   a - open for appending
#   + - open for updating


# 'rb' - open for read in binary mode
# 'rt' - open for read in text mode ( t is by default)




# f = open("sample.txt","r")     # 'r' - READ MODE (by default)
# f = open("sample.txt")           # no need to write 'r'  
# data = f.read()                  # 'open' is a built in function
# # data =  f.read(4)              # reads only 4 character
# print(data)
# f.close()


#------------------------------------------------
# Readline
# f = open("sample.txt")
# data = f.readline()              # reads 1 line     
# # data = f.readlines()             # reads all line , spaces, new line gaps
# print(data)
# f.close()


# write---------------------------------------------------------
# g = open("samples.txt", 'w')                      # auto creates files
# data = g.write(' ok   tata bye bye') 
# data = g.write(' ok   tata bye bye')              # auto writes new line   
# data = g.write(' ok   tata bye bye') 
# data = g.write(' ok   tata bye bye')              # 4 times
# print(data)
# g.close()


#append-----------------------------------------------
# h = open("samples.txt", 'a')                      # auto creates files
# data = h.write(" \n hmhmmmmmhmmmmmmmhmmmmmmmhmmmmmmmhmmmmmmmmhmmmmhhhhhhhmhhmh")        # auto writes new line   
# print(data)
# h.close()

#-------------------------------------------------------
# with and as:

# with open("sampless.txt", 'r') as j :    #'w'
#     # j.write("ok automatic stuff")
#  k=j.read()
#  print(k)                               #  no need of closing statement, its automated


#----------------------------------------------
#problem set


# l = open('poem.txt')
# z = l.read()

# if 'twinkle' in z:
#     print("twinkle is present")
# else:
#     print("Not present")    

# l.close()

#-----------------------------------------------------

# game score

# def game():
#     return 20

# score =  game()

# with open("game.txt") as highestscore:
#     hiscore = highestscore.read() 

   
# if  hiscore =='':
#     print('1st record')
#     with open("game.txt",'w') as highestscore:
#      highestscore.write(str(score))

# elif int(hiscore)<score:
#     print('new record')
#     with open("game.txt",'w') as highestscore:
#      highestscore.write(str(score))
 
 #-------------------------------------

#finding inside log

finder = True
i = 1

with open('log.txt') as o:
    while finder:
       finder = o.readline()

       if 'python'  in finder.lower():
        print("YES")
        print(finder)
        print(f" python is present on line {i}")
       i+=1

#------------------------------------

# copy pasting

# with open("this.txt") as d:
#     copy = d.read()

# with open("copied.txt", 'w') as d:
#     paste = d.write(copy)
#     print('copied and pasted succesfully')


#-----------------------------------

#Renaming file : instead deleting file(using os) and creating new with same data


# file1 = 'rename1.txt'
# file2 = 'rename2.txt'

# with open(file1) as a1:
#     rename = a1.read()

# with open(file2, 'w') as a2:
#     rename2 = a2.write(rename)

# os.remove(file1)    


#--------------------------------