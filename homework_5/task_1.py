import random
import math

def my_func(n):
    counter = 0

    for i in range(n):
        a = random.random()  
        b = random.random() 

        if math.sqrt(a**2 + b**2) <= 1:
            counter += 1

    result = 4 * counter / n
    print(f"n = {n}, result = {result}")
    return result

my_func(10)
my_func(1000)
my_func(100000)
my_func(10000000)

# ფუნქცია ითვლის π-ს მნიშვნელობას.
# a და b არის შემთხვევითი რიცხვები 0 და 1 შორის, რომლებიც წარმოადგენენ ერთეულიანი კვადრატის შიდა წერტილებს. 
# თუ წერტილი მდებარეობს ერთეულიანი წრის შიგნით (ან მის ზღვარზე), მაშინ counter-ის მნიშვნელობა იზრდება. 
# π-ს მნიშვნელობა კი გამოითვლება ფორმულით 4 * counter / n, სადაც n არის გენერირებული წერტილების რაოდენობა, 
# შესაბამისად რაც უფრო იზრდება n-ის მნიშვნელობა, მით უფრო ზუსტია შედეგი.
