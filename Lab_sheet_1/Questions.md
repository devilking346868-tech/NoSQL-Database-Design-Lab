# Lab Sheet-01: NoSQL Database Design Lab
# BCA V Semester / III Years (Session 2026- 2027)

## Question 1
Create a new MongoDB database named StudentDB and verify its successful creation using MongoDB Shell.

### Commands and Output

```
use("admin")
switched to db admin
use StudentDB
switched to db StudentDB
db.createCollection("Students")
{ ok: 1 }
show dbs
StudentDB   8.00 KiB
admin      40.00 KiB
config     60.00 KiB
db
StudentDB
```


## Question 2
Create the collections Students, Faculty, and Courses within the StudentDB database.

### Commands and Output

```
use StudentDB
already on db StudentDB
db.createCollection("Students")
MongoServerError[NamespaceExists]: Collection already exists. NS: StudentDB.Students
db.createCollection("Faculty")
{ ok: 1 }
db.createCollection("Courses")
{ ok: 1 }
show collections
Courses
Faculty
Students
```


## Question 3
Insert a single document into the Students collection containing student details such as Roll Number, Name, Department, Semester, and CGPA.

### Commands and Output

```
use StudentDB
switched to db StudentDB
db.Students.insertOne({
    RollNumber: 101,
    Name: "Rohit",
    Department: "BCA",
    Semester: 5,
    CGPA: 8.5
})
{
  acknowledged: true,
  insertedId: ObjectId('6ae4269e831f636a19d044b5')
}
StudentDB
```



## Question 4
Insert multiple student documents into the Students collection using an appropriate MongoDB command.

### Commands and Output

```
test> use StudentDB
switched to db StudentDB
StudentDB> const students = [];

StudentDB> for (let i = 1; i <= 5; i++) {
|     students.push({
|         RollNumber: 100 + i,
|         Name: "Student" + i,
|         Department: "BCA",
|         Semester: 5,
|         CGPA: 8.0 + (i / 10)
|     });
| }
5
StudentDB> db.Students.insertMany(students);
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae427a11c61064776235ec9'),
    '1': ObjectId('6ae427a11c61064776235eca'),
    '2': ObjectId('6ae427a11c61064776235ecb'),
    '3': ObjectId('6ae427a11c61064776235ecc'),
    '4': ObjectId('6ae427a11c61064776235ecd')
  }
}
StudentDB> 
```



## Question 5
Retrieve all documents stored in the Students collection and display the results.

### Commands and Output

```
StudentDB> use StudentDB
already on db StudentDB
StudentDB> db.Students.find()
[
  {
    _id: ObjectId('6ae4269e831f636a19d044b5'),
    RollNumber: 101,
    Name: 'Rohit',
    Department: 'BCA',
    Semester: 5,
    CGPA: 8.5
  },
  {
    _id: ObjectId('6ae427a11c61064776235ec9'),
    RollNumber: 101,
    Name: 'Student1',
    Department: 'BCA',
    Semester: 5,
    CGPA: 8.1
  },
  {
    _id: ObjectId('6ae427a11c61064776235eca'),
    RollNumber: 102,
    Name: 'Student2',
    Department: 'BCA',
    Semester: 5,
    CGPA: 8.2
  },
  {
    _id: ObjectId('6ae427a11c61064776235ecb'),
    RollNumber: 103,
    Name: 'Student3',
    Department: 'BCA',
    Semester: 5,
    CGPA: 8.3
  },
  {
    _id: ObjectId('6ae427a11c61064776235ecc'),
    RollNumber: 104,
    Name: 'Student4',
    Department: 'BCA',
    Semester: 5,
    CGPA: 8.4
  },
  {
    _id: ObjectId('6ae427a11c61064776235ecd'),
    RollNumber: 105,
    Name: 'Student5',
    Department: 'BCA',
    Semester: 5,
    CGPA: 8.5
  }
]
StudentDB> 
```



## Question 6
Retrieve a specific student record based on the Roll Number using a suitable query.

### Commands and Output

