employees = [
    {"name": "Alice",   "tasks": [5, 7, 9],   "department": "IT"},
    {"name": "Bob",     "tasks": [2, 3, 4],   "department": "Sales"},
    {"name": "Charlie", "tasks": [8, 7, 6],   "department": "IT"},
    {"name": "Diana",   "tasks": [9, 8, 10],  "department": "Marketing"},
    {"name": "George",  "tasks": [2, 7, 6],   "department": "IT"}
]

# 1
avg_list = list(map(
    lambda emp: {
        "name": emp["name"],
        "department": emp["department"],
        "average_tasks": sum(emp["tasks"]) / len(emp["tasks"])
    },
    employees
))

print("List with Average Tasks:")
for x in avg_list:
    print(x)


# 2
sorted_list = sorted(
    avg_list,
    key=lambda x: x["average_tasks"],
    reverse=True
)

print("\n List Sorted by average_tasks:")
for x in sorted_list:
    print(x)


# 3
max_avg_tasks = max(avg_list, key=lambda x: x["average_tasks"])

print("\n Employee with max average tasks:")
print(max_avg_tasks)

# 4
more_than_six = list(filter(
    lambda x: x["department"] == "IT" and x["average_tasks"] > 6,
    avg_list
))

print("\n Employees with avg tasks more than 6:")
for x in more_than_six:
    print(x)

