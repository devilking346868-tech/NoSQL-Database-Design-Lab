# Lab Sheet-05: NoSQL Database Design Lab
# BCA V Semester / III Years (Session 2026- 2027)

## Question 1
Install and configure Riak KV on a Linux system. Create a bucket named students and perform basic key-value operations such as storing, retrieving, updating, and deleting student records.

### Commands and Output

```cmd
# Install Riak KV (Ubuntu/Debian)
$ sudo apt update
$ sudo apt install -y libssl-dev libncurses5 curl jq
$ sudo dpkg -i riak_3.0.16-OTP22_amd64.deb
Setting up riak (3.0.16) ...

# Start and verify Riak
$ sudo riak start
$ riak ping
pong
$ riak version
3.0.16
$ curl -i http://localhost:8098/ping
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 2

OK

# Note: In Riak, a bucket is created automatically when the first key is stored in it.

# STORE (PUT)
$ curl -i -XPUT -H "Content-Type: application/json" \
  -d '{"RollNumber":101,"Name":"Rohit","Department":"BCA","Semester":5,"CGPA":8.5}' \
  http://localhost:8098/buckets/students/keys/101
HTTP/1.1 204 No Content

# RETRIEVE (GET)
$ curl -s http://localhost:8098/buckets/students/keys/101 | jq
{
  "RollNumber": 101,
  "Name": "Rohit",
  "Department": "BCA",
  "Semester": 5,
  "CGPA": 8.5
}

# UPDATE (PUT with the same key overwrites the value)
$ curl -i -XPUT -H "Content-Type: application/json" \
  -d '{"RollNumber":101,"Name":"Rohit","Department":"BCA","Semester":6,"CGPA":9.0}' \
  http://localhost:8098/buckets/students/keys/101
HTTP/1.1 204 No Content

$ curl -s http://localhost:8098/buckets/students/keys/101 | jq
{
  "RollNumber": 101,
  "Name": "Rohit",
  "Department": "BCA",
  "Semester": 6,
  "CGPA": 9.0
}

# DELETE
$ curl -i -XDELETE http://localhost:8098/buckets/students/keys/101
HTTP/1.1 204 No Content

# Verify deletion
$ curl -i http://localhost:8098/buckets/students/keys/101
HTTP/1.1 404 Object Not Found
not found
```


## Question 2
Using Riak KV, create a user_sessions bucket to store user session information. Store session ID, user ID, login time, and session status, and retrieve session information using its key.

### Commands and Output

```javascript
# Session ID is used as the key
$ curl -i -XPUT -H "Content-Type: application/json" \
  -d '{"SessionID":"S1001","UserID":101,"LoginTime":"2026-10-30T10:15:00","Status":"active"}' \
  http://localhost:8098/buckets/user_sessions/keys/S1001
HTTP/1.1 204 No Content

$ curl -i -XPUT -H "Content-Type: application/json" \
  -d '{"SessionID":"S1002","UserID":102,"LoginTime":"2026-10-30T10:45:00","Status":"expired"}' \
  http://localhost:8098/buckets/user_sessions/keys/S1002
HTTP/1.1 204 No Content

# Retrieve session by key
$ curl -s http://localhost:8098/buckets/user_sessions/keys/S1001 | jq
{
  "SessionID": "S1001",
  "UserID": 101,
  "LoginTime": "2026-10-30T10:15:00",
  "Status": "active"
}

$ curl -s http://localhost:8098/buckets/user_sessions/keys/S1002 | jq
{
  "SessionID": "S1002",
  "UserID": 102,
  "LoginTime": "2026-10-30T10:45:00",
  "Status": "expired"
}

# List keys of the bucket (for demonstration only, not recommended in production)
$ curl -s "http://localhost:8098/buckets/user_sessions/keys?keys=true"
{"keys":["S1002","S1001"]}
```


## Question 3
Design a Riak KV application for storing user profiles and preferences. Store details such as name, email, city, language, theme, and notification preferences. Demonstrate PUT and GET operations.

### Commands and Output

```javascript
# PUT user profile (key = user id)
$ curl -i -XPUT -H "Content-Type: application/json" \
  -d '{
    "name":"Rohit Kumar",
    "email":"rohit@example.com",
    "city":"Bulandshahr",
    "preferences":{
      "language":"Hindi",
      "theme":"dark",
      "notifications":{"email":true,"sms":false,"push":true}
    }
  }' \
  http://localhost:8098/buckets/user_profiles/keys/user101
HTTP/1.1 204 No Content

$ curl -i -XPUT -H "Content-Type: application/json" \
  -d '{
    "name":"Amit Sharma",
    "email":"amit@example.com",
    "city":"Delhi",
    "preferences":{
      "language":"English",
      "theme":"light",
      "notifications":{"email":true,"sms":true,"push":false}
    }
  }' \
  http://localhost:8098/buckets/user_profiles/keys/user102
HTTP/1.1 204 No Content

# GET user profile
$ curl -s http://localhost:8098/buckets/user_profiles/keys/user101 | jq
{
  "name": "Rohit Kumar",
  "email": "rohit@example.com",
  "city": "Bulandshahr",
  "preferences": {
    "language": "Hindi",
    "theme": "dark",
    "notifications": {
      "email": true,
      "sms": false,
      "push": true
    }
  }
}

# GET only one preference using jq
$ curl -s http://localhost:8098/buckets/user_profiles/keys/user101 | jq '.preferences.theme'
"dark"
```


