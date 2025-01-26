class Employee:
    def __init__(self, name, salary):
        self.salary = salary
        self.name = name

    def getSalary(self):
        print(f"Salary of {self.name} -> {self.salary}")

ankush = Employee("Ankush", "534454543534")
ankush.getSalary()
