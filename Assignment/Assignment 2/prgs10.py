'''
    Find the reverse of a number
'''
print("\n\tREVERSE OF A NUMBER\n")

num = int(input("Enter a number : "))
tempNum = num
reverseNum = 0

while tempNum != 0:
    digit = int(tempNum % 10)
    tempNum = int(tempNum / 10)
    reverseNum = reverseNum * 10 + digit

print("\nReverse of {} is = {}".format(num, reverseNum))

'''
OUTPUT : 

    REVERSE OF A NUMBER

Enter a number : 5689

Reverse of 5689 is = 9865

'''