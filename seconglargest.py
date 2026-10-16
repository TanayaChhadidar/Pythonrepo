arr = [10, 20, 5, 20, 15]

unique = list(set(arr))
largest = max(unique)
unique.remove(largest)

print(max(unique))