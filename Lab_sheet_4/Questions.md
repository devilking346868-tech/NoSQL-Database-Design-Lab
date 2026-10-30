# Lab Sheet-04: NoSQL Database Design Lab
# BCA V Semester / III Years (Session 2026- 2027)

## Question 1
Install and configure Apache HBase. Create a table named Student with column families personal and academic. Insert at least five student records and display them using HBase shell commands.

### Commands and Output

```javascript
rohit@rohit-OptiPlex-3050:/usr/local/hbase$ bin/hbase shell
HBase Shell
Use "help" to get list of supported commands.
Use "exit" to quit this interactive shell.
For Reference, please visit: https://hbase.apache.org/docs/shell
Version 2.5.16, r33c9a36af4fb6505196dcaa084ee2cf200071475, Fri Aug 14 12:53:27 PDT 2026
Took 0.0042 seconds                                                             
hbase:001:0> 














hbase:001:0> create 'Student', 'personal', 'academic'
Created table Student
Took 2.1374 seconds                                                             
=> Hbase::Table - Student
hbase:002:0> put 'Student', '101', 'personal:name', 'Rohit'
Took 0.6036 seconds                                                             
hbase:003:0> put 'Student', '101', 'personal:department', 'BCA'
Took 0.0097 seconds                                                             
hbase:004:0> put 'Student', '101', 'academic:semester', '5'
Took 0.0049 seconds                                                             
hbase:005:0> put 'Student', '101', 'academic:cgpa', '8.5'
Took 0.0076 seconds                                                             
hbase:006:0> 
hbase:007:0> put 'Student', '102', 'personal:name', 'Amit'
Took 0.0048 seconds                                                             
hbase:008:0> put 'Student', '102', 'personal:department', 'BCA'
Took 0.0066 seconds                                                             
hbase:009:0> put 'Student', '102', 'academic:semester', '5'
Took 0.0052 seconds                                                             
hbase:010:0> put 'Student', '102', 'academic:cgpa', '8.2'
Took 0.0051 seconds                                                             
hbase:011:0> 
hbase:012:0> put 'Student', '103', 'personal:name', 'Rahul'
Took 0.0089 seconds                                                             
hbase:013:0> put 'Student', '103', 'personal:department', 'MCA'
Took 0.0055 seconds                                                             
hbase:014:0> put 'Student', '103', 'academic:semester', '3'
Took 0.0066 seconds                                                             
hbase:015:0> put 'Student', '103', 'academic:cgpa', '8.7'
Took 0.0147 seconds                                                             
hbase:016:0> 
hbase:017:0> put 'Student', '104', 'personal:name', 'Priya'
Took 0.0067 seconds                                                             
hbase:018:0> put 'Student', '104', 'personal:department', 'BCA'
Took 0.0048 seconds                                                             
hbase:019:0> put 'Student', '104', 'academic:semester', '5'
Took 0.0089 seconds                                                             
hbase:020:0> put 'Student', '104', 'academic:cgpa', '9.1'
Took 0.0085 seconds                                                             
hbase:021:0> 
hbase:022:0> put 'Student', '105', 'personal:name', 'Neha'
Took 0.0051 seconds                                                             
hbase:023:0> put 'Student', '105', 'personal:department', 'MCA'
Took 0.0106 seconds                                                             
hbase:024:0> put 'Student', '105', 'academic:semester', '3'
Took 0.0058 seconds                                                             
hbase:025:0> put 'Student', '105', 'academic:cgpa', '8.9'
Took 0.0047 seconds                                                             
hbase:026:0> scan 'Student'
ROW                   COLUMN+CELL                                               
 101                  column=academic:cgpa, timestamp=2026-10-30T14:54:29.079, v
                      alue=8.5                                                  
 101                  column=academic:semester, timestamp=2026-10-30T14:54:29.02
                      8, value=5                                                
 101                  column=personal:department, timestamp=2026-10-30T14:54:28.
                      986, value=BCA                                            
 101                  column=personal:name, timestamp=2026-10-30T14:54:28.915, v
                      alue=Rohit                                                
 102                  column=academic:cgpa, timestamp=2026-10-30T14:54:29.253, v
                      alue=8.2                                                  
 102                  column=academic:semester, timestamp=2026-10-30T14:54:29.22
                      0, value=5                                                
 102                  column=personal:department, timestamp=2026-10-30T14:54:29.
                      186, value=BCA                                            
 102                  column=personal:name, timestamp=2026-10-30T14:54:29.147, v
                      alue=Amit                                                 
 103                  column=academic:cgpa, timestamp=2026-10-30T14:54:29.467, v
                      alue=8.7                                                  
 103                  column=academic:semester, timestamp=2026-10-30T14:54:29.40
                      2, value=3                                                
 103                  column=personal:department, timestamp=2026-10-30T14:54:29.
                      369, value=MCA                                            
 103                  column=personal:name, timestamp=2026-10-30T14:54:29.313, v
                      alue=Rahul                                                
 104                  column=academic:cgpa, timestamp=2026-10-30T14:54:29.675, v
                      alue=9.1                                                  
 104                  column=academic:semester, timestamp=2026-10-30T14:54:29.62
                      9, value=5                                                
 104                  column=personal:department, timestamp=2026-10-30T14:54:29.
                      589, value=BCA                                            
 104                  column=personal:name, timestamp=2026-10-30T14:54:29.549, v
                      alue=Priya                                                
 105                  column=academic:cgpa, timestamp=2026-10-30T14:54:30.590, v
                      alue=8.9                                                  
 105                  column=academic:semester, timestamp=2026-10-30T14:54:29.82
                      2, value=3                                                
 105                  column=personal:department, timestamp=2026-10-30T14:54:29.
                      785, value=MCA                                            
 105                  column=personal:name, timestamp=2026-10-30T14:54:29.752, v
                      alue=Neha                                                 
5 row(s)
Took 0.1543 seconds                                                             
hbase:027:0> get 'Student', '101'
COLUMN                CELL                                                      
 academic:cgpa        timestamp=2026-10-30T14:54:29.079, value=8.5              
 academic:semester    timestamp=2026-10-30T14:54:29.028, value=5                
 personal:department  timestamp=2026-10-30T14:54:28.986, value=BCA              
 personal:name        timestamp=2026-10-30T14:54:28.915, value=Rohit            
1 row(s)
Took 0.0648 seconds                                                             
hbase:028:0> list
TABLE                                                                           
Student                                                                         
1 row(s)
Took 0.0439 seconds                                                             
=> ["Student"]
hbase:029:0> 
```


