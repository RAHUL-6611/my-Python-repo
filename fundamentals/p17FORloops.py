for i in range(0, 8):  # not 8
    print(i)

for i in range(0, 8, 3):  # not 8 taking 3 step at a time
    print(i)

# -------------------------------------------------------
    # for and else (optional)

    for i in range(10):
        print(i)
    else:
        print("as soon as logic gets false else is outputted ")

# -------------------------------------------------------
     # Break

    for i in range(11):
        print(i)
        if i == 7:
         break
    else:
        print("break kiya kisine?")

# -------------------------------------------------------

   # continue

for i in range(11):       #less than 11
       if i == 5:         # 5 is skipped
        continue
       print(i)

# -------------------------------------------------------
    # pass   : is a null statement in py
r = 0
if r<10:
 pass
print("yo! pass boi")


#Tables time!-------------------------------------------------------
num = int(input("num : "))
for i in range(11):
    print(str(num) + "X" + str(i) + "=" + str(i*num) )


#-------------------------------------------------------
# ik=0 
# while(ik<=10):
#  print(f"{num}X{ik}={num*ik}")   #python f strings 
#  ik += 1


#-------------------------------------------------------

# li =["Harry","sohan","Sachin","Rahul","priya"]

# for name in li:
#     if name.startswith("S"):
#         print("Hello " + name)

#     if name.startswith("p"):
#         print("angel " + name)


#-------------------------------------------------------
# primius = int(input("num : "))
# prime = True

# for i in range(2, primius):
#  if (primius%i == 0):
#   prime = False
#   break

# #  else:                       #optional
# #   prime = True


# if (prime == True):
#          print("it is a prime number")

# else:
#          print("not a prime num")


#-------------------------------------------------------

# sumkanum = int(input(": "))

# for cum  in range(1):
#     print("sum : " + str(sumkanum*(sumkanum + 1)/2))
#-------------------------------------------------------
# k = 0
# while (k in sumkanum):
#     print("")

#-------------------------------------------------------

# fac = int(input(" : "))
# factorial = 1

# for i in range(1 ,fac + 1):
#     factorial = factorial * i
# print(f"The factorial of {fac} is {factorial}")


# #-------------------------------------------------------
# kio = int(input(": "))                   #only for kio = 0
# for i in range(kio + 1):
#     print("*" *(i+1))       #same as (i*1)
#     print(" *\n  *" *(i+1))
#     print("   *\n    *" *(i+1))
#     print("     *\n      *" *(i+1))
#     print("       *\n        *" *(i+1))
#     print("         *\n          *" *(i+1))
#     print("           *\n            *" *(i+1))
#     print("             *\n              *" *(i+1))
#     print("               *\n                *" *(i+1))
#     print("                 *\n                  *" *(i+1))
#     print("                   *\n                    *" *(i+1))
#     print("                     *\n                      *" *(i+1))
#     print("                       *\n                        *" *(i+1))

#-------------------------------------------------------
n= 9
for i in range(9):
    print( "   "* (n-i-1), end="")        #doesnt print new line
    print( "  *"* (2*i + 1), end="")      #doesnt print new line
    print( ""* (n-i-1))                   #prints new line ,the work is to print new line ,space doesnt matter
    # print("\n")                           #works with more space
#-------------------------------------------------------

print('''
            ***********
            **       **
            **        *
            **       **
            **      **
            ** * * ** 
            ** *
            **  *
            **   *
            **    *

                   
                             ''')
                
#-------------------------------------------------------
for i in range(3):
    if (i%2 == 0):
        print("**********")

    else :
        print("*        *")    

#-------------------------------------------------------
for i in range(10):
    if (i == 0):
        print("*************************************")

    elif (i == 9) :
        print("*************************************")

    else:
        print("*                                   *")        
                                                   
#-------------------------------------------------------
   
#-------------------------------------------------------
o = int(input(" : "))
i = 10
while  (i<=10 and i>=0 ):
 print( str(o) + " X " + str(i) + " = ",o*i)
 i-=1