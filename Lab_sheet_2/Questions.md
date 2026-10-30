# Lab Sheet-02: NoSQL Database Design Lab
# BCA V Semester / III Years (Session 2026- 2027)

## Question 1
Create a simple student database in an RDBMS and represent the same student data using a NoSQL document model. Compare both approaches based on schema, data storage, flexibility, and scalability.
- Create a Student table in MySQL.
- Insert at least 5 student records.
- Create an equivalent Students collection in MongoDB.
- Insert the same data as documents.
- Compare the two approaches.


# Experiment: RDBMS vs NoSQL Database

## Problem Statement
Create a simple student database in an RDBMS and represent the same student data using a NoSQL document model. Compare both approaches based on schema, data storage, flexibility, and scalability.

## 1. Objectives
- To understand RDBMS and NoSQL databases.
- To create a Student table in MySQL.
- To insert at least 5 student records.
- To create a Students collection in MongoDB.
- To insert the same student data as documents.
- To compare MySQL and MongoDB.

## 2. MySQL Implementation

### A. Create Database and Table

**Command:**

```sql
CREATE DATABASE StudentDB;

USE StudentDB;

CREATE TABLE Students (
    RollNumber INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Semester INT,
    CGPA FLOAT
);
```

### B. Insert 5 Student Records

**Command:**

```sql
INSERT INTO Students
(RollNumber, Name, Department, Semester, CGPA)
VALUES
(101, 'Rohit', 'BCA', 5, 8.5),
(102, 'Amit', 'BCA', 5, 8.2),
(103, 'Rahul', 'MCA', 3, 8.7),
(104, 'Priya', 'BCA', 5, 9.1),
(105, 'Neha', 'MCA', 3, 8.9);
```

### C. Display Records

**Command:**

```sql
SELECT * FROM Students;
```

**Output:**

All five student records are displayed successfully.

## 3. MongoDB Implementation

### A. Create Database and Collection

**Command:**

```javascript
use StudentDB

db.createCollection("Students")
```

### B. Insert Same 5 Student Records

**Command:**

```javascript
db.Students.insertMany([
    {
        RollNumber: 101,
        Name: "Rohit",
        Department: "BCA",
        Semester: 5,
        CGPA: 8.5
    },
    {
        RollNumber: 102,
        Name: "Amit",
        Department: "BCA",
        Semester: 5,
        CGPA: 8.2
    },
    {
        RollNumber: 103,
        Name: "Rahul",
        Department: "MCA",
        Semester: 3,
        CGPA: 8.7
    },
    {
        RollNumber: 104,
        Name: "Priya",
        Department: "BCA",
        Semester: 5,
        CGPA: 9.1
    },
    {
        RollNumber: 105,
        Name: "Neha",
        Department: "MCA",
        Semester: 3,
        CGPA: 8.9
    }
])
```

### C. Display Records

**Command:**

```javascript
db.Students.find()
```

**Output:**

All five student documents are displayed successfully.

## 4. Comparison Between MySQL and MongoDB

| Basis | MySQL (RDBMS) | MongoDB (NoSQL) |
|---|---|---|
| Schema | Fixed Schema | Flexible Schema |
| Data Storage | Rows and Columns | BSON Documents |
| Flexibility | Less Flexible | More Flexible |
| Scalability | Vertical Scaling | Horizontal Scaling |
| Relationships | Tables and Joins | Embedded Documents and References |
| Query Language | SQL | MongoDB Query Language |

## 5. Observations

- MySQL stores data in rows and columns.
- MongoDB stores data in BSON documents.
- Both databases store the same five student records.
- MySQL uses a predefined schema.
- MongoDB supports flexible document structures.
- Both databases support CRUD operations.

## 6. Conclusion

MySQL and MongoDB both successfully store and manage student records. MySQL is suitable for structured data with fixed schemas, whereas MongoDB is suitable for flexible and document-oriented data. Both databases have their own advantages depending on application requirements.

## 7. Screenshots

Attach the following screenshots:

- MySQL database and table creation.
- MySQL insertion and SELECT output.
- MongoDB database and collection creation.
- MongoDB insertMany() output.
- MongoDB find() output.



## Question 2
Create a MongoDB database named CollegeDB and a collection named Students. Insert at least five student documents containing: Student_ID, Name, Course, Semester, Marks

1. Display all documents.
2. Find students from a particular course.
3. Update marks of a student.
4. Delete one student.
5. Count the total number of students.


# Experiment: Create Collections in StudentDB

## Problem Statement

Create the collections Students, Faculty, and Courses within the StudentDB database.

## 1. Objective

To create multiple collections inside the StudentDB database using MongoDB Shell and verify their successful creation.

