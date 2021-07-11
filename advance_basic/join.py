l = ['mein', 'tum', 'voh']

for item in l:
    if item is not l[2]:                    # if using pycharm, directly write 'voh' instead of l[2] 
        print(item, "aur ",end="")
    else:
        print(item)    
# print(" aur ".join(l))