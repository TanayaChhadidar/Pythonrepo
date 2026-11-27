class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def display(self):
        print("Laptop Brand:", self.brand)
        print("RAM:", self.ram, "GB")


l1 = Laptop("Asus", 16)
l1.display()