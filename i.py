price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

amount = price * discount / 100
final_price = price - amount

print("Discount:", amount)
print("Final price:", final_price)