## Question 4
Implement a shopping cart application using Riak KV. Store a shopping cart for each user containing product IDs, quantities, and prices. Demonstrate adding, updating, retrieving, and removing products from the cart.

### Commands and Output

```javascript
# Design: bucket = carts, key = cart:<userID>, value = JSON document

# CREATE cart with first product
$ curl -i -XPUT -H "Content-Type: application/json" \
  -d '{"UserID":101,"Items":[{"ProductID":"P1","Quantity":2,"Price":500}]}' \
  http://localhost:8098/buckets/carts/keys/cart:101
HTTP/1.1 204 No Content

# ADD a product (read - modify - write)
$ curl -s http://localhost:8098/buckets/carts/keys/cart:101 \
  | jq '.Items += [{"ProductID":"P2","Quantity":1,"Price":1200}]' > cart101.json
$ curl -i -XPUT -H "Content-Type: application/json" \
  -d @cart101.json http://localhost:8098/buckets/carts/keys/cart:101
HTTP/1.1 204 No Content

# RETRIEVE cart
$ curl -s http://localhost:8098/buckets/carts/keys/cart:101 | jq -c
{"UserID":101,"Items":[{"ProductID":"P1","Quantity":2,"Price":500},{"ProductID":"P2","Quantity":1,"Price":1200}]}

# UPDATE quantity of product P1 to 3
$ curl -s http://localhost:8098/buckets/carts/keys/cart:101 \
  | jq '(.Items[] | select(.ProductID=="P1") | .Quantity) = 3' > cart101.json
$ curl -i -XPUT -H "Content-Type: application/json" \
  -d @cart101.json http://localhost:8098/buckets/carts/keys/cart:101
HTTP/1.1 204 No Content

$ curl -s http://localhost:8098/buckets/carts/keys/cart:101 | jq -c
{"UserID":101,"Items":[{"ProductID":"P1","Quantity":3,"Price":500},{"ProductID":"P2","Quantity":1,"Price":1200}]}

# REMOVE product P2 from the cart
$ curl -s http://localhost:8098/buckets/carts/keys/cart:101 \
  | jq '.Items |= map(select(.ProductID != "P2"))' > cart101.json
$ curl -i -XPUT -H "Content-Type: application/json" \
  -d @cart101.json http://localhost:8098/buckets/carts/keys/cart:101
HTTP/1.1 204 No Content

$ curl -s http://localhost:8098/buckets/carts/keys/cart:101 | jq -c
{"UserID":101,"Items":[{"ProductID":"P1","Quantity":3,"Price":500}]}

# EMPTY the cart completely (delete key)
$ curl -i -XDELETE http://localhost:8098/buckets/carts/keys/cart:101
HTTP/1.1 204 No Content
```


## Question 5
Demonstrate the structure of data in a key-value store using Riak. Store different types of values such as strings, JSON documents, and lists. Retrieve the stored values and explain the role of bucket, key, and value.

### Commands and Output

```javascript
# 1. STRING value
$ curl -i -XPUT -H "Content-Type: text/plain" \
  -d 'Hello Riak' http://localhost:8098/buckets/demo/keys/greeting
HTTP/1.1 204 No Content

$ curl -s http://localhost:8098/buckets/demo/keys/greeting
Hello Riak

# 2. JSON document value
$ curl -i -XPUT -H "Content-Type: application/json" \
  -d '{"Name":"Rohit","Department":"BCA","CGPA":8.5}' \
  http://localhost:8098/buckets/demo/keys/student101
HTTP/1.1 204 No Content

$ curl -s http://localhost:8098/buckets/demo/keys/student101
{"Name":"Rohit","Department":"BCA","CGPA":8.5}

# 3. LIST value (stored as a JSON array)
$ curl -i -XPUT -H "Content-Type: application/json" \
  -d '["Java","Python","MongoDB","Riak"]' \
  http://localhost:8098/buckets/demo/keys/skills
HTTP/1.1 204 No Content

$ curl -s http://localhost:8098/buckets/demo/keys/skills
["Java","Python","MongoDB","Riak"]

# List all keys of the demo bucket
$ curl -s "http://localhost:8098/buckets/demo/keys?keys=true"
{"keys":["skills","greeting","student101"]}

EXPLANATION:

1. Bucket
   - A bucket is a logical namespace used to group related keys (like a table or collection).
   - Example: students, user_sessions, carts, demo.
   - Buckets can have their own properties (n_val, r, w, etc.).

2. Key
   - A key is the unique identifier of an object inside a bucket.
   - Data is always accessed using bucket + key.
   - Example: greeting, student101, skills.

3. Value
   - A value is the actual data stored against a key.
   - Riak treats a value as an opaque blob; it can be a string, JSON, list, image, etc.
   - The Content-Type header tells Riak/clients how to interpret the value.

Structure:  Bucket -> Key -> Value
Example:    demo -> student101 -> {"Name":"Rohit","Department":"BCA","CGPA":8.5}
```


## Question 6
Demonstrate consistency in Riak KV by configuring suitable read and write quorum values. Perform read/write operations and explain how Riak handles consistency in a distributed environment.

