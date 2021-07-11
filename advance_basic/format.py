'''
format function
'''
users = ['rohan','shubham','sneha']

comp1 = ['raspberry pi', 'andriod', 'iphone']
comp2 = ['andriod', 'iphone','raspberry pi']

#noob
# for i in range(0, len(users)):
#     print ("computer used by ", users[i], " is ", comp[i])
    
#pro        
for i in range(0, len(users)):    
    template1 = "Computer used by {0} is {1}"
    template2 = "Computer used by {0} is {2}"
    # print(template1.format(users[i], comp1[i]))    
    print(template2.format(users[i], comp1[i], comp2[i]))    