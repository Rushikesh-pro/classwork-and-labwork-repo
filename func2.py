class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of employee is {self.name} with {self.id} age")

e=Employee("Hari",45)
e.showDetails()
e1=Employee("Ram",67)
e1.showDetails()