# Write a Program to count the number of times a character appears in a string without using built in function.

inputString = input("Enter a string : ")
inputChar = input("Enter a character you want to count: ")
count = 0

for char in inputString:
    if char == inputChar:
        count += 1

print("\n >> The character '", inputChar, "' appears", count, "times in the string", inputString, "' <<")
