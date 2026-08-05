# *args

def show(*args):
    print(args)

show(10, 20)
show(10, 20, 30, 40)


def total(*args):
    total = 0

    for number in args:
        total += number

    return total

print(total(10, 20))
print(total(10, 20, 30))
print(total(10, 20, 30, 40))


# **kwargs

def student(**kwargs):
    print(kwargs)

student(name="Kiran", age=22)


def display(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display(
    name="Kiran",
    age=22,
    branch="CSE",
    city="Hyderabad"
)


# Packing

def pack_args(*args):
    print(args)

pack_args(10, 20, 30)


def pack_kwargs(**kwargs):
    print(kwargs)

pack_kwargs(name="Kiran", age=22)


# Unpacking

numbers = [10, 20]

def add(a, b):
    return a + b

print(add(*numbers))


data = {
    "name": "Kiran",
    "age": 22
}

def show_student(name, age):
    print(name)
    print(age)

show_student(**data)





# Mini Project - Student Information System

def display_subjects(*subjects):
    print("Subjects:")
    for subject in subjects:
        print("-", subject)


def display_student(**details):
    print("\nStudent Details:")
    for key, value in details.items():
        print(f"{key}: {value}")


# Function Calls

display_subjects(
    "Python",
    "Machine Learning",
    "Mathematics",
    "Statistics"
)

display_student(
    name="Kiran",
    age=22,
    branch="CSE",
    cgpa=8.5,
    city="Hyderabad"
)

def emp_details(**data):
    print("\n Employee Details:")
    for key,value in data.items():
        print(f"{key}:{value}")

emp_details(name="alice",
             salary=50000,
             department="HR",
             city="Delhi")

def skills(*skills):
    print("\nSkills:")
    for skill in skills:
        print("-", skill)

skills("Python", "Java", "C++", "SQL", "Flask")
