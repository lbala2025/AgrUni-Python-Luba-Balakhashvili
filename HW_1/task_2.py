number = int(input("Enter a number between 1 and 1000: "))

if 1 <= number <= 1000:
    for i in range(1,number+1):
        if number % i == 0:
            print(i, end=" ")
else:
    print("Number must be between 1 and 1000.")