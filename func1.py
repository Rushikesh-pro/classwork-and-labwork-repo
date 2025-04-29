class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of employee is {self.name} with {self.id} age")

class Programmer(Employee):
    def displayLanguages(self):
        print("having knowledge about python")

obj = Programmer("Hari",54)
obj.displayLanguages()
obj.showDetails()


