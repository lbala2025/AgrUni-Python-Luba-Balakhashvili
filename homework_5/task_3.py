from functools import reduce

products = [
    ("Keyboard", 49.99, 3),
    ("Mouse", 19.99, 0),
    ("Monitor", 159.99, 2),
    ("USB Cable", 4.99, 10),
    ("Headphones", 89.99, 1)
]

# 1
available_products = list(filter(lambda p: p[2] > 0, products))

print("Products available in stock:")
for p in available_products:
    print(p)

# 2
total_values = list(map(lambda p: (p[0], p[1] * p[2]), available_products))

print("\n Total value of each product:")
for t in total_values:
    print(t)


# 3
total_value = reduce(
    lambda acc, p: acc + p[1] * p[2],
    available_products,
    0
)

print("\n Total value of all available products:")
print(total_value)
