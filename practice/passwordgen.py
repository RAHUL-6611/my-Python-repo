import string
import random
if __name__ == "__main__":
    s1 = string.ascii_letters
    s2 = string.ascii_lowercase
    s3 = string.ascii_uppercase
    s4= string.digits
    s5= string.punctuation
    
    # print(s1)
    # print(s2)
    # print(s3)
    # print(s4)
    # print(s5)

    Pwlen = int(input("Enter password length"))
    s = []

    # ------------------------------------------
    # y use extend instead of append,
    # extend to add elements as it is
    # whereas append will add the whole thing as one 
    # eg.
    # s.append(s1) 
    # s.extend(list(s1))                # to extend something in a list, array
    # print(s) 
    s.extend(list(s1))                # to extend something in a list, array
    s.extend(list(s2))                # to extend something in a list, array
    s.extend(list(s3))                # to extend something in a list, array
    s.extend(list(s4))                # to  extend something in a list, array
    s.extend(list(s5))                # to add or extend something in a list, array
    # print(s) 


    #method 1
    # random.shuffle(s)                # randomly shuffling the list to get a mixture of all for better password
    # print(s) 
    # print("".join(s[0:Pwlen]))
    
    #method 2
    print("".join(random.sample(s, Pwlen)))
    #End

    #learning join
    # print("".join("apple"))
    # print("".join("456"))

