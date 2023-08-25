# Find the sum of all even numbers upto 100

# print("\n\tSUM OF FIRST 100 EVEN NUMBERS\n")
sum = 0
# print("Sum = ",end="")

for i in range(1, 101):
    if int(i%2) == 0:
        # print(i,end=" + ")
        sum += i
print("\b\b")
      
print("\nSum of first 100 even number is =",sum)
