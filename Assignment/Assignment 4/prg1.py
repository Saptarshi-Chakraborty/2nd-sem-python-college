n =  int(input("How many lines you want to print: "))

for i in range(n):
    #print(i)
    for j in range(i+1):
        print("*", end=" ")
    print()
