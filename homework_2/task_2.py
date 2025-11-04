subjects = {
'math': {'George': 85, 'Salome': 78, 'David': 92},
'physics': {'George': 90, 'David': 75, 'Salome': 88},
'chemistry': {'David': 82, 'George': 80, 'Salome': 91}
}

#Output: {'George': {'math': 85, 'physics': 90, 'chemistry': 80}, ...}

students = {}

for subject, scores in subjects.items():
    for name, mark in scores.items():
        if name not in students:
            students[name] = {}
        students[name][subject] = mark

print(students)