'''
      *
     * *
    * * *

'''


n =  int(input("How many lines you want to print: "))

for i in range(n):
    #space control loop
    for j in range(n-i):
        print(end=" ")
    
    for j in range(i+1):
        print("*", end=" ")
    print()
