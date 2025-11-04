def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


year = input("Enter an Integer for year: ")
while year.isdigit()==False or int(year) <= 0:
    year = input("Input INVALID. Please enter a valid year: ")

year = int(year)
if is_leap(year): print(f"{year} is a leap year")
else: print(f"{year} is not a leap year")

