# Lab Sheet-03: NoSQL Database Design Lab
# BCA V Semester / III Years (Session 2026- 2027)

## Question 1
Design a Student Activity Tracking System in MongoDB that stores student details, enrolled courses, attendance, skills, and recent activities. Perform queries to retrieve students based on different activity conditions.

### Commands and Output

```javascript

test> use StudentActivityDB
switched to db StudentActivityDB
StudentActivityDB> db.createCollection("Students")
{ ok: 1 }
StudentActivityDB> db.Students.insertMany([
|     {
|         StudentID: 101,
|         Name: "Rohit",
|         Department: "BCA",
|         Semester: 5,
|         Courses: ["MongoDB", "Python", "Java"],
|         Attendance: {
|             TotalClasses: 100,
|             AttendedClasses: 90,
|             Percentage: 90
|         },
|         Skills: ["Python", "JavaScript", "MongoDB"],
|         RecentActivities: [
|             { Activity: "Assignment Submitted", Date: ISODate("2026-10-20") }, 
|             { Activity: "Quiz Completed", Date: ISODate("2026-10-25") }
|         ]
|     },
|     {
|         StudentID: 102,
|         Name: "Amit",
|         Department: "BCA",
|         Semester: 5,
|         Courses: ["Python", "C++"],
|         Attendance: {
|             TotalClasses: 100,
|             AttendedClasses: 75,
|             Percentage: 75
|         },
|         Skills: ["Python", "C++"],
|         RecentActivities: [
|             { Activity: "Assignment Submitted", Date: ISODate("2026-10-18") }
|         ]
|     },
|     {
|         StudentID: 103,
|         Name: "Rahul",
|         Department: "MCA",
|         Semester: 3,
|         Courses: ["MongoDB", "Java"],
|         Attendance: {
|             TotalClasses: 100,
|             AttendedClasses: 95,
|             Percentage: 95
|         },
|         Skills: ["Java", "MongoDB"],
|         RecentActivities: [
|             { Activity: "Project Completed", Date: ISODate("2026-10-26") }
|         ]
|     },
|     {
|         StudentID: 104,
|         Name: "Priya",
|         Department: "BCA",
|         Semester: 5,
|         Courses: ["Python", "Web Development"],
|         Attendance: {
|             TotalClasses: 100,
|             AttendedClasses: 85,
|             Percentage: 85
|         },
|         Skills: ["HTML", "CSS", "JavaScript"],
|         RecentActivities: [
|             { Activity: "Quiz Completed", Date: ISODate("2026-10-22") }
|         ]
|     },
|     {
|         StudentID: 105,
|         Name: "Neha",
|         Department: "MCA",
|         Semester: 3,
|         Courses: ["MongoDB", "Python"],
|         Attendance: {
|             TotalClasses: 100,
|             AttendedClasses: 60,
|             Percentage: 60
|         },
|         Skills: ["Python", "MongoDB"],
|         RecentActivities: [
|             { Activity: "Assignment Submitted", Date: ISODate("2026-10-24") }
|         ]
|     }
| ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae44871ee7e2dac72a3e9d0'),
    '1': ObjectId('6ae44871ee7e2dac72a3e9d1'),
    '2': ObjectId('6ae44871ee7e2dac72a3e9d2'),
    '3': ObjectId('6ae44871ee7e2dac72a3e9d3'),
    '4': ObjectId('6ae44871ee7e2dac72a3e9d4')
  }
}
StudentActivityDB> db.Students.find()
[
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d0'),
    StudentID: 101,
    Name: 'Rohit',
    Department: 'BCA',
    Semester: 5,
    Courses: [ 'MongoDB', 'Python', 'Java' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 90, Percentage: 90 },
    Skills: [ 'Python', 'JavaScript', 'MongoDB' ],
    RecentActivities: [
      {
        Activity: 'Assignment Submitted',
        Date: ISODate('2026-10-20T00:00:00.000Z')
      },
      {
        Activity: 'Quiz Completed',
        Date: ISODate('2026-10-25T00:00:00.000Z')
      }
    ]
  },
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d1'),
    StudentID: 102,
    Name: 'Amit',
    Department: 'BCA',
    Semester: 5,
    Courses: [ 'Python', 'C++' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 75, Percentage: 75 },
    Skills: [ 'Python', 'C++' ],
    RecentActivities: [
      {
        Activity: 'Assignment Submitted',
        Date: ISODate('2026-10-18T00:00:00.000Z')
      }
    ]
  },
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d2'),
    StudentID: 103,
    Name: 'Rahul',
    Department: 'MCA',
    Semester: 3,
    Courses: [ 'MongoDB', 'Java' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 95, Percentage: 95 },
    Skills: [ 'Java', 'MongoDB' ],
    RecentActivities: [
      {
        Activity: 'Project Completed',
        Date: ISODate('2026-10-26T00:00:00.000Z')
      }
    ]
  },
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d3'),
    StudentID: 104,
    Name: 'Priya',
    Department: 'BCA',
    Semester: 5,
    Courses: [ 'Python', 'Web Development' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 85, Percentage: 85 },
    Skills: [ 'HTML', 'CSS', 'JavaScript' ],
    RecentActivities: [
      {
        Activity: 'Quiz Completed',
        Date: ISODate('2026-10-22T00:00:00.000Z')
      }
    ]
  },
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d4'),
    StudentID: 105,
    Name: 'Neha',
    Department: 'MCA',
    Semester: 3,
    Courses: [ 'MongoDB', 'Python' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 60, Percentage: 60 },
    Skills: [ 'Python', 'MongoDB' ],
    RecentActivities: [
      {
        Activity: 'Assignment Submitted',
        Date: ISODate('2026-10-24T00:00:00.000Z')
      }
    ]
  }
]
StudentActivityDB> db.Students.find({ Courses: "MongoDB" })
[
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d0'),
    StudentID: 101,
    Name: 'Rohit',
    Department: 'BCA',
    Semester: 5,
    Courses: [ 'MongoDB', 'Python', 'Java' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 90, Percentage: 90 },
    Skills: [ 'Python', 'JavaScript', 'MongoDB' ],
    RecentActivities: [
      {
        Activity: 'Assignment Submitted',
        Date: ISODate('2026-10-20T00:00:00.000Z')
      },
      {
        Activity: 'Quiz Completed',
        Date: ISODate('2026-10-25T00:00:00.000Z')
      }
    ]
  },
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d2'),
    StudentID: 103,
    Name: 'Rahul',
    Department: 'MCA',
    Semester: 3,
    Courses: [ 'MongoDB', 'Java' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 95, Percentage: 95 },
    Skills: [ 'Java', 'MongoDB' ],
    RecentActivities: [
      {
        Activity: 'Project Completed',
        Date: ISODate('2026-10-26T00:00:00.000Z')
      }
    ]
  },
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d4'),
    StudentID: 105,
    Name: 'Neha',
    Department: 'MCA',
    Semester: 3,
    Courses: [ 'MongoDB', 'Python' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 60, Percentage: 60 },
    Skills: [ 'Python', 'MongoDB' ],
    RecentActivities: [
      {
        Activity: 'Assignment Submitted',
        Date: ISODate('2026-10-24T00:00:00.000Z')
      }
    ]
  }
]
StudentActivityDB> db.Students.find({ "Attendance.Percentage": { $gt: 80 } })
[
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d0'),
    StudentID: 101,
    Name: 'Rohit',
    Department: 'BCA',
    Semester: 5,
    Courses: [ 'MongoDB', 'Python', 'Java' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 90, Percentage: 90 },
    Skills: [ 'Python', 'JavaScript', 'MongoDB' ],
    RecentActivities: [
      {
        Activity: 'Assignment Submitted',
        Date: ISODate('2026-10-20T00:00:00.000Z')
      },
      {
        Activity: 'Quiz Completed',
        Date: ISODate('2026-10-25T00:00:00.000Z')
      }
    ]
  },
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d2'),
    StudentID: 103,
    Name: 'Rahul',
    Department: 'MCA',
    Semester: 3,
    Courses: [ 'MongoDB', 'Java' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 95, Percentage: 95 },
    Skills: [ 'Java', 'MongoDB' ],
    RecentActivities: [
      {
        Activity: 'Project Completed',
        Date: ISODate('2026-10-26T00:00:00.000Z')
      }
    ]
  },
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d3'),
    StudentID: 104,
    Name: 'Priya',
    Department: 'BCA',
    Semester: 5,
    Courses: [ 'Python', 'Web Development' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 85, Percentage: 85 },
    Skills: [ 'HTML', 'CSS', 'JavaScript' ],
    RecentActivities: [
      {
        Activity: 'Quiz Completed',
        Date: ISODate('2026-10-22T00:00:00.000Z')
      }
    ]
  }
]
StudentActivityDB> db.Students.find({ Skills: "Python" })
[
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d0'),
    StudentID: 101,
    Name: 'Rohit',
    Department: 'BCA',
    Semester: 5,
    Courses: [ 'MongoDB', 'Python', 'Java' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 90, Percentage: 90 },
    Skills: [ 'Python', 'JavaScript', 'MongoDB' ],
    RecentActivities: [
      {
        Activity: 'Assignment Submitted',
        Date: ISODate('2026-10-20T00:00:00.000Z')
      },
      {
        Activity: 'Quiz Completed',
        Date: ISODate('2026-10-25T00:00:00.000Z')
      }
    ]
  },
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d1'),
    StudentID: 102,
    Name: 'Amit',
    Department: 'BCA',
    Semester: 5,
    Courses: [ 'Python', 'C++' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 75, Percentage: 75 },
    Skills: [ 'Python', 'C++' ],
    RecentActivities: [
      {
        Activity: 'Assignment Submitted',
        Date: ISODate('2026-10-18T00:00:00.000Z')
      }
    ]
  },
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d4'),
    StudentID: 105,
    Name: 'Neha',
    Department: 'MCA',
    Semester: 3,
    Courses: [ 'MongoDB', 'Python' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 60, Percentage: 60 },
    Skills: [ 'Python', 'MongoDB' ],
    RecentActivities: [
      {
        Activity: 'Assignment Submitted',
        Date: ISODate('2026-10-24T00:00:00.000Z')
      }
    ]
  }
]
StudentActivityDB> db.Students.find({ "RecentActivities.Activity": "Assignment Submitted" })
[
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d0'),
    StudentID: 101,
    Name: 'Rohit',
    Department: 'BCA',
    Semester: 5,
    Courses: [ 'MongoDB', 'Python', 'Java' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 90, Percentage: 90 },
    Skills: [ 'Python', 'JavaScript', 'MongoDB' ],
    RecentActivities: [
      {
        Activity: 'Assignment Submitted',
        Date: ISODate('2026-10-20T00:00:00.000Z')
      },
      {
        Activity: 'Quiz Completed',
        Date: ISODate('2026-10-25T00:00:00.000Z')
      }
    ]
  },
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d1'),
    StudentID: 102,
    Name: 'Amit',
    Department: 'BCA',
    Semester: 5,
    Courses: [ 'Python', 'C++' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 75, Percentage: 75 },
    Skills: [ 'Python', 'C++' ],
    RecentActivities: [
      {
        Activity: 'Assignment Submitted',
        Date: ISODate('2026-10-18T00:00:00.000Z')
      }
    ]
  },
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d4'),
    StudentID: 105,
    Name: 'Neha',
    Department: 'MCA',
    Semester: 3,
    Courses: [ 'MongoDB', 'Python' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 60, Percentage: 60 },
    Skills: [ 'Python', 'MongoDB' ],
    RecentActivities: [
      {
        Activity: 'Assignment Submitted',
        Date: ISODate('2026-10-24T00:00:00.000Z')
      }
    ]
  }
]
StudentActivityDB> db.Students.find({ "RecentActivities.Activity": "Project Completed" })
[
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d2'),
    StudentID: 103,
    Name: 'Rahul',
    Department: 'MCA',
    Semester: 3,
    Courses: [ 'MongoDB', 'Java' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 95, Percentage: 95 },
    Skills: [ 'Java', 'MongoDB' ],
    RecentActivities: [
      {
        Activity: 'Project Completed',
        Date: ISODate('2026-10-26T00:00:00.000Z')
      }
    ]
  }
]
StudentActivityDB> db.Students.find({ "Attendance.Percentage": { $lt: 75 } })
[
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d4'),
    StudentID: 105,
    Name: 'Neha',
    Department: 'MCA',
    Semester: 3,
    Courses: [ 'MongoDB', 'Python' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 60, Percentage: 60 },
    Skills: [ 'Python', 'MongoDB' ],
    RecentActivities: [
      {
        Activity: 'Assignment Submitted',
        Date: ISODate('2026-10-24T00:00:00.000Z')
      }
    ]
  }
]
StudentActivityDB> db.Students.find({
|     Courses: "MongoDB",
|     "Attendance.Percentage": { $gt: 80 }
| })
[
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d0'),
    StudentID: 101,
    Name: 'Rohit',
    Department: 'BCA',
    Semester: 5,
    Courses: [ 'MongoDB', 'Python', 'Java' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 90, Percentage: 90 },
    Skills: [ 'Python', 'JavaScript', 'MongoDB' ],
    RecentActivities: [
      {
        Activity: 'Assignment Submitted',
        Date: ISODate('2026-10-20T00:00:00.000Z')
      },
      {
        Activity: 'Quiz Completed',
        Date: ISODate('2026-10-25T00:00:00.000Z')
      }
    ]
  },
  {
    _id: ObjectId('6ae44871ee7e2dac72a3e9d2'),
    StudentID: 103,
    Name: 'Rahul',
    Department: 'MCA',
    Semester: 3,
    Courses: [ 'MongoDB', 'Java' ],
    Attendance: { TotalClasses: 100, AttendedClasses: 95, Percentage: 95 },
    Skills: [ 'Java', 'MongoDB' ],
    RecentActivities: [
      {
        Activity: 'Project Completed',
        Date: ISODate('2026-10-26T00:00:00.000Z')
      }
    ]
  }
]
StudentActivityDB> 
```


