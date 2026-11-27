class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)


s1 = Student("Tanaya", 101, "MCA")
s1.display()