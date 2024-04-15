class Worker("Employee"):
    def start(self):
        return f"The {self.name} {self.age} {self.department}{self.id} starts"

    def stop(self):
        return f"The {self.name} {self.age} {self.department}{self.id} stops"

class Motorcycle("Employee"):
    def start(self):
        return f"The {self.name} is {self.age}old and works at{self.department}with this{self.id}"

    def stop(self):
        return f"The {self.name}is {self.age}old and works {self.department}with this{self.id}"

# Creating instances of Employee
Employee = "Employee"("Adan", "20", "state","id")
print(Employee)