## 2. Commands and Output

### Step 1: Select the StudentDB Database

**Command:**

```javascript
use StudentDB
```

**Output:**

```text
already on db StudentDB
```

### Step 2: Create Students Collection

**Command:**

```javascript
db.createCollection("Students")
```

**Output:**

```text
MongoServerError[NamespaceExists]: Collection already exists. NS: StudentDB.Students
```

**Note:** The Students collection already existed in the database, so MongoDB displayed the NamespaceExists message.

### Step 3: Create Faculty Collection

**Command:**

```javascript
db.createCollection("Faculty")
```

**Output:**

```text
{ ok: 1 }
```

### Step 4: Create Courses Collection

**Command:**

```javascript
db.createCollection("Courses")
```

**Output:**

```text
{ ok: 1 }
```

### Step 5: Display All Collections

**Command:**

```javascript
show collections
```

**Output:**

```text
Courses
Faculty
Students
```

## 3. Observations

1. Successfully selected the StudentDB database.
2. The Students collection already existed.
3. Successfully created Faculty and Courses collections.
4. Verified all three collections using the show collections command.

## 4. Conclusion

In this experiment, three collections named Students, Faculty, and Courses were managed within the StudentDB database using MongoDB Shell. Their existence was successfully verified using the show collections command.



## Question 3
Create a MongoDB collection named Orders where each order contains customer information
and its associated products as an embedded document/array.
1. Insert at least five orders.
2. Display orders of a particular customer.
3. Update the quantity of a product.
4. Calculate the total order amount using aggregation.
5. Display orders above a specified amount.


# Experiment: MongoDB Orders Collection Using Embedded Documents

## Problem Statement

Create a MongoDB collection named Orders where each order contains customer information and its associated products as an embedded document/array.

## 1. Objectives

1. To create an Orders collection in MongoDB.
2. To insert at least five orders.
3. To retrieve orders of a particular customer.
4. To update the quantity of a product.
5. To calculate the total order amount using aggregation.
6. To display orders above a specified amount.
7. To understand embedded documents and arrays in MongoDB.

## 2. Create Database and Collection

**Command:**

```javascript
use OrderDB

db.createCollection("Orders")
```

**Output:**

```text
switched to db OrderDB
{ ok: 1 }
```

## 3. Insert Five Orders

**Command:**

```javascript
db.Orders.insertMany([
    {
        Order_ID: 101,
        Customer: {
            Customer_ID: 1,
            Name: "Rohit"
        },
        Products: [
            { Product: "Laptop", Quantity: 1, Price: 50000 },
            { Product: "Mouse", Quantity: 2, Price: 500 }
        ]
    },
    {
        Order_ID: 102,
        Customer: {
            Customer_ID: 2,
            Name: "Amit"
        },
        Products: [
            { Product: "Keyboard", Quantity: 1, Price: 1500 },
            { Product: "Mouse", Quantity: 1, Price: 500 }
        ]
    },
    {
        Order_ID: 103,
        Customer: {
            Customer_ID: 3,
            Name: "Rahul"
        },
        Products: [
            { Product: "Monitor", Quantity: 1, Price: 12000 }
        ]
    },
    {
        Order_ID: 104,
        Customer: {
            Customer_ID: 1,
            Name: "Rohit"
        },
        Products: [
            { Product: "Laptop", Quantity: 1, Price: 50000 },
            { Product: "Keyboard", Quantity: 1, Price: 1500 }
        ]
    },
    {
        Order_ID: 105,
        Customer: {
            Customer_ID: 4,
            Name: "Priya"
        },
        Products: [
            { Product: "Headphones", Quantity: 2, Price: 2000 }
        ]
    }
])
```

**Output:**

```text
acknowledged: true
insertedIds: 5 documents
```

## 4. Display All Orders

**Command:**

```javascript
db.Orders.find()
```

**Output:**

Displays all five orders with customer information and associated products.

## 5. Display Orders of a Particular Customer

**Command:**

```javascript
db.Orders.find({
    "Customer.Name": "Rohit"
})
```

**Output:**

Displays all orders placed by customer Rohit.

## 6. Update the Quantity of a Product

**Command:**

```javascript
db.Orders.updateOne(
    {
        Order_ID: 101,
        "Products.Product": "Mouse"
    },
    {
        $set: {
            "Products.$.Quantity": 3
        }
    }
)
```

**Output:**

```text
{
    acknowledged: true,
    matchedCount: 1,
    modifiedCount: 1
}
```

## 7. Calculate Total Order Amount Using Aggregation

**Command:**

