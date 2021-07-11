# Dict is always unordered ,mutable,indexed,duplicates not allowed,object is not callable

bigdict = {
    "name" : " rahul ",
    "number" : 7757936611,
    "job" : {'software engineer' : " deeshaw mnc "},
    "marks": [0,0,0],
    # "marks" :[0]   duplicats not allowed
    1:2
}

print(bigdict['number'])
print(bigdict["job"]["software engineer"])

#-----------------------------------------------------
#muttable
bigdict['marks'] = [98,96,97,100]

print(bigdict['marks'])

#--------------------------
print(bigdict.keys())     # keys are the mains which saves values
print(bigdict.values())   # the values
print(bigdict.items())    #both combined


print(type(bigdict))

print(list(bigdict.keys()))  # conversion into list
print(list(bigdict.values ()))
print(list(bigdict.items()))
#-------------------------

#adding some changes or more keys

smallupdate = {
    "lovish" : "friend",
    "name" : "Parmar Rahul"     #old value changed
}

bigdict.update(smallupdate)  #adding more changes
print(bigdict)

print(bigdict.get("name"))
#or
print(bigdict["name"])

#------------------------------------------------

#--------------------------------------------------------------
# exercise

#1. hindi to english translation app




