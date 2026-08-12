# class Employee:
#     company ="ABC Technologies"

#     def __init__(self, name, salary):
#         self.name=name
#         self.salary=salary

#     def display(self):
#         print("Employee name:", self.name)
#         print("Salary:", self.salary)

#     @classmethod
#     def show_company(cls):
#         print("Company:", cls.company)

#     @staticmethod
#     def is_valid_salary(salary):
#         if salary>=15000:
#             return True
#         else:
#             return False

# e1=Employee("Kiran", 20000)
# e2=Employee("Ravi", 12000)

# e1.display()
# e2.display()

# Employee.show_company()

# print("Is valid salary:", Employee.is_valid_salary(30000))
# print("Is valid salary:", Employee.is_valid_salary(12000))



class Employee:

    company= "ABC Technologies"

    def __init__(self, name, salary, department):
        self.name=name
        self.salary=salary
        self.department=department

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)

    @classmethod
    def show_company(cls):
        print("Company:", cls.company)

    @staticmethod
    def is_valid_salary(salary):
        if salary >= 15000:
            return True
        else:
            return False

    def __str__(self):
        return f"Employee Name: {self.name} , Salary: {self.salary} , Department: {self.department}"

    def __repr__(self):
        return f"Employee:('{self.name}',{self.salary},'{self.department}')"

emp1=Employee("kiran",30000,"AI/ML")
emp2=Employee("Ravi",12000,"Python")

emp1.display()
emp2.display()

Employee.show_company()

print("Is valid salary:",Employee.is_valid_salary(30000))
print("Is valid salary:",Employee.is_valid_salary(12000))

print(emp1)
print(emp2)

print(repr(emp1))
print(repr(emp2))

