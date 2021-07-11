# SETS - no repeated items,immutable,
# cannot add list in set ,bcz  list i changeable and set isnt, can add tuple

ask = {1,2,3,4,5,1}               

print(ask)                   #ignores extra 1
print(type(ask))             #set

#---------------------------------------
asp = set()                           #empty ask = {} is not a set its a dict
print(type(asp))


asp.add(5)
asp.add(5)                            #ignores duplicates
asp.add(6)
asp.add(7)
asp.add(8)
# asp.add([1,2,3,4,5]) or {1,2,3,4,5}                   #cannot add mutable things like LIST, DICT
asp.add((1,2,3,4,5))                  #can add a tuple

print(asp)

#----------------------------------------------
# methods

print(len(asp))

#asp.remove(5)
print(asp)

print(asp.pop())     #prints  a random element out ,it takes no argument

# asp.clear()         #to cleanshave your set

asp.union({2,4,6,8,10})
print(asp)
asp.intersection({5,6,8})
print(asp)

#differnet things
# ----------------------------------------------
sets = {1,1.1,0.e1,"1"}
print(sets)

#=------------------------------------------
# myDict = {
#   "Maut":"death", 
#   "Kitaab":"book",
#   "Chaabi":"key",
#   "Hisaab":"calculation", 
#   "Nadi":"river",
#   "Gaadi":"vehicle", 
#   "Jute":"shoes"
    
# }

# print("your options are :", myDict.keys())
# k = input("enter your word : \n ")

# # print("translation is ",Translationsss[ak])
# print("your translation for this word is : ",myDict.get(k))


#------print all unique numbers------------------------------
# myset = {}
# myset = set()

# myset.add(int(input("1.")))
# myset.add(int(input("2.")))
# myset.add(int(input("3.")))
# myset.add(int(input("4.")))
# myset.add(int(input("5.")))
# myset.add(int(input("6.")))
# myset.add(int(input("7.")))
# myset.add(int(input("8.")))


# print(myset)

#----------------------------------------------------------
d = set()
d.add(20)
d.add("20")
d.add(20.0)

print(len(d))   #answer is 2 bcz int 2 and float 2 has same value 2

#---------------------------------------------------------------

lang = {}

aa = input("1. ")
bb = input("2. ")
cc = input("3. ")
dd = input("4. ")
ee = input("5. ")

lang["rahul"] = aa
lang["sonali "] = bb
lang["saee"] = cc
lang["prajakta"] = dd
lang["baishonavi"] = ee

print(lang)

#values can be duplicate but keys has to be unique
# ------------------------------