### Commands and Output

```javascript
# Check the current bucket properties
$ curl -s http://localhost:8098/buckets/students/props | jq '.props | {n_val, r, w, dw, allow_mult, last_write_wins}'
{
  "n_val": 3,
  "r": "quorum",
  "w": "quorum",
  "dw": "quorum",
  "allow_mult": false,
  "last_write_wins": false
}

# Set bucket level quorum: N=3, R=2, W=2
$ curl -i -XPUT -H "Content-Type: application/json" \
  -d '{"props":{"n_val":3,"r":2,"w":2}}' \
  http://localhost:8098/buckets/students/props
HTTP/1.1 204 No Content

# Write with request level quorum (w=2)
$ curl -i -XPUT -H "Content-Type: application/json" \
  -d '{"Name":"Amit","CGPA":8.2}' \
  "http://localhost:8098/buckets/students/keys/102?w=2"
HTTP/1.1 204 No Content

# Read with request level quorum (r=2)
$ curl -s "http://localhost:8098/buckets/students/keys/102?r=2"
{"Name":"Amit","CGPA":8.2}

# Strong read/write (all replicas must respond): r=3, w=3
$ curl -i -XPUT -H "Content-Type: application/json" \
  -d '{"Name":"Amit","CGPA":8.4}' \
  "http://localhost:8098/buckets/students/keys/102?w=3"
HTTP/1.1 204 No Content

$ curl -s "http://localhost:8098/buckets/students/keys/102?r=3"
{"Name":"Amit","CGPA":8.4}

# Fast but weaker consistency: r=1, w=1
$ curl -s "http://localhost:8098/buckets/students/keys/102?r=1"
{"Name":"Amit","CGPA":8.4}

EXPLANATION:

1. N, R, W values
   - N (n_val) = number of replicas stored for every key (default 3).
   - R = number of replicas that must respond to a read.
   - W = number of replicas that must acknowledge a write.

2. Consistency rule
   - If R + W > N (for example 2 + 2 > 3), every read quorum overlaps with the latest
     write quorum, so the latest value is returned (strong-like consistency).
   - If R + W <= N (for example 1 + 1), reads and writes are faster, but stale data
     can be returned (eventual consistency).

3. How Riak handles consistency in a distributed environment
   - Riak is AP-oriented in the CAP theorem: it favours Availability and Partition tolerance
     and provides eventual consistency.
   - Vector clocks / dotted version vectors track the history of each object and detect
     concurrent updates.
   - Read repair: when a read finds out-of-date replicas, Riak updates them in the background.
   - Hinted handoff: if a node is down, another node temporarily holds the write and hands
     it back when the original node recovers (sloppy quorum).
   - Active anti-entropy (AAE): background process that compares replicas using hash trees
     and repairs differences.
   - Conflict resolution: either last-write-wins or siblings (allow_mult=true) resolved by
     the application.
```


## Question 7
Design a Riak-based application that demonstrates scaling. Create multiple buckets and insert a large number of key-value records. Explain how Riak distributes data across nodes and supports horizontal scaling.

### Commands and Output

```javascript
# Insert 1000 records into each of 3 buckets
$ for bucket in orders products customers; do
>   for i in $(seq 1 1000); do
>     curl -s -XPUT -H "Content-Type: application/json" \
>       -d "{\"id\":$i,\"bucket\":\"$bucket\",\"value\":\"data$i\"}" \
>       http://localhost:8098/buckets/$bucket/keys/$i > /dev/null
>   done
> done

# Verify one record from each bucket
$ curl -s http://localhost:8098/buckets/orders/keys/500
{"id":500,"bucket":"orders","value":"data500"}
$ curl -s http://localhost:8098/buckets/products/keys/750
{"id":750,"bucket":"products","value":"data750"}
$ curl -s http://localhost:8098/buckets/customers/keys/1000
{"id":1000,"bucket":"customers","value":"data1000"}

# Count the keys in a bucket (demonstration only)
$ curl -s "http://localhost:8098/buckets/orders/keys?keys=true" | jq '.keys | length'
1000

# Check the cluster status
$ sudo riak admin member-status
================================= Membership ==================================
Status     Ring    Pending    Node
-------------------------------------------------------------------------------
valid     100.0%      --      'riak@127.0.0.1'
-------------------------------------------------------------------------------
Valid:1 / Leaving:0 / Exiting:0 / Joining:0 / Down:0

# Add a new node to the cluster (run on the new node riak@192.168.1.12)
$ sudo riak admin cluster join riak@192.168.1.11
Success: staged join request for 'riak@192.168.1.12' to 'riak@192.168.1.11'
$ sudo riak admin cluster plan
$ sudo riak admin cluster commit
Cluster changes committed

$ sudo riak admin member-status
================================= Membership ==================================
Status     Ring    Pending    Node
-------------------------------------------------------------------------------
valid      50.0%      --      'riak@192.168.1.11'
valid      50.0%      --      'riak@192.168.1.12'
-------------------------------------------------------------------------------
Valid:2 / Leaving:0 / Exiting:0 / Joining:0 / Down:0

EXPLANATION:

1. Consistent hashing
   - Riak hashes bucket + key (SHA-1) and maps it to a position on a fixed 160-bit ring.

2. Ring and vnodes
   - The ring is divided into a fixed number of partitions (default 64). Each partition
     is managed by a virtual node (vnode).
   - Vnodes are distributed equally among the physical nodes.

3. Replication
   - Every key is stored on N consecutive vnodes (default N = 3) on different nodes,
     so data stays available if a node fails.

4. Horizontal scaling
   - When a node is added, the ring is rebalanced and some vnodes (and their data)
     are handed off to the new node automatically.
   - No downtime and no manual re-sharding is needed; capacity and throughput grow
     almost linearly with the number of nodes.
   - There is no master node, so there is no single point of failure.
```