## Question 2
Develop an Event Logging System that records login, logout, failed-login, file-upload, and password-change events. Use MongoDB queries to identify repeated failed-login attempts and frequently occurring events.

### Commands and Output

```javascript
StudentActivityDB> use EventLogDB
switched to db EventLogDB
EventLogDB> db.createCollection("Events")
{ ok: 1 }
EventLogDB> db.Events.insertMany([
|     {
|         EventID: 101,
|         UserID: 1,
|         Username: "Rohit",
|         EventType: "login",
|         Timestamp: ISODate("2026-10-25T09:00:00Z"),
|         IPAddress: "192.168.1.10"
|     },
|     {
|         EventID: 102,
|         UserID: 1,
|         Username: "Rohit",
|         EventType: "logout",
|         Timestamp: ISODate("2026-10-25T10:00:00Z"),
|         IPAddress: "192.168.1.10"
|     },
|     {
|         EventID: 103,
|         UserID: 2,
|         Username: "Amit",
|         EventType: "failed-login",
|         Timestamp: ISODate("2026-10-25T09:15:00Z"),
|         IPAddress: "192.168.1.20"
|     },
|     {
|         EventID: 104,
|         UserID: 2,
|         Username: "Amit",
|         EventType: "failed-login",
|         Timestamp: ISODate("2026-10-25T09:16:00Z"),
|         IPAddress: "192.168.1.20"
|     },
|     {
|         EventID: 105,
|         UserID: 2,
|         Username: "Amit",
|         EventType: "failed-login",
|         Timestamp: ISODate("2026-10-25T09:17:00Z"),
|         IPAddress: "192.168.1.20"
|     },
|     {
|         EventID: 106,
|         UserID: 3,
|         Username: "Rahul",
|         EventType: "file-upload",
|         Timestamp: ISODate("2026-10-25T11:00:00Z"),
|         IPAddress: "192.168.1.30"
|     },
|     {
|         EventID: 107,
|         UserID: 1,
|         Username: "Rohit",
|         EventType: "password-change",
|         Timestamp: ISODate("2026-10-25T12:00:00Z"),
|         IPAddress: "192.168.1.10"
|     },
|     {
|         EventID: 108,
|         UserID: 3,
|         Username: "Rahul",
|         EventType: "login",
|         Timestamp: ISODate("2026-10-25T13:00:00Z"),
|         IPAddress: "192.168.1.30"
|     },
|     {
|         EventID: 109,
|         UserID: 2,
|         Username: "Amit",
|         EventType: "failed-login",
|         Timestamp: ISODate("2026-10-25T14:00:00Z"),
|         IPAddress: "192.168.1.20"
|     },
|     {
|         EventID: 110,
|         UserID: 3,
|         Username: "Rahul",
|         EventType: "file-upload",
|         Timestamp: ISODate("2026-10-25T15:00:00Z"),
|         IPAddress: "192.168.1.30"
|     }
| ])
| 
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae449adee7e2dac72a3e9d5'),
    '1': ObjectId('6ae449adee7e2dac72a3e9d6'),
    '2': ObjectId('6ae449adee7e2dac72a3e9d7'),
    '3': ObjectId('6ae449adee7e2dac72a3e9d8'),
    '4': ObjectId('6ae449adee7e2dac72a3e9d9'),
    '5': ObjectId('6ae449adee7e2dac72a3e9da'),
    '6': ObjectId('6ae449adee7e2dac72a3e9db'),
    '7': ObjectId('6ae449adee7e2dac72a3e9dc'),
    '8': ObjectId('6ae449adee7e2dac72a3e9dd'),
    '9': ObjectId('6ae449adee7e2dac72a3e9de')
  }
}
EventLogDB> db.Events.find()
[
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9d5'),
    EventID: 101,
    UserID: 1,
    Username: 'Rohit',
    EventType: 'login',
    Timestamp: ISODate('2026-10-25T09:00:00.000Z'),
    IPAddress: '192.168.1.10'
  },
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9d6'),
    EventID: 102,
    UserID: 1,
    Username: 'Rohit',
    EventType: 'logout',
    Timestamp: ISODate('2026-10-25T10:00:00.000Z'),
    IPAddress: '192.168.1.10'
  },
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9d7'),
    EventID: 103,
    UserID: 2,
    Username: 'Amit',
    EventType: 'failed-login',
    Timestamp: ISODate('2026-10-25T09:15:00.000Z'),
    IPAddress: '192.168.1.20'
  },
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9d8'),
    EventID: 104,
    UserID: 2,
    Username: 'Amit',
    EventType: 'failed-login',
    Timestamp: ISODate('2026-10-25T09:16:00.000Z'),
    IPAddress: '192.168.1.20'
  },
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9d9'),
    EventID: 105,
    UserID: 2,
    Username: 'Amit',
    EventType: 'failed-login',
    Timestamp: ISODate('2026-10-25T09:17:00.000Z'),
    IPAddress: '192.168.1.20'
  },
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9da'),
    EventID: 106,
    UserID: 3,
    Username: 'Rahul',
    EventType: 'file-upload',
    Timestamp: ISODate('2026-10-25T11:00:00.000Z'),
    IPAddress: '192.168.1.30'
  },
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9db'),
    EventID: 107,
    UserID: 1,
    Username: 'Rohit',
    EventType: 'password-change',
    Timestamp: ISODate('2026-10-25T12:00:00.000Z'),
    IPAddress: '192.168.1.10'
  },
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9dc'),
    EventID: 108,
    UserID: 3,
    Username: 'Rahul',
    EventType: 'login',
    Timestamp: ISODate('2026-10-25T13:00:00.000Z'),
    IPAddress: '192.168.1.30'
  },
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9dd'),
    EventID: 109,
    UserID: 2,
    Username: 'Amit',
    EventType: 'failed-login',
    Timestamp: ISODate('2026-10-25T14:00:00.000Z'),
    IPAddress: '192.168.1.20'
  },
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9de'),
    EventID: 110,
    UserID: 3,
    Username: 'Rahul',
    EventType: 'file-upload',
    Timestamp: ISODate('2026-10-25T15:00:00.000Z'),
    IPAddress: '192.168.1.30'
  }
]
EventLogDB> db.Events.find({
|     EventType: "failed-login"
| })
[
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9d7'),
    EventID: 103,
    UserID: 2,
    Username: 'Amit',
    EventType: 'failed-login',
    Timestamp: ISODate('2026-10-25T09:15:00.000Z'),
    IPAddress: '192.168.1.20'
  },
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9d8'),
    EventID: 104,
    UserID: 2,
    Username: 'Amit',
    EventType: 'failed-login',
    Timestamp: ISODate('2026-10-25T09:16:00.000Z'),
    IPAddress: '192.168.1.20'
  },
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9d9'),
    EventID: 105,
    UserID: 2,
    Username: 'Amit',
    EventType: 'failed-login',
    Timestamp: ISODate('2026-10-25T09:17:00.000Z'),
    IPAddress: '192.168.1.20'
  },
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9dd'),
    EventID: 109,
    UserID: 2,
    Username: 'Amit',
    EventType: 'failed-login',
    Timestamp: ISODate('2026-10-25T14:00:00.000Z'),
    IPAddress: '192.168.1.20'
  }
]
EventLogDB> db.Events.aggregate([
|     {
|         $match: {
|             EventType: "failed-login"
|         }
|     },
|     {
|         $group: {
|             _id: "$Username",
|             FailedAttempts: { $sum: 1 }
|         }
|     },
|     {
|         $match: {
|             FailedAttempts: { $gt: 1 }
|         }
|     }
| ])
[ { _id: 'Amit', FailedAttempts: 4 } ]
EventLogDB> db.Events.aggregate([
|     {
|         $group: {
|             _id: "$EventType",
|             TotalEvents: { $sum: 1 }
|         }
|     },
|     {
|         $sort: {
|             TotalEvents: -1
|         }
|     }
| ])
[
  { _id: 'failed-login', TotalEvents: 4 },
  { _id: 'login', TotalEvents: 2 },
  { _id: 'file-upload', TotalEvents: 2 },
  { _id: 'logout', TotalEvents: 1 },
  { _id: 'password-change', TotalEvents: 1 }
]
EventLogDB> db.Events.aggregate([
|     {
|         $match: {
|             EventType: "failed-login"
|         }
|     },
|     {
|         $group: {
|             _id: "$UserID",
|             Username: { $first: "$Username" },
|             FailedAttempts: { $sum: 1 }
|         }
|     },
|     {
|         $match: {
|             FailedAttempts: { $gt: 1 }
|         }
|     }
| ])
| 
[ { _id: 2, Username: 'Amit', FailedAttempts: 4 } ]
EventLogDB> db.Events.find({
|     EventType: "login"
| })
| 
[
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9d5'),
    EventID: 101,
    UserID: 1,
    Username: 'Rohit',
    EventType: 'login',
    Timestamp: ISODate('2026-10-25T09:00:00.000Z'),
    IPAddress: '192.168.1.10'
  },
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9dc'),
    EventID: 108,
    UserID: 3,
    Username: 'Rahul',
    EventType: 'login',
    Timestamp: ISODate('2026-10-25T13:00:00.000Z'),
    IPAddress: '192.168.1.30'
  }
]
EventLogDB> db.Events.find({
|     EventType: "file-upload"
| })
[
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9da'),
    EventID: 106,
    UserID: 3,
    Username: 'Rahul',
    EventType: 'file-upload',
    Timestamp: ISODate('2026-10-25T11:00:00.000Z'),
    IPAddress: '192.168.1.30'
  },
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9de'),
    EventID: 110,
    UserID: 3,
    Username: 'Rahul',
    EventType: 'file-upload',
    Timestamp: ISODate('2026-10-25T15:00:00.000Z'),
    IPAddress: '192.168.1.30'
  }
]
EventLogDB> db.Events.find({
|     EventType: "password-change"
| })
[
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9db'),
    EventID: 107,
    UserID: 1,
    Username: 'Rohit',
    EventType: 'password-change',
    Timestamp: ISODate('2026-10-25T12:00:00.000Z'),
    IPAddress: '192.168.1.10'
  }
]
EventLogDB> db.Events.find({
|     Username: "Amit"
| })
[
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9d7'),
    EventID: 103,
    UserID: 2,
    Username: 'Amit',
    EventType: 'failed-login',
    Timestamp: ISODate('2026-10-25T09:15:00.000Z'),
    IPAddress: '192.168.1.20'
  },
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9d8'),
    EventID: 104,
    UserID: 2,
    Username: 'Amit',
    EventType: 'failed-login',
    Timestamp: ISODate('2026-10-25T09:16:00.000Z'),
    IPAddress: '192.168.1.20'
  },
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9d9'),
    EventID: 105,
    UserID: 2,
    Username: 'Amit',
    EventType: 'failed-login',
    Timestamp: ISODate('2026-10-25T09:17:00.000Z'),
    IPAddress: '192.168.1.20'
  },
  {
    _id: ObjectId('6ae449adee7e2dac72a3e9dd'),
    EventID: 109,
    UserID: 2,
    Username: 'Amit',
    EventType: 'failed-login',
    Timestamp: ISODate('2026-10-25T14:00:00.000Z'),
    IPAddress: '192.168.1.20'
  }
]
EventLogDB> 

```


