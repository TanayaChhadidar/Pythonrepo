a = [1, 2, 3, 2, 4, 2]
n = int(input("Enter element: "))
count = 0

for i in a:
    if i == n:
        count += 1

print("Occurrences:", count)