## Question 2
Using Apache HBase, perform basic CRUD operations on an Employee table. Demonstrate create, put, get, scan, and delete operations.

### Commands and Output
```javascript
hbase:001:0> create 'Employee', 'personal', 'job'
Created table Employee
Took 2.6392 seconds                                                             
=> Hbase::Table - Employee
hbase:002:0> put 'Employee', '101', 'personal:name', 'Rohit'
Took 0.4411 seconds                                                             
hbase:003:0> put 'Employee', '101', 'personal:city', 'Chhapra'
Took 0.0144 seconds                                                             
hbase:004:0> put 'Employee', '101', 'job:department', 'IT'
Took 0.0477 seconds                                                             
hbase:005:0> put 'Employee', '101', 'job:salary', '30000'
Took 0.0033 seconds                                                             
hbase:006:0> 
hbase:007:0> put 'Employee', '102', 'personal:name', 'Amit'
Took 0.0058 seconds                                                             
hbase:008:0> put 'Employee', '102', 'personal:city', 'Patna'
Took 0.0042 seconds                                                             
hbase:009:0> put 'Employee', '102', 'job:department', 'HR'
Took 0.0051 seconds                                                             
hbase:010:0> put 'Employee', '102', 'job:salary', '25000'
Took 0.0074 seconds                                                             
hbase:011:0> 
hbase:012:0> put 'Employee', '103', 'personal:name', 'Rahul'
Took 0.0039 seconds                                                             
hbase:013:0> put 'Employee', '103', 'personal:city', 'Delhi'
Took 0.0067 seconds                                                             
hbase:014:0> put 'Employee', '103', 'job:department', 'Finance'
Took 0.0069 seconds                                                             
hbase:015:0> put 'Employee', '103', 'job:salary', '35000'
Took 0.0215 seconds                                                             
hbase:016:0> get 'Employee', '101'
COLUMN                CELL                                                      
 job:department       timestamp=2026-10-30T15:03:16.206, value=IT               
 job:salary           timestamp=2026-10-30T15:03:16.281, value=30000            
 personal:city        timestamp=2026-10-30T15:03:16.154, value=Chhapra          
 personal:name        timestamp=2026-10-30T15:03:16.054, value=Rohit            
1 row(s)
Took 0.1529 seconds                                                             
hbase:017:0> scan 'Employee'
ROW                   COLUMN+CELL                                               
 101                  column=job:department, timestamp=2026-10-30T15:03:16.206, 
                      value=IT                                                  
 101                  column=job:salary, timestamp=2026-10-30T15:03:16.281, valu
                      e=30000                                                   
 101                  column=personal:city, timestamp=2026-10-30T15:03:16.154, v
                      alue=Chhapra                                              
 101                  column=personal:name, timestamp=2026-10-30T15:03:16.054, v
                      alue=Rohit                                                
 102                  column=job:department, timestamp=2026-10-30T15:03:16.412, 
                      value=HR                                                  
 102                  column=job:salary, timestamp=2026-10-30T15:03:16.450, valu
                      e=25000                                                   
 102                  column=personal:city, timestamp=2026-10-30T15:03:16.377, v
                      alue=Patna                                                
 102                  column=personal:name, timestamp=2026-10-30T15:03:16.343, v
                      alue=Amit                                                 
 103                  column=job:department, timestamp=2026-10-30T15:03:16.574, 
                      value=Finance                                             
 103                  column=job:salary, timestamp=2026-10-30T15:03:17.443, valu
                      e=35000                                                   
 103                  column=personal:city, timestamp=2026-10-30T15:03:16.542, v
                      alue=Delhi                                                
 103                  column=personal:name, timestamp=2026-10-30T15:03:16.499, v
                      alue=Rahul                                                
3 row(s)
Took 0.0706 seconds                                                             
hbase:018:0> put 'Employee', '101', 'job:salary', '40000'
Took 0.0038 seconds                                                             
hbase:019:0> delete 'Employee', '102', 'personal:city'
Took 0.0503 seconds                                                             
hbase:020:0> deleteall 'Employee', '103'
Took 0.0046 seconds                                                             
hbase:021:0> scan 'Employee'
ROW                   COLUMN+CELL                                               
 101                  column=job:department, timestamp=2026-10-30T15:03:16.206, 
                      value=IT                                                  
 101                  column=job:salary, timestamp=2026-10-30T15:03:49.632, valu
                      e=40000                                                   
 101                  column=personal:city, timestamp=2026-10-30T15:03:16.154, v
                      alue=Chhapra                                              
 101                  column=personal:name, timestamp=2026-10-30T15:03:16.054, v
                      alue=Rohit                                                
 102                  column=job:department, timestamp=2026-10-30T15:03:16.412, 
                      value=HR                                                  
 102                  column=job:salary, timestamp=2026-10-30T15:03:16.450, valu
                      e=25000                                                   
 102                  column=personal:name, timestamp=2026-10-30T15:03:16.343, v
                      alue=Amit                                                 
2 row(s)
Took 0.0308 seconds                                                             
hbase:022:0> list
TABLE                                                                           
Employee                                                                        
Student                                                                         
2 row(s)
Took 0.1601 seconds                                                             
=> ["Employee", "Student"]
hbase:023:0> 

```