## Question 3
Create a Mini Blogging Platform using MongoDB where each blog contains author, category, tags, comments, and publication information. Retrieve blogs using different combinations of tags and categories.

### Commands and Output

```javascript
test> use BlogDB
switched to db BlogDB
BlogDB> db.createCollection("Blogs")
{ ok: 1 }
BlogDB> db.Blogs.insertMany([
|     {
|         BlogID: 1,
|         Title: "Introduction to MongoDB",
|         Author: "Rohit",
|         Category: "Technology",
|         Tags: ["MongoDB", "Database"],
|         Comments: [
|             { User: "Amit", Message: "Great blog!" }
|         ],
|         Published: true,
|         PublishDate: ISODate("2026-10-20")
|     },
|     {
|         BlogID: 2,
|         Title: "Learning Python",
|         Author: "Amit",
|         Category: "Programming",
|         Tags: ["Python", "Coding"],
|         Comments: [
|             { User: "Rahul", Message: "Very useful!" }
|         ],
|         Published: true,
|         PublishDate: ISODate("2026-10-22")
|     },
|     {
|         BlogID: 3,
|         Title: "Web Development",
|         Author: "Rahul",
|         Category: "Technology",
|         Tags: ["HTML", "CSS"],
|         Comments: [],
|         Published: false,
|         PublishDate: ISODate("2026-10-25")
|     }
| ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae44b6af2dc03fbb87e0aa6'),
    '1': ObjectId('6ae44b6af2dc03fbb87e0aa7'),
    '2': ObjectId('6ae44b6af2dc03fbb87e0aa8')
  }
}
BlogDB> db.Blogs.find()
[
  {
    _id: ObjectId('6ae44b6af2dc03fbb87e0aa6'),
    BlogID: 1,
    Title: 'Introduction to MongoDB',
    Author: 'Rohit',
    Category: 'Technology',
    Tags: [ 'MongoDB', 'Database' ],
    Comments: [ { User: 'Amit', Message: 'Great blog!' } ],
    Published: true,
    PublishDate: ISODate('2026-10-20T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae44b6af2dc03fbb87e0aa7'),
    BlogID: 2,
    Title: 'Learning Python',
    Author: 'Amit',
    Category: 'Programming',
    Tags: [ 'Python', 'Coding' ],
    Comments: [ { User: 'Rahul', Message: 'Very useful!' } ],
    Published: true,
    PublishDate: ISODate('2026-10-22T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae44b6af2dc03fbb87e0aa8'),
    BlogID: 3,
    Title: 'Web Development',
    Author: 'Rahul',
    Category: 'Technology',
    Tags: [ 'HTML', 'CSS' ],
    Comments: [],
    Published: false,
    PublishDate: ISODate('2026-10-25T00:00:00.000Z')
  }
]
BlogDB> db.Blogs.find({ Category: "Technology" })
[
  {
    _id: ObjectId('6ae44b6af2dc03fbb87e0aa6'),
    BlogID: 1,
    Title: 'Introduction to MongoDB',
    Author: 'Rohit',
    Category: 'Technology',
    Tags: [ 'MongoDB', 'Database' ],
    Comments: [ { User: 'Amit', Message: 'Great blog!' } ],
    Published: true,
    PublishDate: ISODate('2026-10-20T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae44b6af2dc03fbb87e0aa8'),
    BlogID: 3,
    Title: 'Web Development',
    Author: 'Rahul',
    Category: 'Technology',
    Tags: [ 'HTML', 'CSS' ],
    Comments: [],
    Published: false,
    PublishDate: ISODate('2026-10-25T00:00:00.000Z')
  }
]
BlogDB> db.Blogs.find({ Tags: "Python" })
[
  {
    _id: ObjectId('6ae44b6af2dc03fbb87e0aa7'),
    BlogID: 2,
    Title: 'Learning Python',
    Author: 'Amit',
    Category: 'Programming',
    Tags: [ 'Python', 'Coding' ],
    Comments: [ { User: 'Rahul', Message: 'Very useful!' } ],
    Published: true,
    PublishDate: ISODate('2026-10-22T00:00:00.000Z')
  }
]
BlogDB> db.Blogs.find({
|     Category: "Technology",
|     Tags: "MongoDB"
| })
[
  {
    _id: ObjectId('6ae44b6af2dc03fbb87e0aa6'),
    BlogID: 1,
    Title: 'Introduction to MongoDB',
    Author: 'Rohit',
    Category: 'Technology',
    Tags: [ 'MongoDB', 'Database' ],
    Comments: [ { User: 'Amit', Message: 'Great blog!' } ],
    Published: true,
    PublishDate: ISODate('2026-10-20T00:00:00.000Z')
  }
]
BlogDB> db.Blogs.find({ Published: true })
[
  {
    _id: ObjectId('6ae44b6af2dc03fbb87e0aa6'),
    BlogID: 1,
    Title: 'Introduction to MongoDB',
    Author: 'Rohit',
    Category: 'Technology',
    Tags: [ 'MongoDB', 'Database' ],
    Comments: [ { User: 'Amit', Message: 'Great blog!' } ],
    Published: true,
    PublishDate: ISODate('2026-10-20T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae44b6af2dc03fbb87e0aa7'),
    BlogID: 2,
    Title: 'Learning Python',
    Author: 'Amit',
    Category: 'Programming',
    Tags: [ 'Python', 'Coding' ],
    Comments: [ { User: 'Rahul', Message: 'Very useful!' } ],
    Published: true,
    PublishDate: ISODate('2026-10-22T00:00:00.000Z')
  }
]
BlogDB> 
```



## Question 4
Design a Flexible Product Catalog where laptops, mobiles, and cameras have different sets of attributes. Store them in a common collection and write queries to search category-specific properties.

### Commands and Output

```javascript
test> use ProductDB
switched to db ProductDB
ProductDB> db.createCollection("Products")
{ ok: 1 }
ProductDB> db.Products.insertMany([
|     {
|         ProductID: 101,
|         Name: "Dell Laptop",
|         Category: "Laptop",
|         Price: 55000,
|         Attributes: {
|             RAM: "16GB",
|             Storage: "512GB SSD",
|             Processor: "Intel i5"
|         }
|     },
|     {
|         ProductID: 102,
|         Name: "HP Laptop",
|         Category: "Laptop",
|         Price: 60000,
|         Attributes: {
|             RAM: "8GB",
|             Storage: "1TB SSD",
|             Processor: "Intel i7"
|         }
|     },
|     {
|         ProductID: 103,
|         Name: "Samsung Mobile",
|         Category: "Mobile",
|         Price: 25000,
|         Attributes: {
|             RAM: "8GB",
|             Storage: "128GB",
|             Battery: "5000mAh"
|         }
|     },
|     {
|         ProductID: 104,
|         Name: "iPhone",
|         Category: "Mobile",
|         Price: 70000,
|         Attributes: {
|             RAM: "6GB",
|             Storage: "256GB",
|             Battery: "4000mAh"
|         }
|     },
|     {
|         ProductID: 105,
|         Name: "Canon Camera",
|         Category: "Camera",
|         Price: 45000,
|         Attributes: {
|             Megapixels: "24MP",
|             Lens: "18-55mm",
|             Type: "DSLR"
|         }
|     }
| ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae44c4f5a472e6c3b05fede'),
    '1': ObjectId('6ae44c4f5a472e6c3b05fedf'),
    '2': ObjectId('6ae44c4f5a472e6c3b05fee0'),
    '3': ObjectId('6ae44c4f5a472e6c3b05fee1'),
    '4': ObjectId('6ae44c4f5a472e6c3b05fee2')
  }
}
ProductDB> db.Products.find()
[
  {
    _id: ObjectId('6ae44c4f5a472e6c3b05fede'),
    ProductID: 101,
    Name: 'Dell Laptop',
    Category: 'Laptop',
    Price: 55000,
    Attributes: { RAM: '16GB', Storage: '512GB SSD', Processor: 'Intel i5' }
  },
  {
    _id: ObjectId('6ae44c4f5a472e6c3b05fedf'),
    ProductID: 102,
    Name: 'HP Laptop',
    Category: 'Laptop',
    Price: 60000,
    Attributes: { RAM: '8GB', Storage: '1TB SSD', Processor: 'Intel i7' }
  },
  {
    _id: ObjectId('6ae44c4f5a472e6c3b05fee0'),
    ProductID: 103,
    Name: 'Samsung Mobile',
    Category: 'Mobile',
    Price: 25000,
    Attributes: { RAM: '8GB', Storage: '128GB', Battery: '5000mAh' }
  },
  {
    _id: ObjectId('6ae44c4f5a472e6c3b05fee1'),
    ProductID: 104,
    Name: 'iPhone',
    Category: 'Mobile',
    Price: 70000,
    Attributes: { RAM: '6GB', Storage: '256GB', Battery: '4000mAh' }
  },
  {
    _id: ObjectId('6ae44c4f5a472e6c3b05fee2'),
    ProductID: 105,
    Name: 'Canon Camera',
    Category: 'Camera',
    Price: 45000,
    Attributes: { Megapixels: '24MP', Lens: '18-55mm', Type: 'DSLR' }
  }
]
ProductDB> db.Products.find({ Category: "Laptop" })
[
  {
    _id: ObjectId('6ae44c4f5a472e6c3b05fede'),
    ProductID: 101,
    Name: 'Dell Laptop',
    Category: 'Laptop',
    Price: 55000,
    Attributes: { RAM: '16GB', Storage: '512GB SSD', Processor: 'Intel i5' }
  },
  {
    _id: ObjectId('6ae44c4f5a472e6c3b05fedf'),
    ProductID: 102,
    Name: 'HP Laptop',
    Category: 'Laptop',
    Price: 60000,
    Attributes: { RAM: '8GB', Storage: '1TB SSD', Processor: 'Intel i7' }
  }
]
ProductDB> db.Products.find({
|     Category: "Laptop",
|     "Attributes.RAM": "16GB"
| })
[
  {
    _id: ObjectId('6ae44c4f5a472e6c3b05fede'),
    ProductID: 101,
    Name: 'Dell Laptop',
    Category: 'Laptop',
    Price: 55000,
    Attributes: { RAM: '16GB', Storage: '512GB SSD', Processor: 'Intel i5' }
  }
]
ProductDB> db.Products.find({
|     Category: "Mobile",
|     "Attributes.Storage": "128GB"
| })
[
  {
    _id: ObjectId('6ae44c4f5a472e6c3b05fee0'),
    ProductID: 103,
    Name: 'Samsung Mobile',
    Category: 'Mobile',
    Price: 25000,
    Attributes: { RAM: '8GB', Storage: '128GB', Battery: '5000mAh' }
  }
]
ProductDB> db.Products.find({
|     Category: "Camera",
|     "Attributes.Type": "DSLR"
| })
[
  {
    _id: ObjectId('6ae44c4f5a472e6c3b05fee2'),
    ProductID: 105,
    Name: 'Canon Camera',
    Category: 'Camera',
    Price: 45000,
    Attributes: { Megapixels: '24MP', Lens: '18-55mm', Type: 'DSLR' }
  }
]
ProductDB> db.Products.find({
|     Price: { $lt: 50000 }
| })
[
  {
    _id: ObjectId('6ae44c4f5a472e6c3b05fee0'),
    ProductID: 103,
    Name: 'Samsung Mobile',
    Category: 'Mobile',
    Price: 25000,
    Attributes: { RAM: '8GB', Storage: '128GB', Battery: '5000mAh' }
  },
  {
    _id: ObjectId('6ae44c4f5a472e6c3b05fee2'),
    ProductID: 105,
    Name: 'Canon Camera',
    Category: 'Camera',
    Price: 45000,
    Attributes: { Megapixels: '24MP', Lens: '18-55mm', Type: 'DSLR' }
  }
]
ProductDB> 

```



