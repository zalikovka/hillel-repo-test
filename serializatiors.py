def serialize_db_student(record):
    return {
        "id": record[0],
        "name": record[1],
        "age": record[2]
    }
