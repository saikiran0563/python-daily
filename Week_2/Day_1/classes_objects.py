class Student:
    def __init__(self, name, age, branch):
        self.name=name
        self.age=age
        self.branch=branch

    def display(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)

s1=Student("Kiran", 21, "CSE")
s2=Student("Ravi", 22, "ECE")

s1.display()
s2.display()