## Question 5
Develop an E-Commerce Order Management System containing customers, products, and orders. Write queries to retrieve a customer's complete purchase history and calculate order totals.

### Commands and Output

```javascript
test> use ECommerceDB
switched to db ECommerceDB
ECommerceDB> db.createCollection("Customers")
{ ok: 1 }
ECommerceDB> db.createCollection("Products")
{ ok: 1 }
ECommerceDB> db.createCollection("Orders")
{ ok: 1 }
ECommerceDB> db.Customers.insertMany([
|     { CustomerID: 1, Name: "Rohit", Email: "rohit@gmail.com" },
|     { CustomerID: 2, Name: "Amit", Email: "amit@gmail.com" },
|     { CustomerID: 3, Name: "Rahul", Email: "rahul@gmail.com" }
| ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae44d445f25992bdfdc0aa0'),
    '1': ObjectId('6ae44d445f25992bdfdc0aa1'),
    '2': ObjectId('6ae44d445f25992bdfdc0aa2')
  }
}
ECommerceDB> db.Products.insertMany([
|     { ProductID: 101, Name: "Laptop", Price: 50000 },
|     { ProductID: 102, Name: "Mobile", Price: 20000 },
|     { ProductID: 103, Name: "Headphones", Price: 2000 }
| ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae44d4e5f25992bdfdc0aa3'),
    '1': ObjectId('6ae44d4e5f25992bdfdc0aa4'),
    '2': ObjectId('6ae44d4e5f25992bdfdc0aa5')
  }
}
ECommerceDB> db.Orders.insertMany([
|     {
|         OrderID: 1,
|         CustomerID: 1,
|         Products: [
|             { ProductID: 101, Quantity: 1, Price: 50000 },
|             { ProductID: 103, Quantity: 2, Price: 2000 }
|         ],
|         OrderDate: ISODate("2026-10-20")
|     },
|     {
|         OrderID: 2,
|         CustomerID: 1,
|         Products: [
|             { ProductID: 102, Quantity: 1, Price: 20000 }
|         ],
|         OrderDate: ISODate("2026-10-25")
|     },
|     {
|         OrderID: 3,
|         CustomerID: 2,
|         Products: [
|             { ProductID: 103, Quantity: 3, Price: 2000 }
|         ],
|         OrderDate: ISODate("2026-10-26")
|     }
| ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae44d625f25992bdfdc0aa6'),
    '1': ObjectId('6ae44d625f25992bdfdc0aa7'),
    '2': ObjectId('6ae44d625f25992bdfdc0aa8')
  }
}
ECommerceDB> db.Customers.find()
[
  {
    _id: ObjectId('6ae44d445f25992bdfdc0aa0'),
    CustomerID: 1,
    Name: 'Rohit',
    Email: 'rohit@gmail.com'
  },
  {
    _id: ObjectId('6ae44d445f25992bdfdc0aa1'),
    CustomerID: 2,
    Name: 'Amit',
    Email: 'amit@gmail.com'
  },
  {
    _id: ObjectId('6ae44d445f25992bdfdc0aa2'),
    CustomerID: 3,
    Name: 'Rahul',
    Email: 'rahul@gmail.com'
  }
]
ECommerceDB> db.Products.find()
[
  {
    _id: ObjectId('6ae44d4e5f25992bdfdc0aa3'),
    ProductID: 101,
    Name: 'Laptop',
    Price: 50000
  },
  {
    _id: ObjectId('6ae44d4e5f25992bdfdc0aa4'),
    ProductID: 102,
    Name: 'Mobile',
    Price: 20000
  },
  {
    _id: ObjectId('6ae44d4e5f25992bdfdc0aa5'),
    ProductID: 103,
    Name: 'Headphones',
    Price: 2000
  }
]
ECommerceDB> db.Orders.find()
[
  {
    _id: ObjectId('6ae44d625f25992bdfdc0aa6'),
    OrderID: 1,
    CustomerID: 1,
    Products: [
      { ProductID: 101, Quantity: 1, Price: 50000 },
      { ProductID: 103, Quantity: 2, Price: 2000 }
    ],
    OrderDate: ISODate('2026-10-20T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae44d625f25992bdfdc0aa7'),
    OrderID: 2,
    CustomerID: 1,
    Products: [ { ProductID: 102, Quantity: 1, Price: 20000 } ],
    OrderDate: ISODate('2026-10-25T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae44d625f25992bdfdc0aa8'),
    OrderID: 3,
    CustomerID: 2,
    Products: [ { ProductID: 103, Quantity: 3, Price: 2000 } ],
    OrderDate: ISODate('2026-10-26T00:00:00.000Z')
  }
]
ECommerceDB> db.Orders.aggregate([
|     { $match: { CustomerID: 1 } },
|     {
|         $lookup: {
|             from: "Customers",
|             localField: "CustomerID",
|             foreignField: "CustomerID",
|             as: "CustomerDetails"
|         }
|     }
| ])
| 
[
  {
    _id: ObjectId('6ae44d625f25992bdfdc0aa6'),
    OrderID: 1,
    CustomerID: 1,
    Products: [
      { ProductID: 101, Quantity: 1, Price: 50000 },
      { ProductID: 103, Quantity: 2, Price: 2000 }
    ],
    OrderDate: ISODate('2026-10-20T00:00:00.000Z'),
    CustomerDetails: [
      {
        _id: ObjectId('6ae44d445f25992bdfdc0aa0'),
        CustomerID: 1,
        Name: 'Rohit',
        Email: 'rohit@gmail.com'
      }
    ]
  },
  {
    _id: ObjectId('6ae44d625f25992bdfdc0aa7'),
    OrderID: 2,
    CustomerID: 1,
    Products: [ { ProductID: 102, Quantity: 1, Price: 20000 } ],
    OrderDate: ISODate('2026-10-25T00:00:00.000Z'),
    CustomerDetails: [
      {
        _id: ObjectId('6ae44d445f25992bdfdc0aa0'),
        CustomerID: 1,
        Name: 'Rohit',
        Email: 'rohit@gmail.com'
      }
    ]
  }
]
ECommerceDB> db.Orders.aggregate([
|     { $unwind: "$Products" },
|     {
|         $group: {
|             _id: "$OrderID",
|             TotalAmount: {
|                 $sum: {
|                     $multiply: ["$Products.Quantity", "$Products.Price"]
|                 }
|             }
|         }
|     }
| ])
[
  { _id: 1, TotalAmount: 54000 },
  { _id: 2, TotalAmount: 20000 },
  { _id: 3, TotalAmount: 6000 }
]
ECommerceDB> db.Orders.aggregate([
|     { $unwind: "$Products" },
|     {
|         $group: {
|             _id: "$CustomerID",
|             TotalPurchase: {
|                 $sum: {
|                     $multiply: ["$Products.Quantity", "$Products.Price"]
|                 }
|             }
|         }
|     }
| ])
[ { _id: 1, TotalPurchase: 74000 }, { _id: 2, TotalPurchase: 6000 } ]
ECommerceDB> 


```



## Question 6
Create a Website Analytics System that stores page visits, user ID, device, browser, location, and timestamp. Use aggregation to identify the most visited pages and commonly used devices.

### Commands and Output

