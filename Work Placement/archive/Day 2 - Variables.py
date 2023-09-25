Age = 18 #int
Height = 5.10 #float
Com = 10j # complex

Base = int(input("What is the base of the triangle? "))
Height = float(input("What is the height of the triangle? "))
area = 0.5 * Base * Height #Base and height gathered from user input will then be multiplied, this is why the inputs either require integers or decimal numbers.
print("The area of the triangle is:", area)

Side_a = int(input("Enter side a: "))
Side_b = int(input("Enter side b: "))
Side_c = int(input("Enter side c: "))
perimeter = Side_a + Side_b + Side_c
print("The perimeter is:", perimeter)

length1 = int(input("Length of rectangle: "))
width1 = int(input("width of rectangle: "))
area1 = length1 * width1
perimeter1 = 2 * length1 * width1
print(area1, perimeter1)



