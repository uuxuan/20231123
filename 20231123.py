class Person:
     
    def __init__(self,name,emp_id,age,salary,department):
        self.name=name
        self.id=emp_id
        self.age=age
        self.department=department
        self.salary=salary

    def calculate_salary(self, salary, hours_worked):
        overtime = 5
        if hours_worked > 50:
            overtime = hours_worked - 50
        self.salary = self.salary + (overtime * (self.salary / 50))

    def assign_department(self, emp_department):
        self.department = emp_department

    def print_employee_details(self):
        print("\nName: ", self.name)
        print("ID: ", self.id)
        print("Age: ",  self.age)
        print("Salary: ", self.salary)
        print("Department: ", self.department)
        print("⋯♡⋯⋯⋯♡我是分隔線♡⋯⋯⋯♡⋯")
    
employee1 = Person("ADAMS", "E7876", 20, 50000, "ACCOUNTING")
employee2 = Person("JONES", "E7499", 36, 45000, "RESEARCH")
employee3 = Person("MARTIN", "E7900", 40, 50000, "SALES")
employee4 = Person("SMITH", "E7698", 25, 55000, "OPERATIONS")

print("原始資料:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()

#Change department
employee1.assign_department("OPERATIONS")
employee4.assign_department("SALES")

#Calculate the overtime of employees
employee2.calculate_salary(45000, 52)
employee4.calculate_salary(45000, 60)

print("更新資料:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()      
