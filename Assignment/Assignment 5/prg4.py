# Write a program to check if a string is pallindrome or not

inputString = input("Enter a string : ")

output = inputString[::-1]

if(inputString == output):
    print("\n >> This is a Pallindrome String <<")
else:
    print("\n >> This is Not a Pallindrome String <<")
