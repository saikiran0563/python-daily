with open("data.txt", "w")as file:
    file.write("hello python")

with open("data.txt", "r")as file:
    content=file.read()

print(content)


with open("student.txt", "r")as file:
    for line in file:
        print(line.strip())


with open("student.txt", "x")as file:
    file.write("Kiran \n Rahul \n Arjun \nPriya")

with open("student.txt", "r")as file:
    for line in file:
        print(line.strip())