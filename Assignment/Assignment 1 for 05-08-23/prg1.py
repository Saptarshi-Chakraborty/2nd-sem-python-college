'''
    SIMPLE INTEREST CALCULATOR
         p * r * t / 100
'''
print("\n\tSIMPLE INTERST CALCULATOR\n")

p = int(input("Enter principle amount : "))
r = float(input("Enter rate of interest : "))
t = float(input("Enter time (in year)   : "))

interest = p * r * t / 100

print("\nThe Interest will be = Rs.", interest)
print("The Total Amount will be = Rs.", interest + p)


''' OUTPUT : 

        SIMPLE INTERST CALCULATOR

Enter principle amount : 100
Enter rate of interest : 2.5
Enter time (in year)   : 3.6

The Interest will be = Rs. 9.0
The Total Amount will be = Rs. 109.0

'''
