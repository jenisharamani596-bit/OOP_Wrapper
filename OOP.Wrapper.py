# Display project title  
print("--- Python OOP Project: Employee Management System ---")  


# Parent Class  
class Person:  
    # Constructor to initialize name and age  
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  

    # Display person details  
    def display(self):  
        print("Name:", self.name)  
        print("Age:", self.age)  


# Employee class inherits from Person  
class Employee(Person):  
    # Constructor to initialize employee details  
    def __init__(self, name, age, emp_id="", salary=0):  
        super().__init__(name, age)  
        self.__emp_id = emp_id  
        self.__salary = salary  

    # Getter method for salary  
    def get_salary(self):  
        return self.__salary  

    # Setter method for salary  
    def set_salary(self, salary):  
        self.__salary = salary  

    # Getter method for employee ID  
    def get_emp_id(self):  
        return self.__emp_id  

    # Override display method  
    def display(self):  
        super().display()  
        print("Employee ID:", self.__emp_id)  
        print("Salary: $", self.__salary)  

    # Destructor  
    def __del__(self):  
        pass  


# Manager class inherits from Employee  
class Manager(Employee):  
    # Constructor to initialize manager details  
    def __init__(self, name, age, emp_id, salary, department):  
        super().__init__(name, age, emp_id, salary)  
        self.department = department  

    # Override display method to show department  
    def display(self):  
        super().display()  
        print("Department:", self.department)  


# Developer class inherits from Employee  
class Developer(Employee):  
    # Constructor to initialize developer details  
    def __init__(self, name, age, emp_id, salary, language):  
        super().__init__(name, age, emp_id, salary)  
        self.language = language  

    # Override display method to show programming language  
    def display(self):  
        super().display()  
        print("Programming Language:", self.language)  


# Check issubclass()
print("\n--- Subclass Checking ---")
print("Manager is subclass of Employee:", issubclass(Manager, Employee))
print("Developer is subclass of Employee:", issubclass(Developer, Employee))


# Main Program  

# Initialize objects with None  
person = None  
employee = None  
manager = None  
developer = None  

# Check whether the menu is displayed for the first time  
first_time = True  

# Repeat the menu until the user exits  
while True:  

    # Display message after the first operation  
    if not first_time:  
        print("\n--- Choose another operation ---")  

    first_time = False  

    # Display main menu  
    print("\nChoose an operation:")  
    print("1. Create a Person")  
    print("2. Create an Employee")  
    print("3. Create a Manager")  
    print("4. Create a Developer")  
    print("5. Show Details")  
    print("6. Exit")  

    # Get user's choice  
    choice = input("\nEnter your choice: ")  

    # Create Person object  
    if choice == "1":  
        name = input("Enter Name: ")  
        age = int(input("Enter Age: "))  

        person = Person(name, age)  

        print("\nPerson created with name:", name, "and age:", age)  

    # Create Employee object  
    elif choice == "2":  
        name = input("Enter Name: ")  
        age = int(input("Enter Age: "))  
        emp_id = input("Enter Employee ID: ")  
        salary = float(input("Enter Salary: "))  

        employee = Employee(name, age, emp_id, salary)  

        print("\nEmployee created with name:", name,  
              "age:", age, "ID:", emp_id,  
              "and salary: $", salary)  

    # Create Manager object  
    elif choice == "3":  
        name = input("Enter Name: ")  
        age = int(input("Enter Age: "))  
        emp_id = input("Enter Employee ID: ")  
        salary = float(input("Enter Salary: "))  
        department = input("Enter Department: ")  

        manager = Manager(name, age, emp_id, salary, department)  

        print("\nManager created with name:", name,  
              "age:", age, "ID:", emp_id,  
              "salary: $", salary,  
              "and department:", department)  

    # Create Developer object  
    elif choice == "4":  
        name = input("Enter Name: ")  
        age = int(input("Enter Age: "))  
        emp_id = input("Enter Employee ID: ")  
        salary = float(input("Enter Salary: "))  
        language = input("Enter Programming Language: ")  

        developer = Developer(name, age, emp_id, salary, language)  

        print("\nDeveloper created with name:", name,  
              "age:", age, "ID:", emp_id,  
              "salary: $", salary,  
              "and programming language:", language)  

    # Display details menu  
    elif choice == "5":  
        print("\nChoose details to show:")  
        print("1. Person")  
        print("2. Employee")  
        print("3. Manager")  
        print("4. Developer")  

        sub_choice = input("Enter your choice: ")  

        # Display Person details  
        if sub_choice == "1":  
            if person is not None:  
                print("\nPerson Details:")  
                person.display()  
            else:  
                print("No Person details available.")  

        # Display Employee details  
        elif sub_choice == "2":  
            if employee is not None:  
                print("\nEmployee Details:")  
                employee.display()  
            else:  
                print("No Employee details available.")  

        # Display Manager details  
        elif sub_choice == "3":  
            if manager is not None:  
                print("\nManager Details:")  
                manager.display()  
            else:  
                print("No Manager details available.")  

        # Display Developer details  
        elif sub_choice == "4":  
            if developer is not None:  
                print("\nDeveloper Details:")  
                developer.display()  
            else:  
                print("No Developer details available.")  

        # Handle invalid details choice  
        else:  
            print("Invalid choice!")  

    # Exit the program  
    elif choice == "6":  
        print("\nExiting the system. All resources have been freed.")  
        print("Goodbye!")  
        break  

    # Handle invalid menu choice  
    else:  
        print("Invalid choice! Please try again.")