```javascript
test> use WebsiteAnalyticsDB
switched to db WebsiteAnalyticsDB
WebsiteAnalyticsDB> db.createCollection("PageVisits")
{ ok: 1 }
WebsiteAnalyticsDB> db.PageVisits.insertMany([
|     {
|         UserID: 101,
|         Page: "/home",
|         Device: "Mobile",
|         Browser: "Chrome",
|         Location: "Delhi",
|         Timestamp: ISODate("2026-10-20T09:00:00Z")
|     },
|     {
|         UserID: 102,
|         Page: "/products",
|         Device: "Desktop",
|         Browser: "Firefox",
|         Location: "Mumbai",
|         Timestamp: ISODate("2026-10-20T10:00:00Z")
|     },
|     {
|         UserID: 103,
|         Page: "/home",
|         Device: "Mobile",
|         Browser: "Chrome",
|         Location: "Delhi",
|         Timestamp: ISODate("2026-10-21T11:00:00Z")
|     },
|     {
|         UserID: 104,
|         Page: "/about",
|         Device: "Tablet",
|         Browser: "Safari",
|         Location: "Patna",
|         Timestamp: ISODate("2026-10-21T12:00:00Z")
|     },
|     {
|         UserID: 105,
|         Page: "/products",
|         Device: "Desktop",
|         Browser: "Chrome",
|         Location: "Mumbai",
|         Timestamp: ISODate("2026-10-22T13:00:00Z")
|     },
|     {
|         UserID: 106,
|         Page: "/home",
|         Device: "Mobile",
|         Browser: "Chrome",
|         Location: "Patna",
|         Timestamp: ISODate("2026-10-22T14:00:00Z")
|     }
| ])
| 
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae44ecb54e2179f8fd2c9e4'),
    '1': ObjectId('6ae44ecb54e2179f8fd2c9e5'),
    '2': ObjectId('6ae44ecb54e2179f8fd2c9e6'),
    '3': ObjectId('6ae44ecb54e2179f8fd2c9e7'),
    '4': ObjectId('6ae44ecb54e2179f8fd2c9e8'),
    '5': ObjectId('6ae44ecb54e2179f8fd2c9e9')
  }
}
WebsiteAnalyticsDB> db.PageVisits.find()
[
  {
    _id: ObjectId('6ae44ecb54e2179f8fd2c9e4'),
    UserID: 101,
    Page: '/home',
    Device: 'Mobile',
    Browser: 'Chrome',
    Location: 'Delhi',
    Timestamp: ISODate('2026-10-20T09:00:00.000Z')
  },
  {
    _id: ObjectId('6ae44ecb54e2179f8fd2c9e5'),
    UserID: 102,
    Page: '/products',
    Device: 'Desktop',
    Browser: 'Firefox',
    Location: 'Mumbai',
    Timestamp: ISODate('2026-10-20T10:00:00.000Z')
  },
  {
    _id: ObjectId('6ae44ecb54e2179f8fd2c9e6'),
    UserID: 103,
    Page: '/home',
    Device: 'Mobile',
    Browser: 'Chrome',
    Location: 'Delhi',
    Timestamp: ISODate('2026-10-21T11:00:00.000Z')
  },
  {
    _id: ObjectId('6ae44ecb54e2179f8fd2c9e7'),
    UserID: 104,
    Page: '/about',
    Device: 'Tablet',
    Browser: 'Safari',
    Location: 'Patna',
    Timestamp: ISODate('2026-10-21T12:00:00.000Z')
  },
  {
    _id: ObjectId('6ae44ecb54e2179f8fd2c9e8'),
    UserID: 105,
    Page: '/products',
    Device: 'Desktop',
    Browser: 'Chrome',
    Location: 'Mumbai',
    Timestamp: ISODate('2026-10-22T13:00:00.000Z')
  },
  {
    _id: ObjectId('6ae44ecb54e2179f8fd2c9e9'),
    UserID: 106,
    Page: '/home',
    Device: 'Mobile',
    Browser: 'Chrome',
    Location: 'Patna',
    Timestamp: ISODate('2026-10-22T14:00:00.000Z')
  }
]
WebsiteAnalyticsDB> db.PageVisits.aggregate([
|     {
|         $group: {
|             _id: "$Page",
|             TotalVisits: { $sum: 1 }
|         }
|     },
|     { $sort: { TotalVisits: -1 } }
| ])
[
  { _id: '/home', TotalVisits: 3 },
  { _id: '/products', TotalVisits: 2 },
  { _id: '/about', TotalVisits: 1 }
]
WebsiteAnalyticsDB> db.PageVisits.aggregate([
|     {
|         $group: {
|             _id: "$Device",
|             TotalVisits: { $sum: 1 }
|         }
|     },
|     { $sort: { TotalVisits: -1 } }
| ])
[
  { _id: 'Mobile', TotalVisits: 3 },
  { _id: 'Desktop', TotalVisits: 2 },
  { _id: 'Tablet', TotalVisits: 1 }
]
WebsiteAnalyticsDB> db.PageVisits.aggregate([
|     {
|         $group: {
|             _id: "$Browser",
|             TotalVisits: { $sum: 1 }
|         }
|     },
|     { $sort: { TotalVisits: -1 } }
| ])
| 
[
  { _id: 'Chrome', TotalVisits: 4 },
  { _id: 'Firefox', TotalVisits: 1 },
  { _id: 'Safari', TotalVisits: 1 }
]
WebsiteAnalyticsDB> db.PageVisits.find({ UserID: 101 })
[
  {
    _id: ObjectId('6ae44ecb54e2179f8fd2c9e4'),
    UserID: 101,
    Page: '/home',
    Device: 'Mobile',
    Browser: 'Chrome',
    Location: 'Delhi',
    Timestamp: ISODate('2026-10-20T09:00:00.000Z')
  }
]
WebsiteAnalyticsDB> 

```



## Question 7
Design a Content Management System for storing articles, authors, categories, tags, and publication status. Write queries to retrieve published and unpublished content according to different criteria.

### Commands and Output

```javascript
test> use CMSDB
switched to db CMSDB
CMSDB> db.createCollection("Articles")
{ ok: 1 }
CMSDB> db.Articles.insertMany([
|     {
|         ArticleID: 101,
|         Title: "Introduction to MongoDB",
|         Author: "Rohit",
|         Category: "Technology",
|         Tags: ["MongoDB", "Database"],
|         Status: "Published",
|         PublishDate: ISODate("2026-10-20")
|     },
|     {
|         ArticleID: 102,
|         Title: "Learning Python",
|         Author: "Amit",
|         Category: "Programming",
|         Tags: ["Python", "Coding"],
|         Status: "Published",
|         PublishDate: ISODate("2026-10-22")
|     },
|     {
|         ArticleID: 103,
|         Title: "Web Development",
|         Author: "Rahul",
|         Category: "Technology",
|         Tags: ["HTML", "CSS"],
|         Status: "Unpublished",
|         PublishDate: null
|     },
|     {
|         ArticleID: 104,
|         Title: "Java Basics",
|         Author: "Priya",
|         Category: "Programming",
|         Tags: ["Java", "Coding"],
|         Status: "Unpublished",
|         PublishDate: null
|     }
| ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae44fc2637cc80999811e9b'),
    '1': ObjectId('6ae44fc2637cc80999811e9c'),
    '2': ObjectId('6ae44fc2637cc80999811e9d'),
    '3': ObjectId('6ae44fc2637cc80999811e9e')
  }
}
CMSDB> db.Articles.find()
[
  {
    _id: ObjectId('6ae44fc2637cc80999811e9b'),
    ArticleID: 101,
    Title: 'Introduction to MongoDB',
    Author: 'Rohit',
    Category: 'Technology',
    Tags: [ 'MongoDB', 'Database' ],
    Status: 'Published',
    PublishDate: ISODate('2026-10-20T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae44fc2637cc80999811e9c'),
    ArticleID: 102,
    Title: 'Learning Python',
    Author: 'Amit',
    Category: 'Programming',
    Tags: [ 'Python', 'Coding' ],
    Status: 'Published',
    PublishDate: ISODate('2026-10-22T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae44fc2637cc80999811e9d'),
    ArticleID: 103,
    Title: 'Web Development',
    Author: 'Rahul',
    Category: 'Technology',
    Tags: [ 'HTML', 'CSS' ],
    Status: 'Unpublished',
    PublishDate: null
  },
  {
    _id: ObjectId('6ae44fc2637cc80999811e9e'),
    ArticleID: 104,
    Title: 'Java Basics',
    Author: 'Priya',
    Category: 'Programming',
    Tags: [ 'Java', 'Coding' ],
    Status: 'Unpublished',
    PublishDate: null
  }
]
CMSDB> db.Articles.find({ Status: "Published" })
[
  {
    _id: ObjectId('6ae44fc2637cc80999811e9b'),
    ArticleID: 101,
    Title: 'Introduction to MongoDB',
    Author: 'Rohit',
    Category: 'Technology',
    Tags: [ 'MongoDB', 'Database' ],
    Status: 'Published',
    PublishDate: ISODate('2026-10-20T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae44fc2637cc80999811e9c'),
    ArticleID: 102,
    Title: 'Learning Python',
    Author: 'Amit',
    Category: 'Programming',
    Tags: [ 'Python', 'Coding' ],
    Status: 'Published',
    PublishDate: ISODate('2026-10-22T00:00:00.000Z')
  }
]
CMSDB> db.Articles.find({ Status: "Unpublished" })
[
  {
    _id: ObjectId('6ae44fc2637cc80999811e9d'),
    ArticleID: 103,
    Title: 'Web Development',
    Author: 'Rahul',
    Category: 'Technology',
    Tags: [ 'HTML', 'CSS' ],
    Status: 'Unpublished',
    PublishDate: null
  },
  {
    _id: ObjectId('6ae44fc2637cc80999811e9e'),
    ArticleID: 104,
    Title: 'Java Basics',
    Author: 'Priya',
    Category: 'Programming',
    Tags: [ 'Java', 'Coding' ],
    Status: 'Unpublished',
    PublishDate: null
  }
]
CMSDB> db.Articles.find({ Category: "Technology" })
[
  {
    _id: ObjectId('6ae44fc2637cc80999811e9b'),
    ArticleID: 101,
    Title: 'Introduction to MongoDB',
    Author: 'Rohit',
    Category: 'Technology',
    Tags: [ 'MongoDB', 'Database' ],
    Status: 'Published',
    PublishDate: ISODate('2026-10-20T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae44fc2637cc80999811e9d'),
    ArticleID: 103,
    Title: 'Web Development',
    Author: 'Rahul',
    Category: 'Technology',
    Tags: [ 'HTML', 'CSS' ],
    Status: 'Unpublished',
    PublishDate: null
  }
]
CMSDB> db.Articles.find({ Author: "Rohit" })
[
  {
    _id: ObjectId('6ae44fc2637cc80999811e9b'),
    ArticleID: 101,
    Title: 'Introduction to MongoDB',
    Author: 'Rohit',
    Category: 'Technology',
    Tags: [ 'MongoDB', 'Database' ],
    Status: 'Published',
    PublishDate: ISODate('2026-10-20T00:00:00.000Z')
  }
]
CMSDB> db.Articles.find({ Tags: "Python" })
[
  {
    _id: ObjectId('6ae44fc2637cc80999811e9c'),
    ArticleID: 102,
    Title: 'Learning Python',
    Author: 'Amit',
    Category: 'Programming',
    Tags: [ 'Python', 'Coding' ],
    Status: 'Published',
    PublishDate: ISODate('2026-10-22T00:00:00.000Z')
  }
]
CMSDB> db.Articles.find({
|     Status: "Published",
|     Category: "Technology"
| })
[
  {
    _id: ObjectId('6ae44fc2637cc80999811e9b'),
    ArticleID: 101,
    Title: 'Introduction to MongoDB',
    Author: 'Rohit',
    Category: 'Technology',
    Tags: [ 'MongoDB', 'Database' ],
    Status: 'Published',
    PublishDate: ISODate('2026-10-20T00:00:00.000Z')
  }
]
CMSDB> db.Articles.find({
|     Status: "Unpublished",
|     Tags: "Coding"
| })
[
  {
    _id: ObjectId('6ae44fc2637cc80999811e9e'),
    ArticleID: 104,
    Title: 'Java Basics',
    Author: 'Priya',
    Category: 'Programming',
    Tags: [ 'Java', 'Coding' ],
    Status: 'Unpublished',
    PublishDate: null
  }
]
CMSDB> 
```



## Question 8
Implement a Shopping Cart System using embedded MongoDB documents. Perform operations for adding products, changing quantities, removing products, and calculating the cart value.
### Commands and Output

```javascript
test> use ShoppingCartDB
switched to db ShoppingCartDB
ShoppingCartDB> db.createCollection("Carts")
{ ok: 1 }
ShoppingCartDB> db.Carts.insertOne({
|     CartID: 101,
|     Customer: "Rohit",
|     Products: [
|         { Product: "Laptop", Price: 50000, Quantity: 1 },
|         { Product: "Mouse", Price: 500, Quantity: 2 }
|     ]
| })
{
  acknowledged: true,
  insertedId: ObjectId('6ae454df1c7ff50d77593269')
}
ShoppingCartDB> db.Carts.updateOne(
|     { CartID: 101 },
|     {
|         $push: {
|             Products: { Product: "Keyboard", Price: 1500, Quantity: 1 }
|         }
|     }
| )
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
ShoppingCartDB> db.Carts.updateOne(
|     { CartID: 101, "Products.Product": "Mouse" },
|     { $set: { "Products.$.Quantity": 3 } }
| )
| 
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
ShoppingCartDB> db.Carts.updateOne(
|     { CartID: 101 },
|     { $pull: { Products: { Product: "Keyboard" } } }
| )
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
ShoppingCartDB> db.Carts.find()
[
  {
    _id: ObjectId('6ae454df1c7ff50d77593269'),
    CartID: 101,
    Customer: 'Rohit',
    Products: [
      { Product: 'Laptop', Price: 50000, Quantity: 1 },
      { Product: 'Mouse', Price: 500, Quantity: 3 }
    ]
  }
]
ShoppingCartDB> db.Carts.aggregate([
|     { $match: { CartID: 101 } },
|     { $unwind: "$Products" },
|     {
|         $group: {
|             _id: "$CartID",
|             CartValue: {
|                 $sum: {
|                     $multiply: [
|                         "$Products.Price",
|                         "$Products.Quantity"
|                     ]
|                 }
|             }
|         }
|     }
| ])
[ { _id: 101, CartValue: 51500 } ]
ShoppingCartDB> 

```

