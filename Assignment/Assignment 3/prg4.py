'''
    Sum of the series
    [ 1 + 1/!2 + 1/!3 + 1/!4 + .... + 1/!N]
'''

n = int(input("Enter the limit : "))

sum = 0

for i in range(1,n+1):
    fact = 1
    for j in range(1,i+1):
        fact *= j
    print("Fact of", i, "is =",fact)
    #print("1/
    sum += 1/fact

print("\nThe sum of the series is =",round(sum,3))
