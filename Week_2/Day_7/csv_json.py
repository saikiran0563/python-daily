import csv, json

student = []

with open("student.csv", "r")as file:
    reader= csv.DictReader(file)

    for row in reader:
        student.append(row)


with open("student.json", "w")as file:
    json.dump(student, file)

print("Data saved successfully")