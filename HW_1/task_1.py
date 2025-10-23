def is_triangle(s1, s2, s3):
    return s1+s2>=s3 and s1+s3>=s2 and s2+s3>=s1

a = float(input("Please enter first side of triangle: "))
b = float(input("Please enter second side of triangle: "))
c = float(input("Please enter third side of triangle: "))

if a>0 and b>0 and c>0 and is_triangle(a, b, c):
    perimeter = a+b+c
    s = perimeter/2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    print("The perimeter of triangle is ", perimeter)
    print("The area of triangle is ", area)
else:
    print("Triangle with this sides can not exist")


