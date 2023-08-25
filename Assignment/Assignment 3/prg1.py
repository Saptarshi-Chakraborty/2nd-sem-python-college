'''
 Sum of N natural Number with for Loop
'''

n = int(input("Enter the limit : "))
sum = 0

print("Sum = ",end="")
for i in range(1, n + 1):
    print(i,end=" + ")
    sum += i
print("\b\b  ")
      
print("\nSum of first", n, "natural number is =",sum)
