'''
    Sum of all natural numbers upto n
'''
print("\n\tSUM OF ALL NATURAL NUMBERS UPTO N\n")
n = int(input("Enter the limit : "))

i = 1  # natural number starts from 1, without 0
sum = 0

print("Sum = ", end="")
while i <= n:
    print(i, end=" + ")
    sum += i
    i += 1

print("\b\b  ")
print("\nSum of first {} natural number is = {}".format(n, sum))