## Question 3
Design an HBase table for an Event Logging System. Store event_id, timestamp, user information, event type, and status using appropriate column families. Insert sample events
and retrieve them based on row keys.
### Commands and Output
```javascript
hbase:023:0> create 'EventLog', 'event', 'user', 'details'
Created table EventLog
Took 2.5105 seconds                                                             
=> Hbase::Table - EventLog
hbase:024:0> put 'EventLog', 'E101', 'event:event_id', 'E101'
Took 0.1268 seconds                                                             
hbase:025:0> put 'EventLog', 'E101', 'event:timestamp', '2026-10-30 10:00:00'
Took 0.0092 seconds                                                             
hbase:026:0> put 'EventLog', 'E101', 'user:user_id', '101'
Took 0.1358 seconds                                                             
hbase:027:0> put 'EventLog', 'E101', 'user:username', 'Rohit'
Took 0.0104 seconds                                                             
hbase:028:0> put 'EventLog', 'E101', 'details:event_type', 'Login'
Took 0.8353 seconds                                                             
hbase:029:0> put 'EventLog', 'E101', 'details:status', 'Success'
Took 0.0059 seconds                                                             
hbase:030:0> 
hbase:031:0> put 'EventLog', 'E102', 'event:event_id', 'E102'
Took 0.0045 seconds                                                             
hbase:032:0> put 'EventLog', 'E102', 'event:timestamp', '2026-10-30 10:05:00'
Took 0.0051 seconds                                                             
hbase:033:0> put 'EventLog', 'E102', 'user:user_id', '102'
Took 0.0034 seconds                                                             
hbase:034:0> put 'EventLog', 'E102', 'user:username', 'Amit'
Took 0.0042 seconds                                                             
hbase:035:0> put 'EventLog', 'E102', 'details:event_type', 'Logout'
Took 0.0039 seconds                                                             
hbase:036:0> put 'EventLog', 'E102', 'details:status', 'Success'
Took 0.0036 seconds                                                             
hbase:037:0> 
hbase:038:0> put 'EventLog', 'E103', 'event:event_id', 'E103'
Took 0.0055 seconds                                                             
hbase:039:0> put 'EventLog', 'E103', 'event:timestamp', '2026-10-30 10:10:00'
Took 0.0033 seconds                                                             
hbase:040:0> put 'EventLog', 'E103', 'user:user_id', '103'
Took 0.0048 seconds                                                             
hbase:041:0> put 'EventLog', 'E103', 'user:username', 'Rahul'
Took 0.0083 seconds                                                             
hbase:042:0> put 'EventLog', 'E103', 'details:event_type', 'Login'
Took 0.0057 seconds                                                             
hbase:043:0> put 'EventLog', 'E103', 'details:status', 'Failed'
Took 0.0039 seconds                                                             
hbase:044:0> 
hbase:045:0> put 'EventLog', 'E104', 'event:event_id', 'E104'
Took 0.0045 seconds                                                             
hbase:046:0> put 'EventLog', 'E104', 'event:timestamp', '2026-10-30 10:15:00'
Took 0.0037 seconds                                                             
hbase:047:0> put 'EventLog', 'E104', 'user:user_id', '104'
Took 0.0070 seconds                                                             
hbase:048:0> put 'EventLog', 'E104', 'user:username', 'Priya'
Took 0.0035 seconds                                                             
hbase:049:0> put 'EventLog', 'E104', 'details:event_type', 'File Upload'
Took 0.0057 seconds                                                             
hbase:050:0> put 'EventLog', 'E104', 'details:status', 'Success'
Took 0.0034 seconds                                                             
hbase:051:0> 
hbase:052:0> put 'EventLog', 'E105', 'event:event_id', 'E105'
Took 0.0097 seconds                                                             
hbase:053:0> put 'EventLog', 'E105', 'event:timestamp', '2026-10-30 10:20:00'
Took 0.0031 seconds                                                             
hbase:054:0> put 'EventLog', 'E105', 'user:user_id', '105'
Took 0.0135 seconds                                                             
hbase:055:0> put 'EventLog', 'E105', 'user:username', 'Neha'
Took 0.0054 seconds                                                             
hbase:056:0> put 'EventLog', 'E105', 'details:event_type', 'Password Change'
Took 0.0137 seconds                                                             
hbase:057:0> put 'EventLog', 'E105', 'details:status', 'Success'
Took 0.0119 seconds                                                             
hbase:058:0> scan 'EventLog'
ROW                   COLUMN+CELL                                               
 E101                 column=details:event_type, timestamp=2026-10-30T15:07:28.4
                      61, value=Login                                           
 E101                 column=details:status, timestamp=2026-10-30T15:07:29.355, 
                      value=Success                                             
 E101                 column=event:event_id, timestamp=2026-10-30T15:07:28.048, 
                      value=E101                                                
 E101                 column=event:timestamp, timestamp=2026-10-30T15:07:28.096,
                       value=2026-10-30 10:00:00                                
 E101                 column=user:user_id, timestamp=2026-10-30T15:07:28.151, va
                      lue=101                                                   
 E101                 column=user:username, timestamp=2026-10-30T15:07:28.393, v
                      alue=Rohit                                                
 E102                 column=details:event_type, timestamp=2026-10-30T15:07:29.4
                      98, value=Logout                                          
 E102                 column=details:status, timestamp=2026-10-30T15:07:29.519, 
                      value=Success                                             
 E102                 column=event:event_id, timestamp=2026-10-30T15:07:29.402, 
                      value=E102                                                
 E102                 column=event:timestamp, timestamp=2026-10-30T15:07:29.429,
                       value=2026-10-30 10:05:00                                
 E102                 column=user:user_id, timestamp=2026-10-30T15:07:29.452, va
                      lue=102                                                   
 E102                 column=user:username, timestamp=2026-10-30T15:07:29.473, v
                      alue=Amit                                                 
 E103                 column=details:event_type, timestamp=2026-10-30T15:07:29.6
                      67, value=Login                                           
 E103                 column=details:status, timestamp=2026-10-30T15:07:29.705, 
                      value=Failed                                              
 E103                 column=event:event_id, timestamp=2026-10-30T15:07:29.559, 
                      value=E103                                                
 E103                 column=event:timestamp, timestamp=2026-10-30T15:07:29.585,
                       value=2026-10-30 10:10:00                                
 E103                 column=user:user_id, timestamp=2026-10-30T15:07:29.606, va
                      lue=103                                                   
 E103                 column=user:username, timestamp=2026-10-30T15:07:29.631, v
                      alue=Rahul                                                
 E104                 column=details:event_type, timestamp=2026-10-30T15:07:29.8
                      59, value=File Upload                                     
 E104                 column=details:status, timestamp=2026-10-30T15:07:29.884, 
                      value=Success                                             
 E104                 column=event:event_id, timestamp=2026-10-30T15:07:29.750, 
                      value=E104                                                
 E104                 column=event:timestamp, timestamp=2026-10-30T15:07:29.783,
                       value=2026-10-30 10:15:00                                
 E104                 column=user:user_id, timestamp=2026-10-30T15:07:29.808, va
                      lue=104                                                   
 E104                 column=user:username, timestamp=2026-10-30T15:07:29.834, v
                      alue=Priya                                                
 E105                 column=details:event_type, timestamp=2026-10-30T15:07:30.0
                      76, value=Password Change                                 
 E105                 column=details:status, timestamp=2026-10-30T15:07:31.094, 
                      value=Success                                             
 E105                 column=event:event_id, timestamp=2026-10-30T15:07:29.942, 
                      value=E105                                                
 E105                 column=event:timestamp, timestamp=2026-10-30T15:07:29.983,
                       value=2026-10-30 10:20:00                                
 E105                 column=user:user_id, timestamp=2026-10-30T15:07:30.009, va
                      lue=105                                                   
 E105                 column=user:username, timestamp=2026-10-30T15:07:30.044, v
                      alue=Neha                                                 
5 row(s)
Took 0.0680 seconds                                                             
hbase:059:0> get 'EventLog', 'E101'
COLUMN                CELL                                                      
 details:event_type   timestamp=2026-10-30T15:07:28.461, value=Login            
 details:status       timestamp=2026-10-30T15:07:29.355, value=Success          
 event:event_id       timestamp=2026-10-30T15:07:28.048, value=E101             
 event:timestamp      timestamp=2026-10-30T15:07:28.096, value=2026-10-30 10:00:
                      00                                                        
 user:user_id         timestamp=2026-10-30T15:07:28.151, value=101              
 user:username        timestamp=2026-10-30T15:07:28.393, value=Rohit            
1 row(s)
Took 0.0287 seconds                                                             
hbase:060:0> get 'EventLog', 'E103'
COLUMN                CELL                                                      
 details:event_type   timestamp=2026-10-30T15:07:29.667, value=Login            
 details:status       timestamp=2026-10-30T15:07:29.705, value=Failed           
 event:event_id       timestamp=2026-10-30T15:07:29.559, value=E103             
 event:timestamp      timestamp=2026-10-30T15:07:29.585, value=2026-10-30 10:10:
                      00                                                        
 user:user_id         timestamp=2026-10-30T15:07:29.606, value=103              
 user:username        timestamp=2026-10-30T15:07:29.631, value=Rahul            
1 row(s)
Took 0.0309 seconds                                                             
hbase:061:0> get 'EventLog', 'E105'
COLUMN                CELL                                                      
 details:event_type   timestamp=2026-10-30T15:07:30.076, value=Password Change  
 details:status       timestamp=2026-10-30T15:07:31.094, value=Success          
 event:event_id       timestamp=2026-10-30T15:07:29.942, value=E105             
 event:timestamp      timestamp=2026-10-30T15:07:29.983, value=2026-10-30 10:20:
                      00                                                        
 user:user_id         timestamp=2026-10-30T15:07:30.009, value=105              
 user:username        timestamp=2026-10-30T15:07:30.044, value=Neha             
1 row(s)
Took 0.0191 seconds                                                             
hbase:062:0> 

```


