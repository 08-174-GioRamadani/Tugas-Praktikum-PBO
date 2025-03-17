class Employee:
    def __init__(self, name, role, hours_worked, task_completed):
        self.name = name
        self.role = role
        self.hours_worked = hours_worked
        self.task_completed = task_completed

    def work(self):
        print(f"{self.name} is working.")

    def evaluate_performance(self):
        # Logika dasar jika tidak di-override
        if self.task_completed / self.hours_worked >= 1:
            return "High Performance"
        elif self.task_completed / self.hours_worked >= 0.5:
            return "Medium Performance"
        else:
            return "Low Performance"

class SoftwareEngineer(Employee):
    def work(self):
        print(f"{self.name} (Software Engineer) is coding.")

    def evaluate_performance(self):
        ratio = self.task_completed / self.hours_worked
        if ratio >= 1.2:
            return "High Performance"
        elif ratio >= 0.7:
            return "Medium Performance"
        else:
            return "Low Performance"

class DataScientist(Employee):
    def work(self):
        print(f"{self.name} (Data Scientist) is analyzing data.")

    def evaluate_performance(self):
        ratio = self.task_completed / self.hours_worked
        if ratio >= 1.1:
            return "High Performance"
        elif ratio >= 0.6:
            return "Medium Performance"
        else:
            return "Low Performance"

class ProductManager(Employee):
    def work(self):
        print(f"{self.name} (Product Manager) is managing the product roadmap.")

    def evaluate_performance(self):
        ratio = self.task_completed / self.hours_worked
        if ratio >= 1.0:
            return "High Performance"
        elif ratio >= 0.5:
            return "Medium Performance"
        else:
            return "Low Performance"

# Contoh Penggunaan
employees = [
    SoftwareEngineer("Alice", "Software Engineer", 40, 50),
    DataScientist("Bob", "Data Scientist", 40, 25),
    ProductManager("Charlie", "Product Manager", 40, 20),
    SoftwareEngineer("David", "Software Engineer", 40, 10)
]

# Menampilkan hasil
for employee in employees:
    employee.work()
    print(f"Performance Rating: {employee.evaluate_performance()}\n")
