import random

def game(comp, you):


 if (comp == 's'):
     if(you == 'w'):
         return False
     elif(you == 'g'):
         return True

 elif (comp == 'g'):
       if(you == 'w'):
         return True
       elif(you == 's'):
         return False
 elif (comp == 'w'):
        if(you == 's'):
         return True
        elif(you == 'g'):
         return False                 

 elif (comp == User):
        return None

print("comp : Snake(s) or Water(w) or Gun(g) ?")
radom = random.randint(1,3)
if radom == 1:
     comp = 's'
elif radom == 2:
     comp = 'w'
elif radom == 3:
     comp = 'g'
                
    
User = input("User: Snake(s) or Water(w) or Gun(g) ?")
a = game(comp,User)
    #-------------------------------------------------------
print(f" comp chose {comp}")
print(f"you chose {User}")


if(a == None):
    print("Tie")
elif(a):
    print("You win")
else:
    print("You Lose \n ,comp Win")        