## Question 4
Create an HBase table for a Content Management System (CMS) with column families such as content, author, and metadata. Insert, update, retrieve, and delete content records.
### Commands and Output
```javascript
hbase:062:0> create 'CMS', 'content', 'author', 'metadata'
Created table CMS
Took 2.5010 seconds                                                                                                                                                                                   
=> Hbase::Table - CMS
hbase:063:0> put 'CMS', 'C101', 'content:title', 'Introduction to MongoDB'
Took 0.0914 seconds                                                                                                                                                                                   
hbase:064:0> put 'CMS', 'C101', 'content:body', 'MongoDB is a NoSQL database'
Took 0.0085 seconds                                                                                                                                                                                   
hbase:065:0> put 'CMS', 'C101', 'author:name', 'Rohit'
Took 0.0036 seconds                                                                                                                                                                                   
hbase:066:0> put 'CMS', 'C101', 'metadata:category', 'Technology'
Took 0.0053 seconds                                                                                                                                                                                   
hbase:067:0> put 'CMS', 'C101', 'metadata:status', 'Published'
Took 0.0033 seconds                                                                                                                                                                                   
hbase:068:0> 
hbase:069:0> put 'CMS', 'C102', 'content:title', 'Learning Python'
Took 0.0053 seconds                                                                                                                                                                                   
hbase:070:0> put 'CMS', 'C102', 'content:body', 'Python is a programming language'
Took 0.0110 seconds                                                                                                                                                                                   
hbase:071:0> put 'CMS', 'C102', 'author:name', 'Amit'
Took 0.0120 seconds                                                                                                                                                                                   
hbase:072:0> put 'CMS', 'C102', 'metadata:category', 'Programming'
Took 0.0099 seconds                                                                                                                                                                                   
hbase:073:0> put 'CMS', 'C102', 'metadata:status', 'Draft'
Took 0.0183 seconds                                                                                                                                                                                   
hbase:074:0> 
hbase:075:0> put 'CMS', 'C103', 'content:title', 'Web Development'
Took 0.0031 seconds                                                                                                                                                                                   
hbase:076:0> put 'CMS', 'C103', 'content:body', 'Learn HTML and CSS'
Took 0.0044 seconds                                                                                                                                                                                   
hbase:077:0> put 'CMS', 'C103', 'author:name', 'Priya'
Took 0.0039 seconds                                                                                                                                                                                   
hbase:078:0> put 'CMS', 'C103', 'metadata:category', 'Technology'
Took 0.0043 seconds                                                                                                                                                                                   
hbase:079:0> put 'CMS', 'C103', 'metadata:status', 'Published'
Took 0.0071 seconds                                                                                                                                                                                   
hbase:080:0> put 'CMS', 'C101', 'content:title', 'Introduction to HBase'
Took 0.0050 seconds                                                                                                                                                                                   
hbase:081:0> put 'CMS', 'C101', 'metadata:status', 'Updated'
Took 0.0063 seconds                                                                                                                                                                                   
hbase:082:0> get 'CMS', 'C101'
COLUMN                                             CELL                                                                                                                                               
 author:name                                       timestamp=2026-10-30T15:11:23.088, value=Rohit                                                                                                     
 content:body                                      timestamp=2026-10-30T15:11:23.063, value=MongoDB is a NoSQL database                                                                               
 content:title                                     timestamp=2026-10-30T15:11:35.552, value=Introduction to HBase                                                                                     
 metadata:category                                 timestamp=2026-10-30T15:11:23.117, value=Technology                                                                                                
 metadata:status                                   timestamp=2026-10-30T15:11:35.578, value=Updated                                                                                                   
1 row(s)
Took 0.0311 seconds                                                                                                                                                                                   
hbase:083:0> scan 'CMS'
ROW                                                COLUMN+CELL                                                                                                                                        
 C101                                              column=author:name, timestamp=2026-10-30T15:11:23.088, value=Rohit                                                                                 
 C101                                              column=content:body, timestamp=2026-10-30T15:11:23.063, value=MongoDB is a NoSQL database                                                          
 C101                                              column=content:title, timestamp=2026-10-30T15:11:35.552, value=Introduction to HBase                                                               
 C101                                              column=metadata:category, timestamp=2026-10-30T15:11:23.117, value=Technology                                                                      
 C101                                              column=metadata:status, timestamp=2026-10-30T15:11:35.578, value=Updated                                                                           
 C102                                              column=author:name, timestamp=2026-10-30T15:11:23.257, value=Amit                                                                                  
 C102                                              column=content:body, timestamp=2026-10-30T15:11:23.224, value=Python is a programming language                                                     
 C102                                              column=content:title, timestamp=2026-10-30T15:11:23.202, value=Learning Python                                                                     
 C102                                              column=metadata:category, timestamp=2026-10-30T15:11:23.295, value=Programming                                                                     
 C102                                              column=metadata:status, timestamp=2026-10-30T15:11:23.327, value=Draft                                                                             
 C103                                              column=author:name, timestamp=2026-10-30T15:11:23.417, value=Priya                                                                                 
 C103                                              column=content:body, timestamp=2026-10-30T15:11:23.389, value=Learn HTML and CSS                                                                   
 C103                                              column=content:title, timestamp=2026-10-30T15:11:23.368, value=Web Development                                                                     
 C103                                              column=metadata:category, timestamp=2026-10-30T15:11:23.442, value=Technology                                                                      
 C103                                              column=metadata:status, timestamp=2026-10-30T15:11:24.180, value=Published                                                                         
3 row(s)
Took 0.0465 seconds                                                                                                                                                                                   
hbase:084:0> delete 'CMS', 'C102', 'content:body'
Took 0.0047 seconds                                                                                                                                                                                   
hbase:085:0> deleteall 'CMS', 'C103'
Took 0.0055 seconds                                                                                                                                                                                   
hbase:086:0> scan 'CMS'
ROW                                                COLUMN+CELL                                                                                                                                        
 C101                                              column=author:name, timestamp=2026-10-30T15:11:23.088, value=Rohit                                                                                 
 C101                                              column=content:body, timestamp=2026-10-30T15:11:23.063, value=MongoDB is a NoSQL database                                                          
 C101                                              column=content:title, timestamp=2026-10-30T15:11:35.552, value=Introduction to HBase                                                               
 C101                                              column=metadata:category, timestamp=2026-10-30T15:11:23.117, value=Technology                                                                      
 C101                                              column=metadata:status, timestamp=2026-10-30T15:11:35.578, value=Updated                                                                           
 C102                                              column=author:name, timestamp=2026-10-30T15:11:23.257, value=Amit                                                                                  
 C102                                              column=content:title, timestamp=2026-10-30T15:11:23.202, value=Learning Python                                                                     
 C102                                              column=metadata:category, timestamp=2026-10-30T15:11:23.295, value=Programming                                                                     
 C102                                              column=metadata:status, timestamp=2026-10-30T15:11:23.327, value=Draft                                                                             
2 row(s)
Took 0.0155 seconds                                                                                                                                                                                   
hbase:087:0> 
```


