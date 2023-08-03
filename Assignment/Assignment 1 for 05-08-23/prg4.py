'''
    AREA CALCULATION OF SQARE, RECTANGE, CIRCLE
'''
import math

again = "yes"

while again == "yes" or again == "YES":
    print("\n\t\t:: AREA CANCULATOR ::\n")
    print("Choose a option and enter corresponding number")
    print("1. Square", "\n2. Rectangle", "\n3. Circle")

    option = int(input(">> "))

    if option == 1:
        print("\nAREA OF SQUARE :")
        side = float(input("Enter length of one side : "))
        area = side * side
        print("\nArea of a square with length {} unit of one side is = {} sqr. unit".format(
            side, area))
    elif option == 2:
        print("\nAREA OF RECTANGLE :")
        length = float(input("Enter length : "))
        width = float(input("Enter width  : "))
        area = length * width
        print("\nArea of a rectangle with length {} unit & width {} unit is = {} sqr. unit".format(
            length, width, area))
    elif option == 3:
        print("\nAREA OF CIRCLE :")
        r = float(input("Enter radius : "))
        area = math.pi * r * r
        print("\nArea of a circle with radius {} unit is = {} sqr. unit".format(r, area))
    else:
        print("Enter a correct option")

    again = input(
        "\n\tWant to run again?\n\tEnter 'yes' to continue\n\tAnything other to exit\n>>")

print("\n\tTHANK YOU FOR USING THIS PROGRAM\n")

''' OUTPUT 1: 

            :: AREA CANCULATOR ::

Choose a option and enter corresponding number
1. Square   
2. Rectangle 
3. Circle    
>> 1

AREA OF SQUARE :
Enter length of one side : 23

Area of a square with length 23.0 unit of one side is = 529.0 sqr. unit

        Want to run again?
        Enter 'yes' to continue
        Anything other to exit
>>no

        THANK YOU FOR USING THIS PROGRAM

OUTPUT 2:
                    :: AREA CANCULATOR ::

Choose a option and enter corresponding number
1. Square 
2. Rectangle 
3. Circle
>> 2

AREA OF RECTANGLE :
Enter length : 3
Enter width  : 15

Area of a rectangle with length 3.0 unit & width 15.0 unit is = 45.0 sqr. unit

        Want to run again?
        Enter 'yes' to continue
        Anything other to exit
>>no

        THANK YOU FOR USING THIS PROGRAM

OUTPUT 3:
                :: AREA CANCULATOR ::

Choose a option and enter corresponding number
1. Square 
2. Rectangle 
3. Circle
>> 3

AREA OF CIRCLE :
Enter radius : 7

Area of a circle with radius 7.0 unit is = 153.93 sqr. unit

        Want to run again?    
        Enter 'yes' to continue
        Anything other to exit
>>q

        THANK YOU FOR USING THIS PROGRAM

'''
