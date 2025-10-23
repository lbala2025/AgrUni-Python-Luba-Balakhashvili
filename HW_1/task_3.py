n = int(input("Enter a number between 1 and 100: "))

a = 0
b = 1

if 1 <= n <= 100:
    for i in range(n):
        print(a, end=" ")
        a_old = a
        a = b
        b = a_old + b

else:
    print("Number must be between 1 and 100")

