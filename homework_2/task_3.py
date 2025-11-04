import random

list = []
for i in range(5):
    rand_num = random.randint(1,4)
    list.append(rand_num)

new_list = []
for num in list:
    for j in range(num):
        new_list.append(num)

print(f"List - {new_list}")
print(f"Length - {len(new_list)}")