## Question 8
Implement a multi-operation transaction-like scenario using Riak KV for a shopping application. Perform multiple related operations such as adding an item to a cart, updating its quantity, and updating the cart total. Discuss the limitations of transactions in a key-value database.

### Commands and Output

```javascript
# Transaction-like scenario on cart:102 using a small shell script

$ cat cart_txn.sh
#!/bin/bash
URL=http://localhost:8098/buckets/carts/keys/cart:102

# Step 1: Create empty cart
curl -s -XPUT -H "Content-Type: application/json" \
  -d '{"UserID":102,"Items":[],"Total":0}' $URL

# Step 2: Add item
curl -s $URL | jq '.Items += [{"ProductID":"P1","Quantity":1,"Price":500}]' > tmp.json
curl -s -XPUT -H "Content-Type: application/json" -d @tmp.json $URL

# Step 3: Update quantity
curl -s $URL | jq '(.Items[] | select(.ProductID=="P1") | .Quantity) = 4' > tmp.json
curl -s -XPUT -H "Content-Type: application/json" -d @tmp.json $URL

# Step 4: Recalculate and update cart total
curl -s $URL | jq '.Total = ([.Items[] | .Quantity * .Price] | add)' > tmp.json
curl -s -XPUT -H "Content-Type: application/json" -d @tmp.json $URL

$ bash cart_txn.sh

$ curl -s http://localhost:8098/buckets/carts/keys/cart:102 | jq -c
{"UserID":102,"Items":[{"ProductID":"P1","Quantity":4,"Price":500}],"Total":2000}

LIMITATIONS OF TRANSACTIONS IN A KEY-VALUE DATABASE:

1. No ACID multi-key transactions
   - Riak has no BEGIN / COMMIT / ROLLBACK. Each PUT is an independent operation.

2. No atomicity across operations
   - If the script fails after step 2, the cart is left half-updated and cannot be
     rolled back automatically.

3. No isolation
   - Two clients modifying the same cart at the same time can overwrite each other
     (lost update) or create sibling versions.

4. Eventual consistency
   - Replicas may be temporarily different, so a read can return an older cart.

5. Application-level handling needed
   - Conflict resolution, retries, idempotent operations, and compensating actions
     must be written in the application.

6. Possible workarounds
   - Keep related data in a single value (one JSON cart document) so that one PUT
     updates everything atomically for that key.
   - Use Riak Data Types (counters, maps, sets) for conflict-free updates.
   - Use strongly consistent buckets (Riak KV strong consistency mode) for
     single-key compare-and-set style operations.
```


## Question 9
Using Riak, implement query-by-data functionality for user records. Store JSON documents containing user information and demonstrate how application-level logic can be used to locate users based on attributes such as city, age, or preferences.

### Commands and Output

```javascript
# Store user records
$ curl -s -XPUT -H "Content-Type: application/json" \
  -d '{"name":"Rohit","city":"Bulandshahr","age":21,"preferences":["cricket","music"]}' \
  http://localhost:8098/buckets/users/keys/u1
$ curl -s -XPUT -H "Content-Type: application/json" \
  -d '{"name":"Amit","city":"Delhi","age":22,"preferences":["music","movies"]}' \
  http://localhost:8098/buckets/users/keys/u2
$ curl -s -XPUT -H "Content-Type: application/json" \
  -d '{"name":"Priya","city":"Delhi","age":20,"preferences":["reading","cricket"]}' \
  http://localhost:8098/buckets/users/keys/u3

# Application-level search script (Python)
$ cat search_users.py
import requests

BASE = "http://localhost:8098/buckets/users"

def get_all_users():
    keys = requests.get(BASE + "/keys?keys=true").json()["keys"]
    return {k: requests.get(f"{BASE}/keys/{k}").json() for k in keys}

users = get_all_users()

print("Users in Delhi:")
for k, u in users.items():
    if u["city"] == "Delhi":
        print(" ", k, u["name"])

print("Users with age >= 21:")
for k, u in users.items():
    if u["age"] >= 21:
        print(" ", k, u["name"], u["age"])

print("Users who like cricket:")
for k, u in users.items():
    if "cricket" in u["preferences"]:
        print(" ", k, u["name"])

$ python3 search_users.py
Users in Delhi:
  u2 Amit
  u3 Priya
Users with age >= 21:
  u1 Rohit 21
  u2 Amit 22
Users who like cricket:
  u1 Rohit
  u3 Priya

# Better approach: Secondary Index (2i) - requires leveldb backend
$ curl -s -XPUT -H "Content-Type: application/json" \
  -H "x-riak-index-city_bin: Delhi" \
  -H "x-riak-index-age_int: 22" \
  -d '{"name":"Amit","city":"Delhi","age":22}' \
  http://localhost:8098/buckets/users/keys/u2

$ curl -s http://localhost:8098/buckets/users/index/city_bin/Delhi
{"keys":["u2"]}

$ curl -s http://localhost:8098/buckets/users/index/age_int/21/25
{"keys":["u2"]}

OBSERVATION:
- A key-value store can only look up values by key. Searching by city, age or
  preferences needs either application logic (scan and filter), secondary indexes (2i),
  or Riak Search (Solr). Scanning all keys is slow for large data and is not
  recommended in production.
```


