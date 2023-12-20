import math

print("Please choose one of the following options:")
print("1. Square")
print("2. Rectangle")
print("3. Circle")
print("4. Triangle")

choice = input("Enter your choice: ")

if choice == "1":
    side = float(input("Please enter the length of the square's side: "))
    area = round(side ** 2, 3)
    perimeter = round(4 * side, 3)
    print("Area of the square: ", area)
    print("Perimeter of the square: ", perimeter)
elif choice == "2":
    width = float(input("Please enter the width of the rectangle: "))
    height = float(input("Please enter the height of the rectangle: "))
    area = round(width * height, 3)
    perimeter = round(2 * (width + height), 3)
    print("Area of the rectangle: ", area)
    print("Perimeter of the rectangle: ", perimeter)
elif choice == "3":
    radius = float(input("Please enter the radius of the circle: "))
    area = round(math.pi * (radius ** 2), 3)
    circumference = round(2 * math.pi * radius, 3)
    print("Area of the circle: ", area)
    print("Circumference of the circle: ", circumference)
elif choice == "4":
    base = float(input("Please enter the base of the triangle: "))
    height = float(input("Please enter the height of the triangle: "))
    area = round(0.5 * base * height, 3)
    print("Area of the triangle: ", area)
    print("To calculate the perimeter of the triangle, the length of all three sides is needed.")
else:
    print("The entered option is invalid.")