```
StudentDB> use StudentDB
already on db StudentDB
StudentDB> db.Students.find({ RollNumber: 101 })
[
  {
    _id: ObjectId('6ae4269e831f636a19d044b5'),
    RollNumber: 101,
    Name: 'Rohit',
    Department: 'BCA',
    Semester: 5,
    CGPA: 8.5
  },
  {
    _id: ObjectId('6ae427a11c61064776235ec9'),
    RollNumber: 101,
    Name: 'Student1',
    Department: 'BCA',
    Semester: 5,
    CGPA: 8.1
  }
]
StudentDB> 
```



## Question 7
Retrieve documents by applying a condition on the Department field and display the matching records.

### Commands and Output

```
StudentDB> use StudentDB
already on db StudentDB
StudentDB> db.Students.find({ Department: "BCA" })
[
  {
    _id: ObjectId('6ae4269e831f636a19d044b5'),
    RollNumber: 101,
    Name: 'Rohit',
    Department: 'BCA',
    Semester: 5,
    CGPA: 8.5
  },
  {
    _id: ObjectId('6ae427a11c61064776235ec9'),
    RollNumber: 101,
    Name: 'Student1',
    Department: 'BCA',
    Semester: 5,
    CGPA: 8.1
  },
  {
    _id: ObjectId('6ae427a11c61064776235eca'),
    RollNumber: 102,
    Name: 'Student2',
    Department: 'BCA',
    Semester: 5,
    CGPA: 8.2
  },
  {
    _id: ObjectId('6ae427a11c61064776235ecb'),
    RollNumber: 103,
    Name: 'Student3',
    Department: 'BCA',
    Semester: 5,
    CGPA: 8.3
  },
  {
    _id: ObjectId('6ae427a11c61064776235ecc'),
    RollNumber: 104,
    Name: 'Student4',
    Department: 'BCA',
    Semester: 5,
    CGPA: 8.4
  },
  {
    _id: ObjectId('6ae427a11c61064776235ecd'),
    RollNumber: 105,
    Name: 'Student5',
    Department: 'BCA',
    Semester: 5,
    CGPA: 8.5
  }
]
StudentDB> 
```



## Question 8
Display only selected fields (such as Name and Department) from the Students collection using field projection.
### Commands and Output

```
StudentDB> use StudentDB
already on db StudentDB
StudentDB> db.Students.find(
|     {},
|     { Name: 1, Department: 1, _id: 0 }
| )
[
  { Name: 'Rohit', Department: 'BCA' },
  { Name: 'Student1', Department: 'BCA' },
  { Name: 'Student2', Department: 'BCA' },
  { Name: 'Student3', Department: 'BCA' },
  { Name: 'Student4', Department: 'BCA' },
  { Name: 'Student5', Department: 'BCA' }
]
StudentDB> 
```

## Question 9
Update the department of a specific student using the updateOne() method.
### Commands and Output

```
test> use StudentDB
switched to db StudentDB
StudentDB> db.Students.updateOne(
|     { RollNumber: 101 },
|     { $set: { Department: "MCA" } }
| )
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
StudentDB> 
```

## Question 10
Modify the semester of all students belonging to a particular department using the updateMany() method.
### Commands and Output

```
StudentDB> use StudentDB
already on db StudentDB
StudentDB> db.Students.updateMany(
|     { Department: "BCA" },
|     { $set: { Semester: 6 } }
| )
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 5,
  modifiedCount: 5,
  upsertedCount: 0
}
StudentDB> 
```

## Question 11
Replace an existing student document with a new document using the replaceOne() method.
### Commands and Output

```
StudentDB> use StudentDB
already on db StudentDB
StudentDB> db.Students.replaceOne(
|     { RollNumber: 101 },
|     {
|         RollNumber: 101,
|         Name: "Rohit",
|         Department: "MCA",
|         Semester: 6,
|         CGPA: 9.0
|     }
| )
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
StudentDB> 
```

## Question 12
Add a new field named Email to all documents in the Students collection.
### Commands and Output

```
StudentDB> use StudentDB
already on db StudentDB
StudentDB> db.Students.updateMany(
|     {},
|     { $set: { Email: "student@example.com" } }
| )
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 6,
  modifiedCount: 6,
  upsertedCount: 0
}
StudentDB> 
```

