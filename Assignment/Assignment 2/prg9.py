'''
    Sum of all even numbers upto N
'''

print("\n\tSUM OF ALL EVEN NUMBERS UPTO N\n")
n = int(input("Enter the limit : "))

i = 1  # natural number starts from 1, without 0
sum = 0

print("S = ", end="")
while i <= n:
    if i % 2 == 0:
        print(i, end=" + ")
        sum += i
    i += 1

print("\b\b  ")
print("\nSum of all even number upto ", n, " is = ", sum)

'''
OUTPUT :
       
         SUM OF ALL EVEN NUMBERS UPTO N

Enter the limit : 12
S = 2 + 4 + 6 + 8 + 10 + 12   

Sum of all even number upto  12  is =  42



'''