```javascript
db.Orders.aggregate([
    {
        $unwind: "$Products"
    },
    {
        $group: {
            _id: "$Order_ID",
            Customer: { $first: "$Customer.Name" },
            TotalAmount: {
                $sum: {
                    $multiply: [
                        "$Products.Quantity",
                        "$Products.Price"
                    ]
                }
            }
        }
    },
    {
        $sort: { _id: 1 }
    }
])
```

**Output:**

```text
[
    { _id: 101, Customer: "Rohit", TotalAmount: 51500 },
    { _id: 102, Customer: "Amit", TotalAmount: 2000 },
    { _id: 103, Customer: "Rahul", TotalAmount: 12000 },
    { _id: 104, Customer: "Rohit", TotalAmount: 51500 },
    { _id: 105, Customer: "Priya", TotalAmount: 4000 }
]
```

## 8. Display Orders Above a Specified Amount

**Command:**

```javascript
db.Orders.aggregate([
    {
        $unwind: "$Products"
    },
    {
        $group: {
            _id: "$Order_ID",
            Customer: { $first: "$Customer.Name" },
            TotalAmount: {
                $sum: {
                    $multiply: [
                        "$Products.Quantity",
                        "$Products.Price"
                    ]
                }
            }
        }
    },
    {
        $match: {
            TotalAmount: { $gt: 10000 }
        }
    }
])
```

**Output:**

```text
[
    { _id: 101, Customer: "Rohit", TotalAmount: 51500 },
    { _id: 103, Customer: "Rahul", TotalAmount: 12000 },
    { _id: 104, Customer: "Rohit", TotalAmount: 51500 }
]
```

## 9. Observations

1. Successfully created the Orders collection.
2. Inserted five order documents.
3. Customer information was stored as an embedded document.
4. Products were stored as an embedded array.
5. Retrieved orders of a particular customer.
6. Updated the quantity of a product successfully.
7. Calculated order amounts using the aggregation pipeline.
8. Retrieved orders having a total amount greater than 10000.

## 10. Conclusion

In this experiment, an Orders collection was created using MongoDB with embedded customer documents and product arrays. Five orders were inserted successfully. Different queries were performed to retrieve customer orders, update product quantities, calculate total order amounts using aggregation, and filter orders based on their total amount. This experiment demonstrated the use of embedded documents, arrays, and aggregation in MongoDB.




## Question 4
Using a key-value database such as Redis, create a simple student information system.
1. Store student ID as the key and student name as the value.
2. Insert at least five students.
3. Retrieve a student using the key.
4. Update a student's value.
5. Delete a student.


# Practical: Student Information System Using Redis

## Aim
To create a simple Student Information System using Redis Key-Value Database.

## 1. Objectives

1. Store student ID as the key and student name as the value.
2. Insert at least five students.
3. Retrieve a student using the key.
4. Update a student's value.
5. Delete a student.

## 2. Software Requirements

1. Redis Server
2. Redis CLI
3. Linux Operating System

## 3. Practical Implementation

### Step 1: Start Redis CLI

**Command:**

```bash
redis-cli
```

### Step 2: Insert at least five students

**Commands:**

```redis
SET 101 "Rohit"
SET 102 "Amit"
SET 103 "Rahul"
SET 104 "Priya"
SET 105 "Neha"
```

**Output:**

```text
OK
OK
OK
OK
OK
```

### Step 3: Retrieve a student using the key

**Command:**

```redis
GET 101
```

**Output:**

```text
"Rohit"
```

### Step 4: Update a student's value

**Command:**

```redis
SET 101 "Rohit Singh"
```

**Output:**

```text
OK
```

Verify the updated value:

```redis
GET 101
```

**Output:**

```text
"Rohit Singh"
```

### Step 5: Delete a student

**Command:**

```redis
DEL 105
```

**Output:**

```text
(integer) 1
```

Verify deletion:

```redis
GET 105
```

**Output:**

```text
(nil)
```

### Step 6: Display all student records

**Command:**

```redis
KEYS *
```

**Expected Output:**

```text
1) "101"
2) "102"
3) "103"
4) "104"
```

## 4. Observations

1. Redis stores data in key-value pairs.
2. The `SET` command is used to insert or update values.
3. The `GET` command retrieves a value using its key.
4. The `DEL` command deletes a key-value pair.
5. Redis provides fast data access.

## 5. Conclusion

Successfully created a simple Student Information System using Redis. Inserted five student records, retrieved a student using its key, updated a student's name, and deleted a student record.

## 6. Screenshots

1. Redis CLI connection.
2. Inserting five student records.
3. Retrieving a student record.
4. Updating a student's name.
5. Deleting a student record.
6. Displaying remaining student records.
