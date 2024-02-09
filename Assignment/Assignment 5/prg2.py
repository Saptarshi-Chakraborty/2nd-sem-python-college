# Write a program to replace all the vowels in a string by *

inputString = input("Enter a string : ")

for i in range(len(inputString)) :
    
    if(inputString[i].lower() in {'a','e','i','o','u'}):
        inputString = inputString.replace(inputString[i], '*')

print("\nThe final string :",inputString)
