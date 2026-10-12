a = [10, 40, 20, 30]
largest = a[0]
second = None

for i in a:
    if i > largest:
        second = largest
        largest = i
    elif i != largest and (second is None or i > second):
        second = i

print("Second largest:", second)