## Question 10
Implement set operations in a Riak-based application. Create sets containing user interests or product categories and demonstrate operations such as adding elements, removing elements, checking membership, and finding common elements.

### Commands and Output

```javascript
# Create and activate a bucket type for the set data type
$ sudo riak admin bucket-type create sets '{"props":{"datatype":"set"}}'
sets created
$ sudo riak admin bucket-type activate sets
sets has been activated

# ADD elements to the set of user101
$ curl -i -XPOST -H "Content-Type: application/json" \
  -d '{"add_all":["cricket","music","movies"]}' \
  http://localhost:8098/types/sets/buckets/interests/datatypes/user101
HTTP/1.1 204 No Content

# ADD elements to the set of user102
$ curl -i -XPOST -H "Content-Type: application/json" \
  -d '{"add_all":["music","reading","travel"]}' \
  http://localhost:8098/types/sets/buckets/interests/datatypes/user102
HTTP/1.1 204 No Content

# RETRIEVE the set
$ curl -s http://localhost:8098/types/sets/buckets/interests/datatypes/user101 | jq
{
  "type": "set",
  "value": ["cricket", "movies", "music"],
  "context": "g2wAAAABaAJtAAAADCNJ..."
}

# REMOVE an element (the causal context is required for removal)
$ CTX=$(curl -s http://localhost:8098/types/sets/buckets/interests/datatypes/user101 | jq -r '.context')
$ curl -i -XPOST -H "Content-Type: application/json" \
  -d "{\"remove\":\"movies\",\"context\":\"$CTX\"}" \
  http://localhost:8098/types/sets/buckets/interests/datatypes/user101
HTTP/1.1 204 No Content

$ curl -s http://localhost:8098/types/sets/buckets/interests/datatypes/user101 | jq -c '.value'
["cricket","music"]

# CHECK MEMBERSHIP
$ curl -s http://localhost:8098/types/sets/buckets/interests/datatypes/user101 \
  | jq '.value | index("cricket") != null'
true
$ curl -s http://localhost:8098/types/sets/buckets/interests/datatypes/user101 \
  | jq '.value | index("travel") != null'
false

# COMMON ELEMENTS (intersection) of both users
$ comm -12 \
  <(curl -s http://localhost:8098/types/sets/buckets/interests/datatypes/user101 | jq -r '.value[]' | sort) \
  <(curl -s http://localhost:8098/types/sets/buckets/interests/datatypes/user102 | jq -r '.value[]' | sort)
music

OBSERVATION:
- Riak sets are CRDTs (Conflict-free Replicated Data Types). Concurrent adds and
  removes on different nodes are merged automatically without conflicts.
- Riak itself supports add and remove; operations like intersection and union are
  done at the application/client level.
```


## Question 11
Install and configure Neo4j. Create a graph containing Student, Course, and Department nodes with appropriate relationships. Insert sample data and visualize the resulting graph.

### Commands and Output

```javascript
# Install Neo4j (Ubuntu/Debian)
$ sudo apt install -y wget gnupg openjdk-17-jre
$ wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/neotechnology.gpg
$ echo 'deb [signed-by=/etc/apt/keyrings/neotechnology.gpg] https://debian.neo4j.com stable latest' | sudo tee /etc/apt/sources.list.d/neo4j.list
$ sudo apt update
$ sudo apt install -y neo4j

# Start and check service
$ sudo systemctl enable neo4j
$ sudo systemctl start neo4j
$ sudo systemctl status neo4j
● neo4j.service - Neo4j Graph Database
     Active: active (running)

# Set initial password and open cypher-shell
$ cypher-shell -u neo4j -p neo4j
Password change required
new password: ********
Connected to Neo4j using Bolt protocol version 5.x at neo4j://localhost:7687 as user neo4j.
neo4j@neo4j>

# Neo4j Browser (for visualization): http://localhost:7474
# Bolt URL: bolt://localhost:7687

# Create sample data
neo4j@neo4j> CREATE (d1:Department {DeptID:1, Name:"Computer Science"}),
                    (d2:Department {DeptID:2, Name:"Mathematics"}),
                    (c1:Course {CourseID:"C101", Title:"NoSQL Databases", Credits:4}),
                    (c2:Course {CourseID:"C102", Title:"Python Programming", Credits:4}),
                    (c3:Course {CourseID:"C103", Title:"Linear Algebra", Credits:3}),
                    (s1:Student {RollNumber:101, Name:"Rohit", Semester:5}),
                    (s2:Student {RollNumber:102, Name:"Amit", Semester:5}),
                    (s3:Student {RollNumber:103, Name:"Priya", Semester:3}),
                    (s1)-[:BELONGS_TO]->(d1),
                    (s2)-[:BELONGS_TO]->(d1),
                    (s3)-[:BELONGS_TO]->(d2),
                    (c1)-[:OFFERED_BY]->(d1),
                    (c2)-[:OFFERED_BY]->(d1),
                    (c3)-[:OFFERED_BY]->(d2),
                    (s1)-[:ENROLLED_IN]->(c1),
                    (s1)-[:ENROLLED_IN]->(c2),
                    (s2)-[:ENROLLED_IN]->(c1),
                    (s3)-[:ENROLLED_IN]->(c3);
Added 8 nodes, created 10 relationships, set 22 properties, added 8 labels

# Verify
neo4j@neo4j> MATCH (n) RETURN labels(n) AS Label, count(*) AS Total;
+----------------------------+
| Label          | Total     |
+----------------------------+
| ["Department"] | 2         |
| ["Course"]     | 3         |
| ["Student"]    | 3         |
+----------------------------+

# Visualize in Neo4j Browser
neo4j$ MATCH (n)-[r]->(m) RETURN n, r, m
(The graph shows Student nodes connected to Course nodes by ENROLLED_IN, to Department
 nodes by BELONGS_TO, and Course nodes connected to Department nodes by OFFERED_BY.)
```