## Question 5
Implement a simple Blogging Platform using HBase. Create suitable column families for blog details, author information, and comments. Insert at least three blog records and retrieve a particular blog using its row key.
### Commands and Output
```javascript
create 'Blog', 'details', 'author', 'comments'

# Insert blog 1
put 'Blog', 'B101', 'details:title', 'Introduction to MongoDB'
put 'Blog', 'B101', 'details:category', 'Technology'
put 'Blog', 'B101', 'author:name', 'Rohit'
put 'Blog', 'B101', 'author:email', 'rohit@gmail.com'
put 'Blog', 'B101', 'comments:comment1', 'Great blog!'

# Insert blog 2
put 'Blog', 'B102', 'details:title', 'Learning Python'
put 'Blog', 'B102', 'details:category', 'Programming'
put 'Blog', 'B102', 'author:name', 'Amit'
put 'Blog', 'B102', 'author:email', 'amit@gmail.com'
put 'Blog', 'B102', 'comments:comment1', 'Very useful!'

# Insert blog 3
put 'Blog', 'B103', 'details:title', 'Web Development'
put 'Blog', 'B103', 'details:category', 'Technology'
put 'Blog', 'B103', 'author:name', 'Priya'
put 'Blog', 'B103', 'author:email', 'priya@gmail.com'
put 'Blog', 'B103', 'comments:comment1', 'Excellent article!'

# Display all blogs
scan 'Blog'

# Retrieve a particular blog using row key
get 'Blog', 'B101'

get 'Blog', 'B102'

get 'Blog', 'B103'
```

