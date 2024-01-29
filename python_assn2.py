# Name: Kartheek Kotha
# Date: Jan 29, 2024
# Assignment: Assignment 2
class EmployeeList:
    def __init__(self, emp_list):
        self.emp_list = emp_list
    def save_list(self , emp_list):
        self.emp_list = emp_list
    def get_list(self):
        return self.emp_list
    def print_list(self):
        print(self.emp_list)
    def sort(self):
        choice = int(input("Enter the choice\n1 to sort by age\n2 to sort by name\n3 to sort by salary\nChoice :"))
        if choice == 1:
            self.sort_by_age()
        elif choice == 2:
            self.sort_by_name()
        elif choice == 3:
            self.sort_by_salary()
        else:
            print("Invalid input")
        return self.emp_list
    def sort_by_age(self):
        self.emp_list.sort(key=lambda x: x[2])
    def sort_by_name(self):
        self.emp_list.sort(key=lambda x: x[1])
    def sort_by_salary(self):
        self.emp_list.sort(key=lambda x: x[3])

if __name__ == "__main__":
    emp_list = [[161, "Ramu", 35, 59000], [171, "Tejas", 30, 82100], [171, "Abhi", 25, 100000], [152, "Jaya", 32, 85000]]
    emp = EmployeeList(emp_list)
    emp.print_list()
    emp.sort()
    emp.print_list()

