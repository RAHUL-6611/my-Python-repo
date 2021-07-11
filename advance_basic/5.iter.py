# Iterable  :  who will get iterated                        # string , list and all are iterable , int is not iterable
# Iterator  :  who will do the iterarion
# Iteration : the process


def gen(m):
    for i in range(m):
        yield i
        
print(gen(10e3))                # thousand element generated without using much of ram

# for i in gen(int(10e2)):                
    # print(i)                    # thousand printed


#--------------------------------------------------------------------------        
# now i am in need of few numbers, i will do
give_me_num = gen(12)      # 12 numbers
        
print(next(give_me_num))   # gives me num 0
print(next(give_me_num))   # gives me num 1
print(next(give_me_num))   # gives me num 2 and so on upto 11