## Question 9
Create a Product Review and Rating System in MongoDB. Store customer reviews and use aggregation to calculate the average rating and number of reviews for each product.
### Commands and Output

```javascript
test> use ProductReviewDB
switched to db ProductReviewDB
ProductReviewDB> db.createCollection("Reviews")
{ ok: 1 }
ProductReviewDB> db.Reviews.insertMany([
|     {
|         ProductID: 101,
|         ProductName: "Laptop",
|         Customer: "Rohit",
|         Rating: 5,
|         Review: "Excellent product"
|     },
|     {
|         ProductID: 101,
|         ProductName: "Laptop",
|         Customer: "Amit",
|         Rating: 4,
|         Review: "Good performance"
|     },
|     {
|         ProductID: 102,
|         ProductName: "Mobile",
|         Customer: "Rahul",
|         Rating: 5,
|         Review: "Great mobile"
|     },
|     {
|         ProductID: 102,
|         ProductName: "Mobile",
|         Customer: "Priya",
|         Rating: 3,
|         Review: "Average product"
|     },
|     {
|         ProductID: 103,
|         ProductName: "Headphones",
|         Customer: "Neha",
|         Rating: 4,
|         Review: "Good sound quality"
|     }
| ])
| 
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae4565351b5c88d6e72c58c'),
    '1': ObjectId('6ae4565351b5c88d6e72c58d'),
    '2': ObjectId('6ae4565351b5c88d6e72c58e'),
    '3': ObjectId('6ae4565351b5c88d6e72c58f'),
    '4': ObjectId('6ae4565351b5c88d6e72c590')
  }
}
ProductReviewDB> db.Reviews.find()
[
  {
    _id: ObjectId('6ae4565351b5c88d6e72c58c'),
    ProductID: 101,
    ProductName: 'Laptop',
    Customer: 'Rohit',
    Rating: 5,
    Review: 'Excellent product'
  },
  {
    _id: ObjectId('6ae4565351b5c88d6e72c58d'),
    ProductID: 101,
    ProductName: 'Laptop',
    Customer: 'Amit',
    Rating: 4,
    Review: 'Good performance'
  },
  {
    _id: ObjectId('6ae4565351b5c88d6e72c58e'),
    ProductID: 102,
    ProductName: 'Mobile',
    Customer: 'Rahul',
    Rating: 5,
    Review: 'Great mobile'
  },
  {
    _id: ObjectId('6ae4565351b5c88d6e72c58f'),
    ProductID: 102,
    ProductName: 'Mobile',
    Customer: 'Priya',
    Rating: 3,
    Review: 'Average product'
  },
  {
    _id: ObjectId('6ae4565351b5c88d6e72c590'),
    ProductID: 103,
    ProductName: 'Headphones',
    Customer: 'Neha',
    Rating: 4,
    Review: 'Good sound quality'
  }
]
ProductReviewDB> db.Reviews.aggregate([
|     {
|         $group: {
|             _id: "$ProductName",
|             AverageRating: { $avg: "$Rating" },
|             TotalReviews: { $sum: 1 }
|         }
|     }
| ])
[
  { _id: 'Headphones', AverageRating: 4, TotalReviews: 1 },
  { _id: 'Laptop', AverageRating: 4.5, TotalReviews: 2 },
  { _id: 'Mobile', AverageRating: 4, TotalReviews: 2 }
]
ProductReviewDB> db.Reviews.find({ ProductName: "Laptop" })
[
  {
    _id: ObjectId('6ae4565351b5c88d6e72c58c'),
    ProductID: 101,
    ProductName: 'Laptop',
    Customer: 'Rohit',
    Rating: 5,
    Review: 'Excellent product'
  },
  {
    _id: ObjectId('6ae4565351b5c88d6e72c58d'),
    ProductID: 101,
    ProductName: 'Laptop',
    Customer: 'Amit',
    Rating: 4,
    Review: 'Good performance'
  }
]
ProductReviewDB> db.Reviews.find({ Rating: { $gt: 4 } })
[
  {
    _id: ObjectId('6ae4565351b5c88d6e72c58c'),
    ProductID: 101,
    ProductName: 'Laptop',
    Customer: 'Rohit',
    Rating: 5,
    Review: 'Excellent product'
  },
  {
    _id: ObjectId('6ae4565351b5c88d6e72c58e'),
    ProductID: 102,
    ProductName: 'Mobile',
    Customer: 'Rahul',
    Rating: 5,
    Review: 'Great mobile'
  }
]
ProductReviewDB> 

```

## Question 10
Design an Inventory Monitoring System containing product stock, minimum stock level, supplier, and restocking date. Write queries to identify products that need immediate restocking.
### Commands and Output

```javascript
test> use InventoryDB
switched to db InventoryDB
InventoryDB> db.createCollection("Products")
{ ok: 1 }
InventoryDB> db.Products.insertMany([
|   {
|     ProductID: 101,
|     ProductName: "Laptop",
|     Stock: 5,
|     MinimumStock: 10,
|     Supplier: "Dell Suppliers",
|     RestockingDate: ISODate("2026-11-05")
|   },
|   {
|     ProductID: 102,
|     ProductName: "Mobile",
|     Stock: 25,
|     MinimumStock: 10,
|     Supplier: "Samsung Traders",
|     RestockingDate: ISODate("2026-11-10")
|   },
|   {
|     ProductID: 103,
|     ProductName: "Keyboard",
|     Stock: 3,
|     MinimumStock: 15,
|     Supplier: "HP Suppliers",
|     RestockingDate: ISODate("2026-11-02")
|   },
|   {
|     ProductID: 104,
|     ProductName: "Mouse",
|     Stock: 20,
|     MinimumStock: 5,
|     Supplier: "Logitech Traders",
|     RestockingDate: ISODate("2026-11-15")
|   },
|   {
|     ProductID: 105,
|     ProductName: "Headphones",
|     Stock: 4,
|     MinimumStock: 10,
|     Supplier: "Boat Suppliers",
|     RestockingDate: ISODate("2026-11-03")
|   }
| ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae4570914a4e91e441e7446'),
    '1': ObjectId('6ae4570914a4e91e441e7447'),
    '2': ObjectId('6ae4570914a4e91e441e7448'),
    '3': ObjectId('6ae4570914a4e91e441e7449'),
    '4': ObjectId('6ae4570914a4e91e441e744a')
  }
}
InventoryDB> db.Products.find()
[
  {
    _id: ObjectId('6ae4570914a4e91e441e7446'),
    ProductID: 101,
    ProductName: 'Laptop',
    Stock: 5,
    MinimumStock: 10,
    Supplier: 'Dell Suppliers',
    RestockingDate: ISODate('2026-11-05T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae4570914a4e91e441e7447'),
    ProductID: 102,
    ProductName: 'Mobile',
    Stock: 25,
    MinimumStock: 10,
    Supplier: 'Samsung Traders',
    RestockingDate: ISODate('2026-11-10T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae4570914a4e91e441e7448'),
    ProductID: 103,
    ProductName: 'Keyboard',
    Stock: 3,
    MinimumStock: 15,
    Supplier: 'HP Suppliers',
    RestockingDate: ISODate('2026-11-02T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae4570914a4e91e441e7449'),
    ProductID: 104,
    ProductName: 'Mouse',
    Stock: 20,
    MinimumStock: 5,
    Supplier: 'Logitech Traders',
    RestockingDate: ISODate('2026-11-15T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae4570914a4e91e441e744a'),
    ProductID: 105,
    ProductName: 'Headphones',
    Stock: 4,
    MinimumStock: 10,
    Supplier: 'Boat Suppliers',
    RestockingDate: ISODate('2026-11-03T00:00:00.000Z')
  }
]
InventoryDB> db.Products.find({
|   $expr: { $lte: ["$Stock", "$MinimumStock"] }
| })
| 
[
  {
    _id: ObjectId('6ae4570914a4e91e441e7446'),
    ProductID: 101,
    ProductName: 'Laptop',
    Stock: 5,
    MinimumStock: 10,
    Supplier: 'Dell Suppliers',
    RestockingDate: ISODate('2026-11-05T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae4570914a4e91e441e7448'),
    ProductID: 103,
    ProductName: 'Keyboard',
    Stock: 3,
    MinimumStock: 15,
    Supplier: 'HP Suppliers',
    RestockingDate: ISODate('2026-11-02T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae4570914a4e91e441e744a'),
    ProductID: 105,
    ProductName: 'Headphones',
    Stock: 4,
    MinimumStock: 10,
    Supplier: 'Boat Suppliers',
    RestockingDate: ISODate('2026-11-03T00:00:00.000Z')
  }
]
InventoryDB> db.Products.find({
|   $expr: { $lt: ["$Stock", "$MinimumStock"] }
| })
| 
[
  {
    _id: ObjectId('6ae4570914a4e91e441e7446'),
    ProductID: 101,
    ProductName: 'Laptop',
    Stock: 5,
    MinimumStock: 10,
    Supplier: 'Dell Suppliers',
    RestockingDate: ISODate('2026-11-05T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae4570914a4e91e441e7448'),
    ProductID: 103,
    ProductName: 'Keyboard',
    Stock: 3,
    MinimumStock: 15,
    Supplier: 'HP Suppliers',
    RestockingDate: ISODate('2026-11-02T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae4570914a4e91e441e744a'),
    ProductID: 105,
    ProductName: 'Headphones',
    Stock: 4,
    MinimumStock: 10,
    Supplier: 'Boat Suppliers',
    RestockingDate: ISODate('2026-11-03T00:00:00.000Z')
  }
]
InventoryDB> db.Products.find().sort({ Stock: 1 })
[
  {
    _id: ObjectId('6ae4570914a4e91e441e7448'),
    ProductID: 103,
    ProductName: 'Keyboard',
    Stock: 3,
    MinimumStock: 15,
    Supplier: 'HP Suppliers',
    RestockingDate: ISODate('2026-11-02T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae4570914a4e91e441e744a'),
    ProductID: 105,
    ProductName: 'Headphones',
    Stock: 4,
    MinimumStock: 10,
    Supplier: 'Boat Suppliers',
    RestockingDate: ISODate('2026-11-03T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae4570914a4e91e441e7446'),
    ProductID: 101,
    ProductName: 'Laptop',
    Stock: 5,
    MinimumStock: 10,
    Supplier: 'Dell Suppliers',
    RestockingDate: ISODate('2026-11-05T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae4570914a4e91e441e7449'),
    ProductID: 104,
    ProductName: 'Mouse',
    Stock: 20,
    MinimumStock: 5,
    Supplier: 'Logitech Traders',
    RestockingDate: ISODate('2026-11-15T00:00:00.000Z')
  },
  {
    _id: ObjectId('6ae4570914a4e91e441e7447'),
    ProductID: 102,
    ProductName: 'Mobile',
    Stock: 25,
    MinimumStock: 10,
    Supplier: 'Samsung Traders',
    RestockingDate: ISODate('2026-11-10T00:00:00.000Z')
  }
]
InventoryDB> db.Products.find({ Supplier: "Dell Suppliers" })
[
  {
    _id: ObjectId('6ae4570914a4e91e441e7446'),
    ProductID: 101,
    ProductName: 'Laptop',
    Stock: 5,
    MinimumStock: 10,
    Supplier: 'Dell Suppliers',
    RestockingDate: ISODate('2026-11-05T00:00:00.000Z')
  }
]
InventoryDB> 

```

