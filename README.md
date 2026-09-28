# 🚀 OOP Wrapper: Employee Management System

> **Project Name:** OOP Wrapper (Employee Management System)
>  
> **Author:** Jenisha Ramani
> 

A Python-based menu-driven console application designed to create and display Person, Employee, Manager, and Developer details using Object-Oriented Programming (OOP) concepts.

---

## 🎯 Project Objectives

- 🖥️ **Menu-Driven Interface:** Create an interactive console application for employee management.
- 👤 **Person Class:** Store and display a person's name and age.
- 💼 **Employee Class:** Manage employee ID and salary details using inheritance.
- 🔒 **Encapsulation:** Use private attributes with getter and setter methods.
- 🔗 **Inheritance:** Demonstrate inheritance using Person, Employee, Manager, and Developer classes.
- 🔄 **Polymorphism:** Implement method overriding to display different details.
- ⚙️ **Super Function:** Use `super()` to access parent class constructors and methods.
- 🧹 **Destructor:** Demonstrate the use of the `__del__()` destructor method.
- 🧬 **Subclass Checking:** Use `issubclass()` to check class inheritance relationships.

---

## ✨ Features & Functionality

1. **Create a Person:** Enter and store a person's name and age.
2. **Create an Employee:** Enter employee name, age, employee ID, and salary.
3. **Create a Manager:** Store manager details with department information.
4. **Create a Developer:** Store developer details with programming language information.
5. **Show Details:** Display the stored details of Person, Employee, Manager, or Developer.
6. **Subclass Checking:** Check whether Manager and Developer are subclasses of Employee.
7. **Interactive Menu:** Perform multiple operations until the user selects Exit.
8. **Invalid Choice Handling:** Display an error message for invalid menu selections.
9. **Details Availability:** Display a message if the requested details are not available.

---

## 🧠 OOP Concepts Used

- Classes and Objects
- Constructor (`__init__`)
- Single Inheritance
- Multilevel Inheritance
- Encapsulation
- Private Attributes
- Getter and Setter Methods
- Polymorphism
- Method Overriding
- `super()` Function
- Destructor (`__del__`)
- `issubclass()` Function
- Conditional Statements (`if-elif-else`)
- While Loop
- User Input (`input()`)

---

## 💻 Technologies Used

- **Programming Language:** Python 3
- **Code Editor:** Visual Studio Code
- **Version Control:** Git
- **Repository:** GitHub

---

## 📂 Project Structure

```text
OOP_Wrapper/
│
├── OOP.Wrapper.py    # Main Python program
├── output.png        # Program output screenshot
└── README.md         # Project documentation
```
## 📸 Project Output

```text
--- Python OOP Project: Employee Management System ---

--- Subclass Checking ---
Manager is subclass of Employee: True
Developer is subclass of Employee: True

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 1
Enter Name: jenisha
Enter Age: 21

Person created with name: jenisha and age: 21

--- Choose another operation ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 2
Enter Name: kinjal
Enter Age: 23
Enter Employee ID: M121
Enter Salary: 90000

Employee created with name: kinjal age: 23 ID: M121 and salary: $ 90000.0

--- Choose another operation ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 3
Enter Name: parag
Enter Age: 21
Enter Employee ID: M122
Enter Salary: 80000
Enter Department: sales

Manager created with name: parag age: 21 ID: M122 salary: $ 80000.0 and department: sales

--- Choose another operation ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 4
Enter Name: vivek
Enter Age: 20
Enter Employee ID: M123
Enter Salary: 97000
Enter Programming Language: python

Developer created with name: vivek age: 20 ID: M123 salary: $ 97000.0 and programming language: python

--- Choose another operation ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 5

Choose details to show:
1. Person
2. Employee
3. Manager
4. Developer
Enter your choice: 4

Developer Details:
Name: vivek
Age: 20
Employee ID: M123
Salary: $ 97000.0
Programming Language: python

--- Choose another operation ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 6

Exiting the system. All resources have been freed.
Goodbye!
```
