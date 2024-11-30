import csv

import os 
file_path='staff_details'
filepath=os.path.abspath(file_path)
print("filepath",filepath)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
        return f"Name:{self.name},Age:{self.age}"  
    
class Employee:
    def __init__(self,employee_id,position):
        self.employee_id = employee_id
        self.position  = position
    def display_info(self):
        return f"employee_id:{self.employee_id},position:{self.position}"

class Staff(Person,Employee):
    def __init__(self,name,age,employee_id,position,department):
        Person.__init__(self,name,age)
        Employee.__init__(self,employee_id,position)
        self.department=department
    def additional_info(self):
        return f"Department:{self.department}"
    
    def display_info(self):
        person_info=Person.display_info(self)
        employee_info=Employee.display_info(self)
        department_info=Staff.additional_info(self)
        return f"{person_info},{employee_info},{department_info}"
         
staff=Staff("mahi",18,7,"programmer","AI")
print(staff.display_info())

with open('staff_details',mode='w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["   "+ 'name' +"   "+'age'+"    "+'employee_id'+"    "+'position'+"     "+'department'])
    writer.writerow(["   "+ staff.name +"    "+ str(staff.age) +"       "+       str(staff.employee_id)   +"      "+ staff.position +"            "+ staff.department ])
    print ("your CSV file has been saved")