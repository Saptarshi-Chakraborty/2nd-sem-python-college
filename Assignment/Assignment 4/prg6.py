'''
    Armstrong number
'''

num =  int(input("Enter a number : "))
temp = num

length = len(str(num))
sum = 0

while( num != 0):
    r = num % 10
    sum = sum + (r**length)
    num = num // 10

if(sum == temp):
    print(temp, "is a Armstrong Number")
else:
    print(temp, "is Not a Armstrong Number")


