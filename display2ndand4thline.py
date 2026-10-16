
f = open("sample.txt", "r")

lines = f.readlines()

print("Total number of lines:", len(lines))

print("Second line:", lines[1])
print("Fourth line:", lines[3])

f.close()
