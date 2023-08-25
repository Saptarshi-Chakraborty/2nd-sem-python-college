# Fibonacci Series upto N terms

n = int(input("Enter the number of terms : "))

a = 0
b = 1

print("\nThe Fibonacci series of", n,"terms is = 0 , 1 , ",end='')
for i in range(n-2):
    c = a + b
    a = b
    b = c
    print(c,end=' , ')

print("\b\b  ")
    
