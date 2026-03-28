from flask import Flask,jsonify,request

app = Flask(__name__)
students=[
    {'id':1,'name':'revanth'},
    {'id':2,'name':'Naga Sai Revanth','skills':['c++','c','python']}
]

@app.route('/students',methods=['GET'])
def home():
    return jsonify(students)

# inserting the data
@app.route('/pushing',methods=['POST'])
def add_student():
    data=request.json
    student={
        'id':data['id'],
        'name':data['name']
    }
    students.append(student)
    
    return jsonify("added the student",student)

#single student data displaying
@app.route('/student/<int:id>',methods=['GET'])
def get_student(id):
    for i in students:
        if i['id']==id:
            return jsonify(i)
    return jsonify('student not found')

# Updating the exissting data
@app.route('/stud/<int:id>',methods=['PUT'])
def updating(id):
    data=request.json
    for i in students:
        if i['id']==id:
            i['name']=data['name']
            return jsonify("updated data",data)
    return jsonify('data is not found')


# deleting the data
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    for student in students:
        if student['id'] == id:
            students.remove(student)
            return jsonify({"message": "Student deleted successfully"})
    
    return jsonify({"message": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)