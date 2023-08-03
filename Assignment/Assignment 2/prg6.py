'''
    Sum of all even numbers upto 1000
'''

print("\n\tSUM OF ALL NATURAL NUMBERS UPTO N\n")

i = 1  # natural number starts from 1, without 0
sum = 0

while i <= 1000:
    if i % 2 == 0:
        sum += i
    i += 1

print("\nSum of all even number upto 1000 is = {}".format(sum))
