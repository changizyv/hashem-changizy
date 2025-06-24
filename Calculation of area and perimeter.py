import math

print("Please choose one of the following options:")
print("1. Square")
print("2. Rectangle")
print("3. Circle")
print("4. Triangle")

try:
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        side = float(input("Please enter the length of the square's side: "))
        if side <= 0:
            print("Side must be positive!")
        else:
            area = round(side ** 2, 3)
            perimeter = round(4 * side, 3)
            print("Area of the square: ", area)
            print("Perimeter of the square: ", perimeter)
    elif choice == "2":
        width = float(input("Please enter the width of the rectangle: "))
        height = float(input("Please enter the height of the rectangle: "))
        if width <= 0 or height <= 0:
            print("Width and height must be positive!")
        else:
            area = round(width * height, 3)
            perimeter = round(2 * (width + height), 3)
            print("Area of the rectangle: ", area)
            print("Perimeter of the rectangle: ", perimeter)
    elif choice == "3":
        radius = float(input("Please enter the radius of the circle: "))
        if radius <= 0:
            print("Radius must be positive!")
        else:
            area = round(math.pi * (radius ** 2), 3)
            perimeter = round(2 * math.pi * radius, 3)
            print("Area of the circle: ", area)
            print("Perimeter of the circle: ", perimeter)
    elif choice == "4":
        base = float(input("Please enter the base of the triangle: "))
        height = float(input("Please enter the height of the triangle: "))
        if base <= 0 or height <= 0:
            print("Base and height must be positive!")
        else:
            area = round(0.5 * base * height, 3)
            print("Area of the triangle: ", area)
            side1 = float(input("Please enter the length of the first side: "))
            side2 = float(input("Please enter the length of the second side: "))
            side3 = float(input("Please enter the length of the third side: "))
            if side1 <= 0 or side2 <= 0 or side3 <= 0 or (side1 + side2 <= side3) or (side2 + side3 <= side1) or (side1 + side3 <= side2):
                print("Invalid triangle sides!")
            else:
                perimeter = round(side1 + side2 + side3, 3)
                print("Perimeter of the triangle: ", perimeter)
    else:
        print("The entered option is invalid.")
except ValueError:
    print("Please enter a valid number!")
