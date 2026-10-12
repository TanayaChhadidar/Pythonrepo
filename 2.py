marks = {
    "Amit": 75,
    "Rahul": 90,
    "Priya": 85
}

name = max(marks, key=marks.get)

print("Top student:", name)
print("Marks:", marks[name])