## Question 6
Demonstrate the column-family data model in HBase by creating a table with multiple column families and different qualifiers. Explain through your implementation how HBase stores columns within column families.
### Commands and Output
```javascript
create 'Student', 'personal', 'academic', 'contact'

# Student 101
put 'Student', '101', 'personal:name', 'Rohit'
put 'Student', '101', 'personal:department', 'BCA'
put 'Student', '101', 'academic:semester', '5'
put 'Student', '101', 'academic:cgpa', '8.5'
put 'Student', '101', 'contact:email', 'rohit@gmail.com'
put 'Student', '101', 'contact:city', 'Chhapra'

# Student 102
put 'Student', '102', 'personal:name', 'Amit'
put 'Student', '102', 'personal:department', 'BCA'
put 'Student', '102', 'academic:semester', '5'
put 'Student', '102', 'academic:cgpa', '8.2'
put 'Student', '102', 'contact:email', 'amit@gmail.com'
put 'Student', '102', 'contact:city', 'Patna'

# Student 103
put 'Student', '103', 'personal:name', 'Rahul'
put 'Student', '103', 'personal:department', 'MCA'
put 'Student', '103', 'academic:semester', '3'
put 'Student', '103', 'academic:cgpa', '8.7'
put 'Student', '103', 'contact:email', 'rahul@gmail.com'
put 'Student', '103', 'contact:city', 'Delhi'

# Display all records
scan 'Student'

# Retrieve one student
get 'Student', '101'

# Retrieve specific column family
get 'Student', '101', {COLUMN => 'personal'}

# Retrieve specific qualifier
get 'Student', '101', {COLUMN => 'academic:cgpa'}
```

## Question 7
Create an HBase table named WebsiteCounter to maintain page-view counters. Implement increment operations and display the updated counter values for different pages.
### Commands and Output
```javascript
create 'WebsiteCounter', 'views'

# Initialize page counters
put 'WebsiteCounter', 'home', 'views:count', '0'
put 'WebsiteCounter', 'about', 'views:count', '0'
put 'WebsiteCounter', 'products', 'views:count', '0'

# Increment page-view counters
incr 'WebsiteCounter', 'home', 'views:count', 1
incr 'WebsiteCounter', 'home', 'views:count', 1
incr 'WebsiteCounter', 'home', 'views:count', 1

incr 'WebsiteCounter', 'about', 'views:count', 1
incr 'WebsiteCounter', 'about', 'views:count', 1

incr 'WebsiteCounter', 'products', 'views:count', 1
incr 'WebsiteCounter', 'products', 'views:count', 1
incr 'WebsiteCounter', 'products', 'views:count', 1
incr 'WebsiteCounter', 'products', 'views:count', 1

# Display updated counter values
get 'WebsiteCounter', 'home'
get 'WebsiteCounter', 'about'
get 'WebsiteCounter', 'products'

# Display all page counters
scan 'WebsiteCounter'
```

