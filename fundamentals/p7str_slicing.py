my_name = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(my_name[17])
print(my_name[0])
print(my_name[7])
print(my_name[20])
print(my_name[11])

name = "my name is RAHUL "
print(name[:2])
print(name[3:7])
print(name[8:10])
print(name[11:])                 #from 1 to 16 

reverse = "malamaalaamalam"      #counting from behind
print(reverse[-8:])              #negative starts from -1
print(reverse[-15:-7])
print(reverse[-1])
print(reverse[-15])
print(reverse[-2])
print(reverse[-14])
print(reverse[-3])
print(reverse[-13])
print(reverse[-3])
print(reverse[-12])
print(reverse[-4])
print(reverse[-11])
print(reverse[-5])
print(reverse[-10])
print(reverse[-6])
print(reverse[-9])
print(reverse[-7])


# slicing with skip values
# l = "lakhwa"
# #print(l[0:3:1])  #printing all values from 0-2
# print(l[0::2])                      #printing from 0-3 (3 not included) and skiping every 2nd position(or skiping one element) ..
# print(l[0::3])                      #printing from 0-end  and skiping every 2nd and 3rd position (or skipping two elements) ..    


# #----------------------------------------------------------------
# # STRING FUNCTON

# #1. len()
# print(len(l))                # length 

# #2. .endswith(" ")
# print(l.endswith("a"))       # true or false

# #3. count
# print(l.count("a"))          # "a" occurs twice
 
# #4. capitalise  
# print(l.capitalize())        # capitlise 1st letter

# #5. find
# print(l.find("a"))           #binary positions eg a is in 1st position

# #6. replace
# print(l.replace("l","m"))   #replaces letters and words

#---------------------------------------------------------------------

# sequence characters

#  1. \n new line
#  2. \t space or tab
#  3. \' sinfle quote
#  4. \" double quote
#  5. \\ backslash


#---------------------------------------------------------------------
  # practice set

#1.
# i = input("enter your name : ")
# print(i + " Sir, Good Morning  ")
# print(" how can i help you " + " ? ")


#2.
# e1 = input(" name :  ")
# e2 = input(" ")
# print(" \n\n Dear " + e1 +", " " \n you are selected ! \n " + e2)


#3.
o = " chipchipak ching ching  ,hello  honey  bunny"
print("3rd exercise")
print(o.find("  "))
print(o.replace("  "," "))

#4.


