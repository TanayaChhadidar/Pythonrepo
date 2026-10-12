a = [1, 2, 2, 3, 4, 3]
b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)