## Question 8
Implement expiring usage/session data using HBase. Design a table for user sessions and configure a TTL (Time-To-Live) for the required column family. Insert session records and
verify their expiration behavior.
### Commands and Output
```javascript
# Create UserSessions table with TTL of 60 seconds
create 'UserSessions',
  { NAME => 'session', TTL => 60 },
  { NAME => 'user', VERSIONS => 1 }

# Insert session records
put 'UserSessions', 'S101', 'session:session_id', 'S101'
put 'UserSessions', 'S101', 'session:login_time', '10:00'
put 'UserSessions', 'S101', 'user:user_id', '101'
put 'UserSessions', 'S101', 'user:username', 'Rohit'

put 'UserSessions', 'S102', 'session:session_id', 'S102'
put 'UserSessions', 'S102', 'session:login_time', '10:05'
put 'UserSessions', 'S102', 'user:user_id', '102'
put 'UserSessions', 'S102', 'user:username', 'Amit'

put 'UserSessions', 'S103', 'session:session_id', 'S103'
put 'UserSessions', 'S103', 'session:login_time', '10:10'
put 'UserSessions', 'S103', 'user:user_id', '103'
put 'UserSessions', 'S103', 'user:username', 'Rahul'

# Display session records
scan 'UserSessions'

# Retrieve a particular session
get 'UserSessions', 'S101'

# Check TTL configuration
describe 'UserSessions'

# Wait 60 seconds, then check again
scan 'UserSessions'
```
## Question 9
Design an HBase table for a large-scale application and explain how its row-key design can support horizontal scaling. Demonstrate insertion of records using a suitable row-key strategy.
### Commands and Output
```javascript
create 'LargeScaleApp', 'user', 'activity'

# Salted row keys (prefix distributes records across regions)

put 'LargeScaleApp', '0_USER101', 'user:name', 'Rohit'
put 'LargeScaleApp', '0_USER101', 'user:email', 'rohit@gmail.com'
put 'LargeScaleApp', '0_USER101', 'activity:type', 'Login'

put 'LargeScaleApp', '1_USER102', 'user:name', 'Amit'
put 'LargeScaleApp', '1_USER102', 'user:email', 'amit@gmail.com'
put 'LargeScaleApp', '1_USER102', 'activity:type', 'Purchase'

put 'LargeScaleApp', '2_USER103', 'user:name', 'Rahul'
put 'LargeScaleApp', '2_USER103', 'user:email', 'rahul@gmail.com'
put 'LargeScaleApp', '2_USER103', 'activity:type', 'Logout'

put 'LargeScaleApp', '3_USER104', 'user:name', 'Priya'
put 'LargeScaleApp', '3_USER104', 'user:email', 'priya@gmail.com'
put 'LargeScaleApp', '3_USER104', 'activity:type', 'Login'

put 'LargeScaleApp', '4_USER105', 'user:name', 'Neha'
put 'LargeScaleApp', '4_USER105', 'user:email', 'neha@gmail.com'
put 'LargeScaleApp', '4_USER105', 'activity:type', 'Purchase'

# Display all records
scan 'LargeScaleApp'

# Retrieve a particular user
get 'LargeScaleApp', '0_USER101'

get 'LargeScaleApp', '2_USER103'
```

## Question 10
Create an HBase table with multiple regions and demonstrate how HBase distributes data across regions. Explain the role of RegionServers in achieving scalability and availability.
### Commands and Output
```javascript
# Create table with multiple regions using pre-split keys
create 'MultiRegionTable',
  { NAME => 'info' },
  { SPLITS => ['100', '200', '300', '400'] }

# Insert records
put 'MultiRegionTable', '050', 'info:name', 'Rohit'
put 'MultiRegionTable', '075', 'info:city', 'Chhapra'

put 'MultiRegionTable', '150', 'info:name', 'Amit'
put 'MultiRegionTable', '175', 'info:city', 'Patna'

put 'MultiRegionTable', '250', 'info:name', 'Rahul'
put 'MultiRegionTable', '275', 'info:city', 'Delhi'

put 'MultiRegionTable', '350', 'info:name', 'Priya'
put 'MultiRegionTable', '375', 'info:city', 'Mumbai'

put 'MultiRegionTable', '450', 'info:name', 'Neha'
put 'MultiRegionTable', '475', 'info:city', 'Pune'

# Display all records
scan 'MultiRegionTable'

# Check table regions
list_regions 'MultiRegionTable'

# Display table description
describe 'MultiRegionTable'
```


## Question 11
Install and configure Apache Cassandra. Create a keyspace named CollegeDB with an appropriate replication factor and create a Students table. Insert and retrieve at least five student records.
### Commands and Output
```javascript
-- Open Cassandra CQLSH
cqlsh

-- Create Keyspace
CREATE KEYSPACE CollegeDB
WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 1
};

-- Use Keyspace
USE CollegeDB;

-- Create Students Table
CREATE TABLE Students (
  student_id int PRIMARY KEY,
  name text,
  department text,
  semester int,
  cgpa float
);

-- Insert five student records
INSERT INTO Students VALUES (101, 'Rohit', 'BCA', 5, 8.5);
INSERT INTO Students VALUES (102, 'Amit', 'BCA', 5, 8.2);
INSERT INTO Students VALUES (103, 'Rahul', 'MCA', 3, 8.7);
INSERT INTO Students VALUES (104, 'Priya', 'BCA', 5, 9.1);
INSERT INTO Students VALUES (105, 'Neha', 'MCA', 3, 8.9);

-- Retrieve all student records
SELECT * FROM Students;

-- Retrieve a particular student
SELECT * FROM Students WHERE student_id = 101;
```

## Question 12
Using Apache Cassandra, perform CRUD operations on an Employees table. Demonstrate INSERT, SELECT, UPDATE, and DELETE operations using CQL.
### Commands and Output
```javascript
-- Open Cassandra CQLSH
cqlsh

-- Use Keyspace
USE CollegeDB;

-- Create Employees Table
CREATE TABLE Employees (
  employee_id int PRIMARY KEY,
  name text,
  department text,
  city text,
  salary double
);

-- INSERT: Add employee records
INSERT INTO Employees (employee_id, name, department, city, salary)
VALUES (101, 'Rohit', 'IT', 'Chhapra', 30000);

INSERT INTO Employees (employee_id, name, department, city, salary)
VALUES (102, 'Amit', 'HR', 'Patna', 25000);

INSERT INTO Employees (employee_id, name, department, city, salary)
VALUES (103, 'Rahul', 'Finance', 'Delhi', 35000);

-- SELECT: Retrieve all employees
SELECT * FROM Employees;

-- SELECT: Retrieve a specific employee
SELECT * FROM Employees WHERE employee_id = 101;

-- UPDATE: Modify employee details
UPDATE Employees
SET salary = 40000, city = 'Mumbai'
WHERE employee_id = 101;

-- Verify updated record
SELECT * FROM Employees WHERE employee_id = 101;

-- DELETE: Delete an employee record
DELETE FROM Employees WHERE employee_id = 102;

-- Verify deletion
SELECT * FROM Employees;
```

