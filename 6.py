a = [10, 20, 30, 40]
n = int(input("Enter element: "))

for i in range(len(a)):
    if a[i] == n:
        print("Index:", i)
        break
else:
    print("Element not found")