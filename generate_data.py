from peewee import fn
from random import randint

from db import Student, Mark

for _ in range(1000):
    # Get random student
    student = Student.select().order_by(fn.Random()).get()

    # Generate mark
    Mark.create(student=student, value=randint(60, 100))