## Question 12
Using Neo4j Cypher, create a social-network graph containing Person nodes and relationships such as FRIENDS_WITH, FOLLOWS, and WORKS_AT. Write queries to find a person's friends and followers.

### Commands and Output

```javascript
neo4j@neo4j> CREATE (rohit:Person {Name:"Rohit", City:"Bulandshahr"}),
                    (amit:Person {Name:"Amit", City:"Delhi"}),
                    (priya:Person {Name:"Priya", City:"Delhi"}),
                    (neha:Person {Name:"Neha", City:"Noida"}),
                    (tcs:Company {Name:"TCS"}),
                    (infosys:Company {Name:"Infosys"}),
                    (rohit)-[:FRIENDS_WITH]->(amit),
                    (rohit)-[:FRIENDS_WITH]->(priya),
                    (amit)-[:FRIENDS_WITH]->(neha),
                    (amit)-[:FOLLOWS]->(rohit),
                    (priya)-[:FOLLOWS]->(rohit),
                    (neha)-[:FOLLOWS]->(rohit),
                    (rohit)-[:FOLLOWS]->(neha),
                    (rohit)-[:WORKS_AT]->(tcs),
                    (amit)-[:WORKS_AT]->(infosys),
                    (priya)-[:WORKS_AT]->(tcs);
Added 6 nodes, created 10 relationships, set 12 properties, added 6 labels

# Find friends of Rohit
neo4j@neo4j> MATCH (p:Person {Name:"Rohit"})-[:FRIENDS_WITH]-(friend)
             RETURN friend.Name AS Friends;
+---------+
| Friends |
+---------+
| "Amit"  |
| "Priya" |
+---------+

# Find followers of Rohit
neo4j@neo4j> MATCH (follower:Person)-[:FOLLOWS]->(p:Person {Name:"Rohit"})
             RETURN follower.Name AS Followers;
+-----------+
| Followers |
+-----------+
| "Amit"    |
| "Priya"   |
| "Neha"    |
+-----------+

# Find whom Rohit follows
neo4j@neo4j> MATCH (p:Person {Name:"Rohit"})-[:FOLLOWS]->(x)
             RETURN x.Name AS Following;
+-----------+
| Following |
+-----------+
| "Neha"    |
+-----------+

# Find friends of friends of Rohit
neo4j@neo4j> MATCH (p:Person {Name:"Rohit"})-[:FRIENDS_WITH]-()-[:FRIENDS_WITH]-(fof)
             WHERE fof <> p
             RETURN DISTINCT fof.Name AS FriendOfFriend;
+----------------+
| FriendOfFriend |
+----------------+
| "Neha"         |
+----------------+

# People working at the same company as Rohit
neo4j@neo4j> MATCH (p:Person {Name:"Rohit"})-[:WORKS_AT]->(c)<-[:WORKS_AT]-(colleague)
             RETURN colleague.Name AS Colleagues, c.Name AS Company;
+------------------------+
| Colleagues | Company   |
+------------------------+
| "Priya"    | "TCS"     |
+------------------------+
```


## Question 13
Design a shopping/e-commerce graph using Neo4j containing Customer, Product, Category, and Order nodes. Create appropriate relationships and write Cypher queries to find products purchased by a particular customer.

### Commands and Output

