n = int(input("Enter number: "))
temp = n
total = 0
digits = len(str(n))

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")