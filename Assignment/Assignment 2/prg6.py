'''
    Largest among three numbers
'''

print("\n\tLARGEST AMONG THREE NUMBERS\n")

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if a == b:
    print("\n!!! first(", a, ")and second (", b, ") numbers are equal  !!!")
elif b == c:
    print("\n!!! second(", b, ")and third (", c, ") numbers are equal  !!!")
elif c == a:
    print("\n!!! first(", a, ")and third (", c, ") numbers are equal  !!!")
elif a > b and a > c:
    print("\n>>", a, "is the largest number <<")
elif b > a and b > c:
    print("\n>>", b, "is the largest number <<")
elif c > a and c > a:
    print("\n>>", c, "is the largest number <<")

'''
 OUTPUT : 

        LARGEST AMONG THREE NUMBERS

Enter first number : 25
Enter second number : 69
Enter third number : 36

>> 69 is the largest number <<

'''
