'''
    Find the roots of a Quadratic Equation
'''
import math

print("\n\tROOTS OF A QUADRATIC EQUATION\n")

a = int(input("Enter the coefficient of x^2 (a): "))
b = int(input("Enter the coefficient of x^1 (b): "))
c = int(input("Enter the coefficient of x^0 (c): "))

d = b**2 - 4*a*c

if d == 0:
    print("\n\tRoots are REAL & EQUAL\n")
    root = math.sqrt(abs(d))
    print("Root 1 =", round((-b + root) / (2 * a), 3))
    print("Root 2 =", round((-b - root) / (2 * a), 3))
elif d > 0:
    print("\n\tRoots are REAL & UNEQUAL\n")
    root = math.sqrt(abs(d))
    print("Root 1 =", round((-b + root) / (2 * a), 3))
    print("Root 2 =", round((-b - root) / (2 * a), 3))
elif d < 0:
    print("\n\tRoots are IMAGINARY & UNEQUAL\n")
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(d)) / (2 * a)
    print("Root 1 = {} + {}i".format(round(real_part, 3), round(imaginary_part, 3)))
    print("Root 2 = {} - {}i".format(round(real_part, 3), round(imaginary_part, 3)))

'''
OUTPUT 1 :
        
    ROOTS OF A QUADRATIC EQUATION

Enter the coefficient of x^2 (a): 4
Enter the coefficient of x^1 (b): 4
Enter the coefficient of x^0 (c): 1

    Roots are REAL & EQUAL

Root 1 = -0.5
Root 2 = -0.5
    
    
OUTPUT 2 :

    
    
OUTPUT 3 :





'''