## Question 13
Remove an existing field from all documents in the collection using an appropriate update operator.
### Commands and Output

```
StudentDB> use StudentDB
already on db StudentDB
StudentDB> db.Students.updateMany(
|     {},
|     { $unset: { Email: "" } }
| )
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 6,
  modifiedCount: 6,
  upsertedCount: 0
}
StudentDB> 
```

## Question 14
Delete a specific student document based on the Roll Number using the deleteOne() method.
### Commands and Output

```
StudentDB> use StudentDB
already on db StudentDB
StudentDB> db.Students.deleteOne({ RollNumber: 101 })
{ acknowledged: true, deletedCount: 1 }
StudentDB> 
```

## Question 15
Delete multiple student records that satisfy a specified condition using the deleteMany() method.
### Commands and Output

```
StudentDB> use StudentDB
already on db StudentDB
StudentDB> db.Students.deleteMany({ Department: "BCA" })
{ acknowledged: true, deletedCount: 5 }
StudentDB> 
```

## Question 16
Count the total number of documents present in the Students collection.
### Commands and Output

```
StudentDB> use StudentDB
already on db StudentDB
StudentDB> db.Students.countDocuments()
0
StudentDB> 
```

## Question 17
Rename the Students collection to StudentDetails and verify the changes.
### Commands and Output

```
StudentDB> use StudentDB
already on db StudentDB
StudentDB> db.Students.renameCollection("StudentDetails")
{ ok: 1 }
StudentDB> show collections
Courses
Faculty
StudentDetails
StudentDB> 
```

## Question 18
Create a new collection named Departments and insert sample departmental information.
### Commands and Output

```
StudentDB> use StudentDB
already on db StudentDB
StudentDB> db.createCollection("Departments")
{ ok: 1 }
StudentDB> db.Departments.insertMany([
|     {
|         DepartmentID: 1,
|         DepartmentName: "Computer Science",
|         HOD: "Mr. Sharma"
|     },
|     {
|         DepartmentID: 2,
|         DepartmentName: "Mathematics",
|         HOD: "Mr. Verma"
|     },
|     {
|         DepartmentID: 3,
|         DepartmentName: "Physics",
|         HOD: "Mr. Kumar"
|     }
| ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae42e5c6781ee66bb87ab83'),
    '1': ObjectId('6ae42e5c6781ee66bb87ab84'),
    '2': ObjectId('6ae42e5c6781ee66bb87ab85')
  }
}
StudentDB> 
```

## Question 19
Drop the Departments collection and verify its successful deletion.
### Commands and Output

```
StudentDB> use StudentDB
already on db StudentDB
StudentDB> db.Departments.drop()
true
StudentDB> show collections
Courses
Faculty
StudentDetails
StudentDB> 
```

## Question 20
Drop the StudentDB database and confirm that all collections have been removed.
### Commands and Output

```
StudentDB> use StudentDB
already on db StudentDB
StudentDB> db.dropDatabase()
{ ok: 1, dropped: 'StudentDB' }
StudentDB> show dbs
admin    40.00 KiB
config  108.00 KiB
StudentDB> 
```

## Question 21
Recreate the StudentDB database and insert sample data after deletion.
### Commands and Output

```
StudentDB> use StudentDB
already on db StudentDB
StudentDB> db.Students.insertMany([
|     {
|         RollNumber: 101,
|         Name: "Rohit",
|         Department: "BCA",
|         Semester: 5,
|         CGPA: 8.5
|     },
|     {
|         RollNumber: 102,
|         Name: "Amit",
|         Department: "BCA",
|         Semester: 5,
|         CGPA: 8.2
|     },
|     {
|         RollNumber: 103,
|         Name: "Rahul",
|         Department: "MCA",
|         Semester: 3,
|         CGPA: 8.7
|     }
| ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae42f8d6781ee66bb87ab86'),
    '1': ObjectId('6ae42f8d6781ee66bb87ab87'),
    '2': ObjectId('6ae42f8d6781ee66bb87ab88')
  }
}
StudentDB> show dbs
StudentDB    8.00 KiB
admin       40.00 KiB
config     108.00 KiB
StudentDB> 
```

