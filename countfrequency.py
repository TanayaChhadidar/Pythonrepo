n = 122333
freq = {}

for digit in str(n):
    freq[digit] = freq.get(digit, 0) + 1

print(freq)