import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()



class Employee:

    all_emps = []

    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE")
    )
    cursor = connection.cursor()
    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        Employee.all_emps.append(self)
        query = "INSERT INTO Employee (first_name, last_name, age, department, salary) VALUES (%s, %s, %s, %s, %s)"
        values = (self.first_name, self.last_name, self.age, self.department, self.salary)

        
        Employee.cursor.execute(query, values)
        Employee.connection.commit()


    def transfer(self, department):
        self.department = department
        query = """
            UPDATE Employee
            SET department = %s
            WHERE first_name = %s AND last_name = %s
        """

        values = (department, self.first_name, self.last_name)

        Employee.cursor.execute(query, values)
        Employee.connection.commit()

    def fire(self):
        self.department = None
        Employee.all_emps.remove(self)
        query = """
            Delete from Employee where first_name = %s and last_name= %s
"""
        values = (self.first_name, self.last_name)
        Employee.cursor.execute(query, values)
        Employee.connection.commit()


    def show(self):
        query = "SELECT first_name, last_name, age, department, salary FROM Employee WHERE first_name = %s AND last_name = %s"
        values = (self.first_name, self.last_name)
        
        Employee.cursor.execute(query, values)
        row = Employee.cursor.fetchone()
        
        if row:
            print(f"\n--- Employee Data ---")
            print(f"Name: {row[0]} {row[1]}")
            print(f"Age: {row[2]}")
            print(f"Department: {row[3]}")
            print(f"Salary: {row[4]}")
        else:
            print("Employee record not found in database.")
    @staticmethod
    def List_employees():
        query = "SELECT first_name, last_name, age, department, salary FROM Employee"
        Employee.cursor.execute(query)
        results = Employee.cursor.fetchall()
        
        if not results:
            print("\nNo employee records found.")
            return

        print("\n All Registered Employees ")
        for row in results:
            print(f"Name: {row[0]} {row[1]} | Age: {row[2]} | Department: {row[3]} | Salary: {row[4]}") 


class Manager(Employee):
    managed_depart = None

    def __init__(self, first_name, last_name, age, department, salary, managed_depart):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_depart = managed_depart

    def show(self):
        query = "SELECT first_name, last_name, age, department, salary FROM Employee WHERE first_name = %s AND last_name = %s"
        values = (self.first_name, self.last_name)
    
        Employee.cursor.execute(query, values)
    
        rows = Employee.cursor.fetchone()
        
        rows = list(rows) # because cursor fetch one returns a tuple and they're immutable
        
        rows[-1] = 'Confidential'
        for row in rows:
            print(row)


while True:
    print("\n==============================")
    print("  Employee Management System  ")
    print("==============================")
    print("Type 'add'  -> Create a record")
    print("Type 'list' -> View all employees")
    print("Type 'q'    -> Exit program")
    
    choice = input("\nEnter choice: ").strip().lower()
    
    if choice == 'q':
        print("\nClosing application database pipelines. Goodbye.")
        break
        
    elif choice == 'add':
        role = input("Press 'm' for Manager or 'e' for Employee: ").strip().lower()
        if role not in ['e', 'm']:
            print("Invalid role option selection.")
            continue
            
        print("\nPlease insert data:")
        f_name = input("First Name: ").strip()
        l_name = input("Last Name: ").strip()
        
        try:
            age = int(input("Age: ").strip())
            dept = input("Department: ").strip()
            salary = float(input("Salary: ").strip())
        except ValueError:
            print("Input Error: Age must be integer numeric values, Salary must be fractional decimal values.")
            continue

        if role == 'e':
            Employee(f_name, l_name, age, dept, salary)
            print(f"\nSuccess: Employee {f_name} {l_name} added.")
            
        elif role == 'm':
            m_dept = input("Managed Department: ").strip()
            Manager(f_name, l_name, age, dept, salary, m_dept)
            print(f"\nSuccess: Manager {f_name} {l_name} added.")
            
    elif choice == 'list':
        Employee.List_employees()
        
    else:
        print("Invalid choice configuration entry. Try again.")

    

