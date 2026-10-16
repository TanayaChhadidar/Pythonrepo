with open("welcome.txt", "w") as file:
    file.write("Welcome to the magical world of Python")

with open("welcome.txt", "r") as file:
    content = file.read()
    print(content)