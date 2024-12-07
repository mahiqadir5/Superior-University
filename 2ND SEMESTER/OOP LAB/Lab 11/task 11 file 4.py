from task_11_file_2 import Manager 
from task_11_file_3 import Worker


def display_employees(employees):
        for employee in employees:
            print(f"{employee.get_name()} Age: {employee.get_age()} Salary: {employee.get_salary()}", end=" ")
        if isinstance(employee, Manager):
            print(f" Department: {employee.get_department()}")
        elif isinstance(employee, Worker):
            print(f"Hours Worked: {employee.get_hours_worked()}")
def add_employee(employees):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))
    emp_type = input("Enter type (Manager/Worker): ").strip().lower()

    if emp_type == 'manager':
        department = input("Enter department: ")
        employees.append(Manager(name, age, salary, department))
    elif emp_type == 'worker':
        hours_worked = int(input("Enter hours worked: "))
        employees.append(Worker(name, age, salary, hours_worked))

def update_employee(employees):
    name = input("Enter the name of the employee to update: ")
    for employee in employees:
        if employee.get_name().lower() == name.lower():
            new_name = input("Enter new name: ")
            employee.set_name(new_name)
            new_age = int(input("Enter new age: "))
            employee.set_age(new_age)
            new_salary = float(input("Enter new salary: "))
            employee.set_salary(new_salary)
            break
    else:
        print("Employee not found.")

def delete_employee(employees):
    name = input("Enter the name of the employee to delete: ")
    for employee in employees:
        if employee.get_name().lower() == name.lower():
            employees.remove(employee)
            print(f"Employee {name} deleted.")
            break
    else:
        print("Employee not found.")

def main():
    employees = []

    while True:
        print("\nMenu:")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_employee(employees)
        elif choice == 2:
            display_employees(employees)
        elif choice == 3:
            update_employee(employees)
        elif choice == 4:
            delete_employee(employees)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")
    main()
