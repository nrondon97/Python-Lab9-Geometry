# geometry.py
# Naylene Rondon
# 4/5/17
# calculations

import rectangle
import circle

#Constants
AREA_RECTANGLE_CHOICE = 1
PERIMETER_RACTANGLE_CHOICE = 2
AREA_CIRCLE_CHOICE = 3
CIRCUMFERENCE_CHOICE = 4
QUIT_CHOICE = 5

def main():
    choice = 0

    while choice!= QUIT_CHOICE:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Enter the width: "))
            length = float(input("Enter the length: "))
            print("The area is: ", rectangle.area(width, length))

        elif choice == PERIMETER_RACTANGLE_CHOICE:
            width = float(input("Enter the width: "))
            length = float(input("Enter the length: "))
            print("The perimeter is: ", rectangle.perimeter(width, length))

        elif choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Enter the radius: "))
            print("The area is: ", circle.area(radius))

        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("Enter the radius: "))
            print("The circumference is: ", circle.circumference(radius))

        elif choice == QUIT_CHOICE:
            print("Exiting the program.")

        else:
            print("Invalid")

def display_menu():
    print()
    print("   ~~~~~~~~Menu~~~~~~~~   ")
    print("(1) Area of a Rectangle")
    print("(2) Perimeter of a Rectangle")
    print("(3) Area of a Circle")
    print("(4) Circumference of a Circle")
    print("(5) Quit")

main()
