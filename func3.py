# Employee class to store official information
class Employee:
    def __init__(self):
        self.employee_id = None
        self.designation = None

    # Method to get employee information
    def get_employee_info(self):
        self.employee_id = input("Enter Employee ID: ")
        self.designation = input("Enter Employee Designation: ")

    # Method to display employee information
    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Designation: {self.designation}")

# Main part of the program
if __name__ == "__main__":
    # Create an instance of Employee
    emp = Employee()

    # Get employee information from the user
    emp.get_employee_info()

    # Display the employee information
    emp.display_employee_info()
