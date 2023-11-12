from db import Student, Teacher

class ValidationError(Exception):
    pass


def validate_student_data(data):
    name = data.get("name")
    age = data.get("age")

    if not (name and age):
        raise ValidationError("name and age are required")

    if not isinstance(age, int):
        raise ValidationError("age must be integer")
    if not isinstance(name, str):
        raise ValidationError("name must be string")

    if age < 0:
        raise ValidationError("age must be positive")
    if name == "":
        raise ValidationError("name must not be empty")


def validate_mark_data(data):
    student_id = data.get("student_id")
    teacher_id = data.get("teacher_id")
    value = data.get("value")

    student = Student.get_or_none(id=student_id)
    teacher = Teacher.get_or_none(id=teacher_id)

    if not student:
        raise ValidationError("student with such id does not exist")
    if not teacher:
        raise ValidationError("teacher with such id does not exist")
    if not (student_id and value):
        raise ValidationError("student_id and value are required")

    if not isinstance(student_id, int):
        raise ValidationError("student_id must be integer")
    if not isinstance(value, int):
        raise ValidationError("value must be integer")

    if value < 0:
        raise ValidationError("value must be positive")

    data["student"] = student
    data["teacher"] = teacher
    return data


def validate_teacher_data(data):
    name = data.get("name")
    age = data.get("age")
    subject = data.get("subject")
    is_active = data.get("is_active")
    # too hard to test datetime, not implemented
    #start_of_work = data.get("start_of_work")
    #end_of_work = data.get("end_of_work")


    if not (all((name, age, subject))):
        raise ValidationError("name, age and subject are required")

    if not isinstance(age, int):
        raise ValidationError("age must be integer")
    if not isinstance(name, str):
        raise ValidationError("name must be string")
    if not isinstance(subject, str):
        raise ValidationError("subject must be string")
    if not isinstance(is_active, int):
        raise ValidationError("subject must be integer")

    if age < 0:
        raise ValidationError("age must be positive")
    if name == "":
        raise ValidationError("name must not be empty")
    if subject == "":
        raise ValidationError("subject must not be empty")
    if is_active not in (0, 1):
        raise ValidationError("is must be 1 or 0")
