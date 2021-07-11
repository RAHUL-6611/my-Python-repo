import time

initial = float(time.time())
print(initial)

for i in range(15):
    print("rahul")
    time.sleep(1)
print("for loop", time.time() - initial)

initial2 = float(time.time())
k = 0
while k < 15:
    print("rahul")
    time.sleep(1)
    k += 1
print("while loop : ", float(time.time() - initial2))

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)