## Question 11
Implement a Bank Wallet Transfer System using MongoDB transactions. Transfer an amount between two users and ensure that both balance updates are completed atomically.
### Commands and Output

```javascript
test> use BankWalletDB
switched to db BankWalletDB
BankWalletDB> db.createCollection("Wallets")
{ ok: 1 }
BankWalletDB> db.Wallets.insertMany([
|   { UserID: 101, Name: "Rohit", Balance: 10000 },
|   { UserID: 102, Name: "Amit", Balance: 5000 }
| ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae457c53f3357ddaac12b88'),
    '1': ObjectId('6ae457c53f3357ddaac12b89')
  }
}
BankWalletDB> const session = db.getMongo().startSession()

BankWalletDB> const walletDB = session.getDatabase("BankWalletDB")

BankWalletDB> session.startTransaction()

BankWalletDB> try {
|   const sender = walletDB.Wallets.updateOne(
|     { UserID: 101, Balance: { $gte: 2000 } },
|     { $inc: { Balance: -2000 } }
|   )
| 
|   if (sender.modifiedCount !== 1) {
|     throw new Error("Insufficient balance or sender not found")
|   }
| 
|   const receiver = walletDB.Wallets.updateOne(
|     { UserID: 102 },
|     { $inc: { Balance: 2000 } }
|   )
| 
|   if (receiver.modifiedCount !== 1) {
|     throw new Error("Receiver not found")
|   }
| 
|   session.commitTransaction()
|   print("Transfer successful")
| } catch (error) {
|   session.abortTransaction()
|   print("Transfer failed: " + error.message)
| } finally {
|   session.endSession()
| }
| 
Transfer failed: This MongoDB deployment does not support retryable writes. Please add retryWrites=false to your connection string.

BankWalletDB> db.Wallets.find()
[
  {
    _id: ObjectId('6ae457c53f3357ddaac12b88'),
    UserID: 101,
    Name: 'Rohit',
    Balance: 10000
  },
  {
    _id: ObjectId('6ae457c53f3357ddaac12b89'),
    UserID: 102,
    Name: 'Amit',
    Balance: 5000
  }
]
BankWalletDB> 


```

## Question 12
Create a User Notification System for messages, order updates, and system alerts. Write queries to retrieve unread notifications and update them after the user views them.
### Commands and Output

```javascript
test> use NotificationDB
switched to db NotificationDB
NotificationDB> db.createCollection("Notifications")
{ ok: 1 }
NotificationDB> db.Notifications.insertMany([
|   {
|     NotificationID: 1,
|     UserID: 101,
|     Type: "Message",
|     Message: "You have received a new message",
|     IsRead: false,
|     Date: new Date()
|   },
|   {
|     NotificationID: 2,
|     UserID: 101,
|     Type: "Order Update",
|     Message: "Your order has been shipped",
|     IsRead: false,
|     Date: new Date()
|   },
|   {
|     NotificationID: 3,
|     UserID: 102,
|     Type: "System Alert",
|     Message: "System maintenance scheduled",
|     IsRead: true,
|     Date: new Date()
|   },
|   {
|     NotificationID: 4,
|     UserID: 101,
|     Type: "System Alert",
|     Message: "New security update available",
|     IsRead: false,
|     Date: new Date()
|   }
| ])
| 
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae458a2ceb6712c2f2a6663'),
    '1': ObjectId('6ae458a2ceb6712c2f2a6664'),
    '2': ObjectId('6ae458a2ceb6712c2f2a6665'),
    '3': ObjectId('6ae458a2ceb6712c2f2a6666')
  }
}
NotificationDB> db.Notifications.find()
[
  {
    _id: ObjectId('6ae458a2ceb6712c2f2a6663'),
    NotificationID: 1,
    UserID: 101,
    Type: 'Message',
    Message: 'You have received a new message',
    IsRead: false,
    Date: ISODate('2026-10-30T08:43:14.281Z')
  },
  {
    _id: ObjectId('6ae458a2ceb6712c2f2a6664'),
    NotificationID: 2,
    UserID: 101,
    Type: 'Order Update',
    Message: 'Your order has been shipped',
    IsRead: false,
    Date: ISODate('2026-10-30T08:43:14.281Z')
  },
  {
    _id: ObjectId('6ae458a2ceb6712c2f2a6665'),
    NotificationID: 3,
    UserID: 102,
    Type: 'System Alert',
    Message: 'System maintenance scheduled',
    IsRead: true,
    Date: ISODate('2026-10-30T08:43:14.281Z')
  },
  {
    _id: ObjectId('6ae458a2ceb6712c2f2a6666'),
    NotificationID: 4,
    UserID: 101,
    Type: 'System Alert',
    Message: 'New security update available',
    IsRead: false,
    Date: ISODate('2026-10-30T08:43:14.281Z')
  }
]
NotificationDB> db.Notifications.find({
|   UserID: 101,
|   IsRead: false
| })
[
  {
    _id: ObjectId('6ae458a2ceb6712c2f2a6663'),
    NotificationID: 1,
    UserID: 101,
    Type: 'Message',
    Message: 'You have received a new message',
    IsRead: false,
    Date: ISODate('2026-10-30T08:43:14.281Z')
  },
  {
    _id: ObjectId('6ae458a2ceb6712c2f2a6664'),
    NotificationID: 2,
    UserID: 101,
    Type: 'Order Update',
    Message: 'Your order has been shipped',
    IsRead: false,
    Date: ISODate('2026-10-30T08:43:14.281Z')
  },
  {
    _id: ObjectId('6ae458a2ceb6712c2f2a6666'),
    NotificationID: 4,
    UserID: 101,
    Type: 'System Alert',
    Message: 'New security update available',
    IsRead: false,
    Date: ISODate('2026-10-30T08:43:14.281Z')
  }
]
NotificationDB> db.Notifications.updateOne(
|   { NotificationID: 1, UserID: 101 },
|   { $set: { IsRead: true } }
| )
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
NotificationDB> db.Notifications.updateMany(
|   { UserID: 101, IsRead: false },
|   { $set: { IsRead: true } }
| )
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 2,
  modifiedCount: 2,
  upsertedCount: 0
}
NotificationDB> db.Notifications.find({ UserID: 101 })
[
  {
    _id: ObjectId('6ae458a2ceb6712c2f2a6663'),
    NotificationID: 1,
    UserID: 101,
    Type: 'Message',
    Message: 'You have received a new message',
    IsRead: true,
    Date: ISODate('2026-10-30T08:43:14.281Z')
  },
  {
    _id: ObjectId('6ae458a2ceb6712c2f2a6664'),
    NotificationID: 2,
    UserID: 101,
    Type: 'Order Update',
    Message: 'Your order has been shipped',
    IsRead: true,
    Date: ISODate('2026-10-30T08:43:14.281Z')
  },
  {
    _id: ObjectId('6ae458a2ceb6712c2f2a6666'),
    NotificationID: 4,
    UserID: 101,
    Type: 'System Alert',
    Message: 'New security update available',
    IsRead: true,
    Date: ISODate('2026-10-30T08:43:14.281Z')
  }
]
NotificationDB> 

```

## Question 13
Design a Course Learning Platform containing courses, instructors, students, modules, progress, and completion status. Retrieve students according to their course progress.
### Commands and Output

```javascript
test> use CourseLearningDB
switched to db CourseLearningDB
CourseLearningDB> db.createCollection("Courses")
{ ok: 1 }
CourseLearningDB> db.Courses.insertMany([
|   {
|     CourseID: 101,
|     CourseName: "MongoDB",
|     Instructor: "Rahul",
|     Students: [
|       { StudentID: 1, Name: "Rohit", Progress: 80, Completed: false },
|       { StudentID: 2, Name: "Amit", Progress: 100, Completed: true }
|     ],
|     Modules: ["Introduction", "CRUD Operations", "Aggregation"]
|   },
|   {
|     CourseID: 102,
|     CourseName: "Python",
|     Instructor: "Priya",
|     Students: [
|       { StudentID: 3, Name: "Neha", Progress: 40, Completed: false },
|       { StudentID: 4, Name: "Rahul", Progress: 100, Completed: true }
|     ],
|     Modules: ["Basics", "Functions", "OOP"]
|   }
| ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae45995062c60948b209dc6'),
    '1': ObjectId('6ae45995062c60948b209dc7')
  }
}
CourseLearningDB> db.Courses.find()
[
  {
    _id: ObjectId('6ae45995062c60948b209dc6'),
    CourseID: 101,
    CourseName: 'MongoDB',
    Instructor: 'Rahul',
    Students: [
      { StudentID: 1, Name: 'Rohit', Progress: 80, Completed: false },
      { StudentID: 2, Name: 'Amit', Progress: 100, Completed: true }
    ],
    Modules: [ 'Introduction', 'CRUD Operations', 'Aggregation' ]
  },
  {
    _id: ObjectId('6ae45995062c60948b209dc7'),
    CourseID: 102,
    CourseName: 'Python',
    Instructor: 'Priya',
    Students: [
      { StudentID: 3, Name: 'Neha', Progress: 40, Completed: false },
      { StudentID: 4, Name: 'Rahul', Progress: 100, Completed: true }
    ],
    Modules: [ 'Basics', 'Functions', 'OOP' ]
  }
]
CourseLearningDB> db.Courses.aggregate([
|   { $unwind: "$Students" },
|   { $match: { "Students.Progress": { $gt: 50 } } },
|   { $project: { CourseName: 1, Student: "$Students.Name", Progress: "$Students.Progress" } }
| ])
| 
[
  {
    _id: ObjectId('6ae45995062c60948b209dc6'),
    CourseName: 'MongoDB',
    Student: 'Rohit',
    Progress: 80
  },
  {
    _id: ObjectId('6ae45995062c60948b209dc6'),
    CourseName: 'MongoDB',
    Student: 'Amit',
    Progress: 100
  },
  {
    _id: ObjectId('6ae45995062c60948b209dc7'),
    CourseName: 'Python',
    Student: 'Rahul',
    Progress: 100
  }
]
CourseLearningDB> db.Courses.aggregate([
|   { $unwind: "$Students" },
|   { $match: { "Students.Completed": true } },
|   { $project: { CourseName: 1, Student: "$Students.Name", Progress: "$Students.Progress" } }
| ])
[
  {
    _id: ObjectId('6ae45995062c60948b209dc6'),
    CourseName: 'MongoDB',
    Student: 'Amit',
    Progress: 100
  },
  {
    _id: ObjectId('6ae45995062c60948b209dc7'),
    CourseName: 'Python',
    Student: 'Rahul',
    Progress: 100
  }
]
CourseLearningDB> db.Courses.aggregate([
|   { $unwind: "$Students" },
|   { $match: { "Students.Progress": { $lt: 50 } } },
|   { $project: { CourseName: 1, Student: "$Students.Name", Progress: "$Students.Progress" } }
| ])
[
  {
    _id: ObjectId('6ae45995062c60948b209dc7'),
    CourseName: 'Python',
    Student: 'Neha',
    Progress: 40
  }
]
CourseLearningDB> db.Courses.updateOne(
|   { CourseID: 101, "Students.StudentID": 1 },
|   { $set: { "Students.$.Progress": 100, "Students.$.Completed": true } }
| )
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
CourseLearningDB> 

```

## Question 14
Create a Real-Time Order Tracking System where an order moves through stages such as Placed, Confirmed, Shipped, and Delivered. Store the complete status history and retrieve the current status of an order.
### Commands and Output

