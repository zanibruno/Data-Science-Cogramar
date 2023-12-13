# ask user for dimensions of the triangle
print("You will be asked to enter dimensions of triangle")
side1 = float(input("Please enter the dimension of the first side: "))
side2 = float(input("Please enter the dimension of second side: "))
side3 = float(input("Please enter dimension of third side: "))

# calculate semi-perimeter of triangle
s = (side1 + side2 + side3)/2

#calculate area of triangle
area = (s*(s-side1)*(s-side2)*(s-side3)) ** 0.5
# print out area of triangle
print(f"the aread of the triangle is {area}")
