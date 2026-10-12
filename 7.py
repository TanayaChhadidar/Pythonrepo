a = [0, 3, 0, 5, 2]
b = []

for i in a:
    if i != 0:
        b.append(i)

for i in a:
    if i == 0:
        b.append(i)

print(b)