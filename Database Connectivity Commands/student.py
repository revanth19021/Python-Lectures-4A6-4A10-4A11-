from pymongo import MongoClient
client=MongoClient("mongodb://127.0.0.1:27017/")
db=client["student_db"]
collection=db["students"]
# student={
#     "name":"Alice",
#     "age":20,
#     "marks":85
# }
collection.insert_one({"name":"revanth","email":"revanth200319@gmail.com"})
print("Data is inserted")
students=collection.find()
for student in students:
    print(student)
    
name=input("Enter name: ")
age=int(input("Enter age: "))
marks=int(input("Enter marks: "))
collection.insert_one({"name":name,"age":age,"marks":marks})

# insert multiple documents

students=[
    {"name":"Bob","age":22,"marks":90},
    {"name":"Charlie","age":21,"marks":88},
    {"name":"David","age":23,"marks":92},
    {"name":"Eve","age":20,"marks":87}
]

db.students.insert_many(students)

data=collection.find()

for i in data:
    print(i)
    
# read specific data (WHERE condition)
result = collection.find({"marks": {"$gt": 85}})

for doc in result:
    print(doc)
 
 #find one document
student = collection.find_one({"name": "Alice"})



#update document
collection.update_one({"name":"Alice"},{"$set":{"marks":95}})


# Update MULTIPLE documents
collection.update_many(
    {"marks":{"$gt":90}},
    {"$set":{"grade":"A"}}
)

#Delete ONE document
collection.delete_one({"name":"revanth"})

#delete MULTIPLE documents

collection.delete_many({"marks":{"$lt":85}})