```javascript
test> use OrderTrackingDB
switched to db OrderTrackingDB
OrderTrackingDB> db.createCollection("Orders")
{ ok: 1 }
OrderTrackingDB> db.Orders.insertMany([
|   {
|     OrderID: 101,
|     Customer: "Rohit",
|     CurrentStatus: "Shipped",
|     StatusHistory: [
|       { Status: "Placed", Date: ISODate("2026-10-25T10:00:00Z") },
|       { Status: "Confirmed", Date: ISODate("2026-10-25T11:00:00Z") },
|       { Status: "Shipped", Date: ISODate("2026-10-26T09:00:00Z") }
|     ]
|   },
|   {
|     OrderID: 102,
|     Customer: "Amit",
|     CurrentStatus: "Delivered",
|     StatusHistory: [
|       { Status: "Placed", Date: ISODate("2026-10-20T10:00:00Z") },
|       { Status: "Confirmed", Date: ISODate("2026-10-20T11:00:00Z") },
|       { Status: "Shipped", Date: ISODate("2026-10-21T09:00:00Z") },
|       { Status: "Delivered", Date: ISODate("2026-10-23T15:00:00Z") }
|     ]
|   }
| ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae45a693d2588604c391b37'),
    '1': ObjectId('6ae45a693d2588604c391b38')
  }
}
OrderTrackingDB> db.Orders.find()
[
  {
    _id: ObjectId('6ae45a693d2588604c391b37'),
    OrderID: 101,
    Customer: 'Rohit',
    CurrentStatus: 'Shipped',
    StatusHistory: [
      { Status: 'Placed', Date: ISODate('2026-10-25T10:00:00.000Z') },
      { Status: 'Confirmed', Date: ISODate('2026-10-25T11:00:00.000Z') },
      { Status: 'Shipped', Date: ISODate('2026-10-26T09:00:00.000Z') }
    ]
  },
  {
    _id: ObjectId('6ae45a693d2588604c391b38'),
    OrderID: 102,
    Customer: 'Amit',
    CurrentStatus: 'Delivered',
    StatusHistory: [
      { Status: 'Placed', Date: ISODate('2026-10-20T10:00:00.000Z') },
      { Status: 'Confirmed', Date: ISODate('2026-10-20T11:00:00.000Z') },
      { Status: 'Shipped', Date: ISODate('2026-10-21T09:00:00.000Z') },
      { Status: 'Delivered', Date: ISODate('2026-10-23T15:00:00.000Z') }
    ]
  }
]
OrderTrackingDB> db.Orders.find(
|   { OrderID: 101 },
|   { _id: 0, OrderID: 1, CurrentStatus: 1 }
| )
[ { OrderID: 101, CurrentStatus: 'Shipped' } ]
OrderTrackingDB> db.Orders.find(
|   { OrderID: 101 },
|   { _id: 0, OrderID: 1, StatusHistory: 1 }
| )
| 
[
  {
    OrderID: 101,
    StatusHistory: [
      { Status: 'Placed', Date: ISODate('2026-10-25T10:00:00.000Z') },
      { Status: 'Confirmed', Date: ISODate('2026-10-25T11:00:00.000Z') },
      { Status: 'Shipped', Date: ISODate('2026-10-26T09:00:00.000Z') }
    ]
  }
]
OrderTrackingDB> db.Orders.updateOne(
|   { OrderID: 101 },
|   {
|     $set: { CurrentStatus: "Confirmed" },
|     $push: {
|       StatusHistory: {
|         Status: "Confirmed",
|         Date: new Date()
|       }
|     }
|   }
| )
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
OrderTrackingDB> db.Orders.updateOne(
|   { OrderID: 101 },
|   {
|     $set: { CurrentStatus: "Shipped" },
|     $push: {
|       StatusHistory: {
|         Status: "Shipped",
|         Date: new Date()
|       }
|     }
|   }
| )
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
OrderTrackingDB> db.Orders.find({ CurrentStatus: "Delivered" })
[
  {
    _id: ObjectId('6ae45a693d2588604c391b38'),
    OrderID: 102,
    Customer: 'Amit',
    CurrentStatus: 'Delivered',
    StatusHistory: [
      { Status: 'Placed', Date: ISODate('2026-10-20T10:00:00.000Z') },
      { Status: 'Confirmed', Date: ISODate('2026-10-20T11:00:00.000Z') },
      { Status: 'Shipped', Date: ISODate('2026-10-21T09:00:00.000Z') },
      { Status: 'Delivered', Date: ISODate('2026-10-23T15:00:00.000Z') }
    ]
  }
]
OrderTrackingDB> db.Orders.find({ CurrentStatus: "Shipped" })
[
  {
    _id: ObjectId('6ae45a693d2588604c391b37'),
    OrderID: 101,
    Customer: 'Rohit',
    CurrentStatus: 'Shipped',
    StatusHistory: [
      { Status: 'Placed', Date: ISODate('2026-10-25T10:00:00.000Z') },
      { Status: 'Confirmed', Date: ISODate('2026-10-25T11:00:00.000Z') },
      { Status: 'Shipped', Date: ISODate('2026-10-26T09:00:00.000Z') },
      { Status: 'Confirmed', Date: ISODate('2026-10-30T08:51:53.779Z') },
      { Status: 'Shipped', Date: ISODate('2026-10-30T08:52:07.916Z') }
    ]
  }
]
OrderTrackingDB> 

```

## Question 15
Develop a Flexible News Database in which different news articles may contain different fields such as author, location, category, tags, images, and sources. Write queries to search articles despite variations in document structure.
### Commands and Output

```javascript
test> use NewsDB
switched to db NewsDB
NewsDB> db.createCollection("News")
{ ok: 1 }
NewsDB> db.News.insertMany([
|   {
|     NewsID: 101,
|     Title: "Technology Updates",
|     Author: "Rohit",
|     Category: "Technology",
|     Tags: ["AI", "Technology"],
|     Location: "Delhi",
|     Image: "tech.jpg",
|     Source: "Tech News"
|   },
|   {
|     NewsID: 102,
|     Title: "Cricket World Cup",
|     Category: "Sports",
|     Tags: ["Cricket", "Sports"],
|     Location: "Mumbai",
|     Source: "Sports News"
|   },
|   {
|     NewsID: 103,
|     Title: "Election Updates",
|     Author: "Amit",
|     Category: "Politics",
|     Location: "Patna",
|     Tags: ["Election", "India"]
|   },
|   {
|     NewsID: 104,
|     Title: "Health Awareness",
|     Author: "Priya",
|     Category: "Health",
|     Tags: ["Health", "Fitness"],
|     Image: "health.jpg",
|     Sources: ["Health Times", "Medical News"]
|   }
| ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ae45be8ba9217fcd6dd9d41'),
    '1': ObjectId('6ae45be8ba9217fcd6dd9d42'),
    '2': ObjectId('6ae45be8ba9217fcd6dd9d43'),
    '3': ObjectId('6ae45be8ba9217fcd6dd9d44')
  }
}
NewsDB> db.News.find()
[
  {
    _id: ObjectId('6ae45be8ba9217fcd6dd9d41'),
    NewsID: 101,
    Title: 'Technology Updates',
    Author: 'Rohit',
    Category: 'Technology',
    Tags: [ 'AI', 'Technology' ],
    Location: 'Delhi',
    Image: 'tech.jpg',
    Source: 'Tech News'
  },
  {
    _id: ObjectId('6ae45be8ba9217fcd6dd9d42'),
    NewsID: 102,
    Title: 'Cricket World Cup',
    Category: 'Sports',
    Tags: [ 'Cricket', 'Sports' ],
    Location: 'Mumbai',
    Source: 'Sports News'
  },
  {
    _id: ObjectId('6ae45be8ba9217fcd6dd9d43'),
    NewsID: 103,
    Title: 'Election Updates',
    Author: 'Amit',
    Category: 'Politics',
    Location: 'Patna',
    Tags: [ 'Election', 'India' ]
  },
  {
    _id: ObjectId('6ae45be8ba9217fcd6dd9d44'),
    NewsID: 104,
    Title: 'Health Awareness',
    Author: 'Priya',
    Category: 'Health',
    Tags: [ 'Health', 'Fitness' ],
    Image: 'health.jpg',
    Sources: [ 'Health Times', 'Medical News' ]
  }
]
NewsDB> db.News.find({ Category: "Technology" })
[
  {
    _id: ObjectId('6ae45be8ba9217fcd6dd9d41'),
    NewsID: 101,
    Title: 'Technology Updates',
    Author: 'Rohit',
    Category: 'Technology',
    Tags: [ 'AI', 'Technology' ],
    Location: 'Delhi',
    Image: 'tech.jpg',
    Source: 'Tech News'
  }
]
NewsDB> db.News.find({ Tags: "Cricket" })
[
  {
    _id: ObjectId('6ae45be8ba9217fcd6dd9d42'),
    NewsID: 102,
    Title: 'Cricket World Cup',
    Category: 'Sports',
    Tags: [ 'Cricket', 'Sports' ],
    Location: 'Mumbai',
    Source: 'Sports News'
  }
]
NewsDB> db.News.find({ Location: "Patna" })
[
  {
    _id: ObjectId('6ae45be8ba9217fcd6dd9d43'),
    NewsID: 103,
    Title: 'Election Updates',
    Author: 'Amit',
    Category: 'Politics',
    Location: 'Patna',
    Tags: [ 'Election', 'India' ]
  }
]
NewsDB> db.News.find({ Author: "Rohit" })
[
  {
    _id: ObjectId('6ae45be8ba9217fcd6dd9d41'),
    NewsID: 101,
    Title: 'Technology Updates',
    Author: 'Rohit',
    Category: 'Technology',
    Tags: [ 'AI', 'Technology' ],
    Location: 'Delhi',
    Image: 'tech.jpg',
    Source: 'Tech News'
  }
]
NewsDB> db.News.find({ Image: { $exists: true } })
[
  {
    _id: ObjectId('6ae45be8ba9217fcd6dd9d41'),
    NewsID: 101,
    Title: 'Technology Updates',
    Author: 'Rohit',
    Category: 'Technology',
    Tags: [ 'AI', 'Technology' ],
    Location: 'Delhi',
    Image: 'tech.jpg',
    Source: 'Tech News'
  },
  {
    _id: ObjectId('6ae45be8ba9217fcd6dd9d44'),
    NewsID: 104,
    Title: 'Health Awareness',
    Author: 'Priya',
    Category: 'Health',
    Tags: [ 'Health', 'Fitness' ],
    Image: 'health.jpg',
    Sources: [ 'Health Times', 'Medical News' ]
  }
]
NewsDB> db.News.find({ Sources: { $exists: true } })
[
  {
    _id: ObjectId('6ae45be8ba9217fcd6dd9d44'),
    NewsID: 104,
    Title: 'Health Awareness',
    Author: 'Priya',
    Category: 'Health',
    Tags: [ 'Health', 'Fitness' ],
    Image: 'health.jpg',
    Sources: [ 'Health Times', 'Medical News' ]
  }
]
NewsDB> db.News.find({
|   Category: "Sports",
|   Tags: "Cricket"
| })
[
  {
    _id: ObjectId('6ae45be8ba9217fcd6dd9d42'),
    NewsID: 102,
    Title: 'Cricket World Cup',
    Category: 'Sports',
    Tags: [ 'Cricket', 'Sports' ],
    Location: 'Mumbai',
    Source: 'Sports News'
  }
]
NewsDB> db.News.find({ Author: { $exists: false } })
[
  {
    _id: ObjectId('6ae45be8ba9217fcd6dd9d42'),
    NewsID: 102,
    Title: 'Cricket World Cup',
    Category: 'Sports',
    Tags: [ 'Cricket', 'Sports' ],
    Location: 'Mumbai',
    Source: 'Sports News'
  }
]
NewsDB> 
```