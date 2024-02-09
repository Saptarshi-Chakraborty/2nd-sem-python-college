# Write a program to find sum of all the digits present in a string.

inputString = input("Enter a string : ")

sum = 0

for i in range(len(inputString)) :
    
    if(inputString[i].isdigit()):
        sum += int(inputString[i])

print("\nThe sum is =", sum)