```javascript
neo4j@neo4j> CREATE (c1:Customer {CustomerID:1, Name:"Rohit", City:"Bulandshahr"}),
                    (c2:Customer {CustomerID:2, Name:"Amit", City:"Delhi"}),
                    (cat1:Category {Name:"Electronics"}),
                    (cat2:Category {Name:"Books"}),
                    (p1:Product {ProductID:"P1", Name:"Headphones", Price:1500}),
                    (p2:Product {ProductID:"P2", Name:"Smartphone", Price:15000}),
                    (p3:Product {ProductID:"P3", Name:"NoSQL Book", Price:450}),
                    (o1:Order {OrderID:"O1", Date:date("2026-10-25")}),
                    (o2:Order {OrderID:"O2", Date:date("2026-10-28")}),
                    (o3:Order {OrderID:"O3", Date:date("2026-10-29")}),
                    (p1)-[:BELONGS_TO]->(cat1),
                    (p2)-[:BELONGS_TO]->(cat1),
                    (p3)-[:BELONGS_TO]->(cat2),
                    (c1)-[:PLACED]->(o1),
                    (c1)-[:PLACED]->(o2),
                    (c2)-[:PLACED]->(o3),
                    (o1)-[:CONTAINS {Quantity:1}]->(p1),
                    (o1)-[:CONTAINS {Quantity:1}]->(p3),
                    (o2)-[:CONTAINS {Quantity:1}]->(p2),
                    (o3)-[:CONTAINS {Quantity:2}]->(p3);
Added 11 nodes, created 12 relationships, set 24 properties, added 11 labels

# Products purchased by customer Rohit
neo4j@neo4j> MATCH (c:Customer {Name:"Rohit"})-[:PLACED]->(o:Order)-[:CONTAINS]->(p:Product)
             RETURN o.OrderID AS Order, p.Name AS Product, p.Price AS Price;
+-----------------------------------------+
| Order | Product      | Price            |
+-----------------------------------------+
| "O1"  | "Headphones" | 1500             |
| "O1"  | "NoSQL Book" | 450              |
| "O2"  | "Smartphone" | 15000            |
+-----------------------------------------+

# Total amount spent by Rohit
neo4j@neo4j> MATCH (c:Customer {Name:"Rohit"})-[:PLACED]->(:Order)-[r:CONTAINS]->(p:Product)
             RETURN sum(r.Quantity * p.Price) AS TotalSpent;
+------------+
| TotalSpent |
+------------+
| 16950      |
+------------+

# Categories of the products purchased by Rohit
neo4j@neo4j> MATCH (c:Customer {Name:"Rohit"})-[:PLACED]->()-[:CONTAINS]->(p)-[:BELONGS_TO]->(cat:Category)
             RETURN DISTINCT cat.Name AS Category;
+---------------+
| Category      |
+---------------+
| "Electronics" |
| "Books"       |
+---------------+

# Recommendation: products bought by others who bought the same products as Rohit
neo4j@neo4j> MATCH (c:Customer {Name:"Rohit"})-[:PLACED]->()-[:CONTAINS]->(p:Product)
                   <-[:CONTAINS]-()<-[:PLACED]-(other:Customer)
             WHERE other <> c
             RETURN other.Name AS OtherCustomer, p.Name AS CommonProduct;
+--------------------------------+
| OtherCustomer | CommonProduct  |
+--------------------------------+
| "Amit"        | "NoSQL Book"   |
+--------------------------------+
```


## Question 14
Demonstrate transactions, consistency, and availability in Neo4j. Perform multiple CREATE, MATCH, SET, and DELETE operations inside a transaction and explain how transaction management maintains consistent graph data.

### Commands and Output

```javascript
# Explicit transaction in cypher-shell (committed)
neo4j@neo4j> :begin
neo4j@neo4j# CREATE (:Account {AccNo:1001, Holder:"Rohit", Balance:5000});
0 rows
Added 1 nodes, set 3 properties, added 1 labels
neo4j@neo4j# CREATE (:Account {AccNo:1002, Holder:"Amit", Balance:2000});
0 rows
Added 1 nodes, set 3 properties, added 1 labels
neo4j@neo4j# MATCH (a:Account {AccNo:1001}) SET a.Balance = a.Balance - 1000;
0 rows
Set 1 properties
neo4j@neo4j# MATCH (b:Account {AccNo:1002}) SET b.Balance = b.Balance + 1000;
0 rows
Set 1 properties
neo4j@neo4j# MATCH (a:Account {AccNo:1001}), (b:Account {AccNo:1002})
             CREATE (a)-[:TRANSFERRED {Amount:1000}]->(b);
0 rows
Created 1 relationships, set 1 properties
neo4j@neo4j# :commit

neo4j@neo4j> MATCH (a:Account) RETURN a.AccNo, a.Holder, a.Balance;
+-------------------------------------+
| a.AccNo | a.Holder | a.Balance      |
+-------------------------------------+
| 1001    | "Rohit"  | 4000           |
| 1002    | "Amit"   | 3000           |
+-------------------------------------+

# Explicit transaction that is ROLLED BACK
neo4j@neo4j> :begin
neo4j@neo4j# MATCH (a:Account {AccNo:1001}) SET a.Balance = a.Balance - 3000;
0 rows
Set 1 properties
neo4j@neo4j# MATCH (a:Account {AccNo:1001}) RETURN a.Balance;
+-----------+
| a.Balance |
+-----------+
| 1000      |
+-----------+
neo4j@neo4j# :rollback

neo4j@neo4j> MATCH (a:Account {AccNo:1001}) RETURN a.Balance;
+-----------+
| a.Balance |
+-----------+
| 4000      |
+-----------+

# DELETE inside a transaction
neo4j@neo4j> :begin
neo4j@neo4j# MATCH (a:Account {AccNo:1002})-[r]-() DELETE r;
0 rows
Deleted 1 relationships
neo4j@neo4j# MATCH (a:Account {AccNo:1002}) DELETE a;
0 rows
Deleted 1 nodes
neo4j@neo4j# :commit

# Note: A node cannot be deleted while it still has relationships,
# unless DETACH DELETE is used: MATCH (a:Account {AccNo:1002}) DETACH DELETE a;

EXPLANATION:

1. ACID transactions
   - Atomicity: all operations in a transaction succeed together or none are applied
     (shown by the rollback).
   - Consistency: the database moves from one valid state to another; constraints are
     enforced, and a node with relationships cannot be deleted without DETACH.
   - Isolation: uncommitted changes are not visible to other transactions
     (default isolation level is read-committed); locks are taken on modified nodes
     and relationships.
   - Durability: committed changes are first written to the transaction log
     (write-ahead log) and survive crashes.

2. Consistency in a cluster
   - In Neo4j clustering, writes go to a primary (leader) member and are committed using
     the Raft consensus protocol after a majority of primaries acknowledge them.
   - Secondary members replicate the transaction log and serve read queries (eventually
     consistent, with bookmarks available for causal consistency).

3. Availability
   - A cluster with 3 or more primaries tolerates the failure of a minority of members.
     If the leader fails, a new leader is elected automatically and the database
     remains available for reads and writes.
```


