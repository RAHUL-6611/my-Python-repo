
for i in range(1,21):
      i = input()
      with open(f"Tables/multiplication{i}.txt",'w') as m:
         for j in range(1,11):
            m.write(f"{i}X{j}={i*j} \n")
            if j!=10:
             m.write('\n')
      break