from os import write


try:
    open("advanced python\open.txt")
    # write("advanced python\open.txt")
except Exception as e:
    print(e)
    print("dekho bhai yeh nhi ho payega")    

# ---------------------------------------------3

try:
    file = open("text.txt", "r")
except EOFError as e:
    print("Sorry, no more content, EOF : end of file")
except IOError as e:
    print("Sorry, i need to again input and output file")
finally:
    print("thi will be printed irrespective of the exception, anyhow")

# ------------------------------------------------------------

try:
    print("I will try this code")
except Exception as e:    
    print("I will throw error")
else:    
    print("I will run if there is no excepttion, in case there is nothing to execute")
finally:    
    print("I will run anyhow")