## Question 15
Develop a small Graph Database application using Neo4j and a programming language such as Python, Java, or JavaScript. Implement CRUD operations and Cypher queries. Demonstrate how graph databases support relationship-based queries, scaling, availability, and suitable use cases such as social networks, recommendation systems, fraud detection, and knowledge graphs.

### Commands and Output

```javascript
# Install the Python driver
$ pip install neo4j
Successfully installed neo4j-5.x

# graph_app.py
$ cat graph_app.py
from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "your_password")

driver = GraphDatabase.driver(URI, auth=AUTH)

def run(query, **params):
    with driver.session() as session:
        return list(session.run(query, **params))

# CREATE
def create_person(name, city):
    run("CREATE (:Person {name:$name, city:$city})", name=name, city=city)

def create_friendship(a, b):
    run("""MATCH (x:Person {name:$a}), (y:Person {name:$b})
           CREATE (x)-[:FRIENDS_WITH]->(y)""", a=a, b=b)

# READ
def get_friends(name):
    result = run("""MATCH (:Person {name:$name})-[:FRIENDS_WITH]-(f)
                    RETURN f.name AS name""", name=name)
    return [r["name"] for r in result]

def recommend_friends(name):
    result = run("""MATCH (p:Person {name:$name})-[:FRIENDS_WITH]-()-[:FRIENDS_WITH]-(rec)
                    WHERE rec <> p AND NOT (p)-[:FRIENDS_WITH]-(rec)
                    RETURN DISTINCT rec.name AS name""", name=name)
    return [r["name"] for r in result]

# UPDATE
def update_city(name, city):
    run("MATCH (p:Person {name:$name}) SET p.city = $city", name=name, city=city)

# DELETE
def delete_person(name):
    run("MATCH (p:Person {name:$name}) DETACH DELETE p", name=name)

if __name__ == "__main__":
    run("MATCH (n) DETACH DELETE n")          # clean start
    for n, c in [("Rohit","Bulandshahr"), ("Amit","Delhi"), ("Priya","Delhi"), ("Neha","Noida")]:
        create_person(n, c)
    create_friendship("Rohit", "Amit")
    create_friendship("Rohit", "Priya")
    create_friendship("Amit", "Neha")

    print("Friends of Rohit      :", get_friends("Rohit"))
    print("Recommendations Rohit :", recommend_friends("Rohit"))

    update_city("Rohit", "Noida")
    print("Rohit's city          :", run("MATCH (p:Person {name:'Rohit'}) RETURN p.city AS c")[0]["c"])

    delete_person("Neha")
    print("Persons after delete  :", [r["n"] for r in run("MATCH (p:Person) RETURN p.name AS n ORDER BY n")])
    driver.close()

$ python3 graph_app.py
Friends of Rohit      : ['Amit', 'Priya']
Recommendations Rohit : ['Neha']
Rohit's city          : Noida
Persons after delete  : ['Amit', 'Priya', 'Rohit']

EXPLANATION:

1. Relationship-based queries
   - Neo4j uses index-free adjacency: each node directly points to its neighbours,
     so traversals (friends, friends-of-friends, shortest path) are fast and do not
     need expensive JOINs, even when the data grows.

2. Scaling
   - Vertical scaling: more memory/CPU for the page cache.
   - Horizontal read scaling: secondary members (read replicas) serve read queries.
   - Large graphs can be split using Neo4j Fabric / composite databases (sharding of
     graphs).

3. Availability
   - A Raft-based cluster with multiple primaries elects a new leader automatically if
     one fails, so the database continues to serve reads and writes.

4. Suitable use cases
   - Social networks: friends, followers, friend suggestions.
   - Recommendation systems: "customers who bought this also bought ...".
   - Fraud detection: finding rings of accounts sharing the same phone, address or card.
   - Knowledge graphs: linking entities and concepts (e.g., people, places, topics) and
     answering semantic queries.
   - Others: network/IT operations, route finding, access control.
```

