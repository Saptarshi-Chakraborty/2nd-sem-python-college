'''
    5 4 3 2 1
    4 3 2 1
    3 2 1
    2 1
    1
'''


n =  int(input("How many lines you want to print: "))

for i in range(n):
    for j in range(n-i,0,-1):
        print(j, end=" ")
    print()
