from django.db import models
from codeschool import models

# Create your models here.
class Tutor(models.Model):
    name = Charfield(max_length=100)



class Learner(models.Model):
    name = Charfield(max_length=100)
    tutor = ForeignKey('Tutor')


class Student(models.User):
    grade = FloatField()
