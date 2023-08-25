'''
    * * * *
    * * *
    * *
    *
'''


n =  int(input("How many lines you want to print: "))

for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()
