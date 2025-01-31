import sqlite3

# Connect to SQLite
connection = sqlite3.connect("Employees.db")

# Create a cursor object
cursor = connection.cursor()

# Enable foreign key support in SQLite
cursor.execute("PRAGMA foreign_keys = ON;")

# Corrected CREATE TABLE statements with Foreign Key constraint
table_info2 = """
CREATE TABLE DEPARTMENTS (
    ID INT PRIMARY KEY,
    Name VARCHAR(25) UNIQUE NOT NULL,  -- Ensuring unique department names
    Manager VARCHAR(25)
);
"""

table_info1 = """
CREATE TABLE EMPLOYEES (
    ID INT PRIMARY KEY,
    Name VARCHAR(25) NOT NULL,
    Department VARCHAR(25),
    Salary DECIMAL(10,2),
    Hire_Date DATE,
    FOREIGN KEY (Department) REFERENCES DEPARTMENTS(Name) ON DELETE SET NULL
);
"""

# Execute table creation
cursor.execute(table_info2)  # Create DEPARTMENTS table first (to avoid FK error)
cursor.execute(table_info1)  # Then create EMPLOYEES table

# Insert records into DEPARTMENTS table first
cursor.executemany('''INSERT INTO DEPARTMENTS (ID, Name, Manager) VALUES (?, ?, ?)''', [
    (1, 'Sales', 'Alice'),
    (2, 'Engineering', 'Bob'),
    (3, 'Marketing', 'Charlie')
])

# Insert records into EMPLOYEES table
cursor.executemany('''INSERT INTO EMPLOYEES (ID, Name, Department, Salary, Hire_Date) VALUES (?, ?, ?, ?, ?)''', [
    (1, 'Alice', 'Sales', 50000, '2021-01-15'),
    (2, 'Bob', 'Engineering', 70000, '2020-06-10'),
    (3, 'Charlie', 'Marketing', 60000, '2022-03-20'),
    (5, 'Raj', 'Sales', 40000, '2020-10-15'),
    (9, 'Nirmal', 'Marketing', 67000, '2020-05-02'),
    (7, 'Robby', 'Engineering', 55000, '2022-04-19'),
    (8, 'John', 'Engineering', 57000, '2021-08-20')
])

# Display all records from EMPLOYEES
print("The inserted records in EMPLOYEES table are:")
for row in cursor.execute('''SELECT * FROM EMPLOYEES'''):
    print(row)

# Display all records from DEPARTMENTS
print("\nThe inserted records in DEPARTMENTS table are:")
for row in cursor.execute('''SELECT * FROM DEPARTMENTS'''):
    print(row)

# Commit changes and close connection
connection.commit()
connection.close()