## Question 22
Perform all CRUD operations using MongoDB Compass and compare the results with the MongoDB Shell.
### Commands and Output

```
MongoDB Compass:

1. Open MongoDB Compass.
2. Connect to mongodb://localhost:27017
3. Select StudentDB database.
4. Open Students collection.

CREATE:
Click Add Data → Insert Document.

READ:
Open the Documents tab to view all documents.

UPDATE:
Select a document → Edit → Modify fields → Update.

DELETE:
Select a document → Delete → Confirm.

COMPARISON WITH MONGODB SHELL:

1. Insert:
db.Students.insertOne({RollNumber: 104, Name: "Priya", Department: "BCA", Semester: 5, CGPA: 9.0})

2. Read:
db.Students.find()

3. Update:
db.Students.updateOne(
    {RollNumber: 104},
    {$set: {CGPA: 9.5}}
)

4. Delete:
db.Students.deleteOne({RollNumber: 104})
```

## Question 23
Demonstrate the use of both MongoDB Shell and MongoDB Compass for managing databases and collections.
### Commands and Output

```
MONGODB SHELL:

1. Open MongoDB Shell using mongosh.

2. Create a database:
   use StudentDB

3. Create collections:
   db.createCollection("Students")
   db.createCollection("Faculty")
   db.createCollection("Courses")

4. Display all collections:
   show collections

5. Display all databases:
   show dbs

6. Drop a collection:
   db.Courses.drop()

7. Drop the database:
   db.dropDatabase()


MONGODB COMPASS:

1. Open MongoDB Compass.

2. Connect to:
   mongodb://localhost:27017

3. Click "Create Database".

4. Enter database name: StudentDB

5. Enter collection name: Students.

6. Click "Create Database".

7. Create additional collections using "Create Collection".

8. View all databases and collections in the left sidebar.

9. To delete a collection, click the three dots beside its name and select "Drop Collection".

10. To delete a database, click the three dots beside its name and select "Drop Database".
```

## Question 24
Compare the CRUD operations of MongoDB with equivalent SQL operations and summarize the differences.
### Commands and Output

```
MONGODB CRUD VS SQL CRUD

1. CREATE (INSERT)

MongoDB:
db.Students.insertOne({
    RollNumber: 101,
    Name: "Rohit",
    Department: "BCA"
})

SQL:
INSERT INTO Students (RollNumber, Name, Department)
VALUES (101, 'Rohit', 'BCA');


2. READ (SELECT)

MongoDB:
db.Students.find()

SQL:
SELECT * FROM Students;


3. UPDATE

MongoDB:
db.Students.updateOne(
    { RollNumber: 101 },
    { $set: { Department: "MCA" } }
)

SQL:
UPDATE Students
SET Department = 'MCA'
WHERE RollNumber = 101;


4. DELETE

MongoDB:
db.Students.deleteOne({ RollNumber: 101 })

SQL:
DELETE FROM Students
WHERE RollNumber = 101;


5. DIFFERENCES

MongoDB:
- NoSQL document-oriented database.
- Stores data in BSON documents.
- Uses collections instead of tables.
- Uses flexible schemas.
- Uses JSON-like query syntax.

SQL:
- Relational database.
- Stores data in rows and columns.
- Uses tables instead of collections.
- Usually follows a predefined schema.
- Uses Structured Query Language (SQL).
```

## Question 25
Prepare a comprehensive laboratory report containing the objectives, commands executed, outputs, screenshots, observations, and conclusion for all CRUD operations performed in this experiment.
### Commands and Output

```
StudentDB> use StudentDB
already on db StudentDB
StudentDB> db.Students.find(
|     {},
|     { Name: 1, Department: 1, _id: 0 }
| )
[
  { Name: 'Rohit', Department: 'BCA' },
  { Name: 'Student1', Department: 'BCA' },
  { Name: 'Student2', Department: 'BCA' },
  { Name: 'Student3', Department: 'BCA' },
  { Name: 'Student4', Department: 'BCA' },
  { Name: 'Student5', Department: 'BCA' }
]
StudentDB> 
```