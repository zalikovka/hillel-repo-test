from flask import Flask, jsonify, request

from db import get_students, insert_student, update_student, delete_student, get_student
from deserializators import deserialize_student_data
from serializatiors import serialize_db_student
from validators import ValidationError, validate_student_data

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({"message": "Hello World"})


@app.route('/students', methods=["GET", "POST"])
def students_api():
    if request.method == "GET":
        records = get_students()

        # Old style
        # students = []
        # for record in records:
        #     students.append(serialize_db_student(record))

        # List comprehension
        students = [serialize_db_student(record) for record in records]

        # Map
        # students = list(map(serialize_db_student, records))

        return jsonify(students)
    elif request.method == "POST":
        data = request.get_json()
        name = data.get("name")
        age = data.get("age")

        try:
            validate_student_data(data)
        except ValidationError as e:
            return jsonify({"message": str(e)}), 422

        insert_student(name, age)
        return jsonify({"name": name, "age": age}), 201


@app.route('/students/<int:id>', methods=["PATCH", "DELETE", "GET"])
def student_api(id):
    if request.method == "PATCH":
        data = deserialize_student_data()

        try:
            validate_student_data(data)
        except ValidationError as e:
            return jsonify({"message": str(e)}), 422

        update_student(id, data["name"], data["age"])

        return jsonify({"id": id, **data})
    elif request.method == "DELETE":
        student = get_student(id)
        if not student:
            return jsonify({"message": "Not Found"}), 404

        delete_student(id)
        return "", 204
    elif request.method == "GET":
        record = get_student(id)
        if not record:
            return jsonify({"message": "Not Found"}), 404

        student = serialize_db_student(record)

        return jsonify(student)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
