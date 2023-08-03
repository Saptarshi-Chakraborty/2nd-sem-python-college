'''
    EVEN NUMBER CHECKER BETWEEN A RANGE
'''

print("\n\tEVEN NUMBER CHECKER BETWEEN A RANGE\n")

low = int(input("Enter lower value for the range : "))
high = int(input("Enter higher value for the range : "))

print("\nEven numbers between {} and {} are: ".format(low, high))
while high >= low:
    if low % 2 == 0:
        print(low, end=", ")
    low += 1

print("\b\b  ")


''' OUTPUT : 

        EVEN NUMBER CHECKER BETWEEN A RANGE

Enter lower value for the range : 1
Enter higher value for the range : 15

Even numbers between 1 and 35 are:
2, 4, 6, 8, 10, 12, 14

'''