## Question 13
Design a Cassandra database for an event logging application. Create an appropriate table, insert multiple events, and write CQL queries to retrieve events for a particular user and time period.
### Commands and Output
```javascript
-- Open Cassandra CQLSH
cqlsh

-- Use Keyspace
USE CollegeDB;

-- Create EventLog Table
CREATE TABLE EventLog (
  user_id int,
  event_time timestamp,
  event_id int,
  event_type text,
  description text,
  ip_address text,
  PRIMARY KEY (user_id, event_time, event_id)
) WITH CLUSTERING ORDER BY (event_time DESC);

-- Insert multiple events
INSERT INTO EventLog VALUES
(101, '2026-10-30 09:00:00', 1, 'Login', 'User logged in', '192.168.1.1');

INSERT INTO EventLog VALUES
(101, '2026-10-30 09:15:00', 2, 'File Upload', 'File uploaded', '192.168.1.1');

INSERT INTO EventLog VALUES
(101, '2026-10-30 10:00:00', 3, 'Logout', 'User logged out', '192.168.1.1');

INSERT INTO EventLog VALUES
(102, '2026-10-30 09:30:00', 4, 'Login', 'User logged in', '192.168.1.2');

INSERT INTO EventLog VALUES
(102, '2026-10-30 10:30:00', 5, 'Password Change', 'Password updated', '192.168.1.2');

-- Retrieve all events
SELECT * FROM EventLog;

-- Retrieve events for a particular user
SELECT * FROM EventLog
WHERE user_id = 101;

-- Retrieve events for user 101 within a time period
SELECT * FROM EventLog
WHERE user_id = 101
AND event_time >= '2026-10-30 09:00:00'
AND event_time <= '2026-10-30 10:00:00';

-- Retrieve login events for user 101
SELECT * FROM EventLog
WHERE user_id = 101
AND event_time >= '2026-10-30 09:00:00'
AND event_time <= '2026-10-30 10:00:00'
AND event_type = 'Login'
ALLOW FILTERING;
```

## Question 14
Demonstrate availability and consistency in Cassandra by creating a keyspace with a suitable replication strategy. Perform read/write operations using different consistency levels such as ONE, QUORUM, and ALL, and observe the behavior.
### Commands and Output
```javascript
-- Open Cassandra CQLSH
cqlsh

-- Create Keyspace with replication factor 3
CREATE KEYSPACE AvailabilityDB
WITH replication = {
  'class': 'NetworkTopologyStrategy',
  'datacenter1': 3
};

-- Use Keyspace
USE AvailabilityDB;

-- Create Table
CREATE TABLE Student (
  student_id int PRIMARY KEY,
  name text,
  department text,
  cgpa float
);

-- Set Consistency Level ONE
CONSISTENCY ONE;

-- Insert record
INSERT INTO Student VALUES (101, 'Rohit', 'BCA', 8.5);

-- Read record
SELECT * FROM Student WHERE student_id = 101;

-- Set Consistency Level QUORUM
CONSISTENCY QUORUM;

-- Insert another record
INSERT INTO Student VALUES (102, 'Amit', 'BCA', 8.2);

-- Read record
SELECT * FROM Student WHERE student_id = 102;

-- Set Consistency Level ALL
CONSISTENCY ALL;

-- Insert another record
INSERT INTO Student VALUES (103, 'Rahul', 'MCA', 8.7);

-- Read record
SELECT * FROM Student WHERE student_id = 103;

-- Display all records
SELECT * FROM Student;

-- Check current consistency level
CONSISTENCY;
```

## Question 15
Design and implement a column-oriented NoSQL application using HBase or Cassandra for any one of the following: Event Logging, Content Management, Blogging Platform, Counters, or Expiring Usage. Demonstrate database/table creation, data insertion, querying, updating, deletion, and explain how consistency, availability, transactions, query features,
and scaling are handled by the selected database.
### Commands and Output
```javascript
-- Open Cassandra shell
cqlsh

-- 1. Create Keyspace
CREATE KEYSPACE EventDB
WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 1
};

USE EventDB;

-- 2. Create EventLog Table
CREATE TABLE EventLog (
  user_id int,
  event_time timestamp,
  event_id int,
  event_type text,
  description text,
  ip_address text,
  PRIMARY KEY (user_id, event_time, event_id)
) WITH CLUSTERING ORDER BY (event_time DESC);

-- 3. Insert Event Records
INSERT INTO EventLog VALUES
(101, '2026-10-30 09:00:00', 1, 'Login', 'User logged in', '192.168.1.1');

INSERT INTO EventLog VALUES
(101, '2026-10-30 09:15:00', 2, 'File Upload', 'File uploaded', '192.168.1.1');

INSERT INTO EventLog VALUES
(101, '2026-10-30 10:00:00', 3, 'Logout', 'User logged out', '192.168.1.1');

INSERT INTO EventLog VALUES
(102, '2026-10-30 09:30:00', 4, 'Login', 'User logged in', '192.168.1.2');

INSERT INTO EventLog VALUES
(102, '2026-10-30 10:30:00', 5, 'Password Change', 'Password updated', '192.168.1.2');

-- 4. Query All Events
SELECT * FROM EventLog;

-- 5. Query Events of a Particular User
SELECT * FROM EventLog
WHERE user_id = 101;

-- 6. Query Events Within a Time Period
SELECT * FROM EventLog
WHERE user_id = 101
AND event_time >= '2026-10-30 09:00:00'
AND event_time <= '2026-10-30 10:00:00';

-- 7. Update an Event
UPDATE EventLog
SET description = 'User successfully logged in'
WHERE user_id = 101
AND event_time = '2026-10-30 09:00:00'
AND event_id = 1;

-- Verify Update
SELECT * FROM EventLog
WHERE user_id = 101;

-- 8. Delete an Event
DELETE FROM EventLog
WHERE user_id = 102
AND event_time = '2026-10-30 09:30:00'
AND event_id = 4;

-- 9. Display Final Records
SELECT * FROM EventLog;
```