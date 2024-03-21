import math
# 1.2 part B

# calaculates Fahrenheit into celsius
print("\nThis program calculates Fahrenheit into celsius.")

# conversion rate found online https://www.datainsightonline.com/post/fahrenheit-to-celsius-converter
fahrenheit = float(input(" Enter temprature in Fahrenheit : "))

# user inputs number
# equation for celsius
celsius = (5 / 9 * (fahrenheit - 32))
print(" Temperature in Celsius is :", celsius)


# 1.3 part C
# This calculates the formula for the area of a trapezoid
print(" \nThis calculates the area of a trapezoid")
height = float(input("Enter the height of the trapezoid : "))
bottom = float(input("Enter the length of the bottom base of the trapezoid : "))
top = float(input("Enter the length  of the top base of the trapezoid : "))

# Trapezoid formula
area= 0.5 * (bottom + top) * height
print("Area of a traperzoid is :", area)


# Calculate The volume of a sphere
print("\nThis calculates the volume of a sphere")
radius = float(input("Enter the radius of the Sphere: "))

# user inputs radius
# math Library, print value of pi
volume = (4 * math.pi * radius ** 3) / 3

# radius is raised to the power of 3
print("The volume of a sphere is : ", volume)