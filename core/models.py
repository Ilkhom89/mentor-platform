# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.username

# Student
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} (Student)"

# Teacher
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.subject}"

# Lesson
class Lesson(models.Model):
    subject = models.CharField(max_length=100)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()

    def __str__(self):
        return f"{self.student} - {self.lesson}"

# StudentLesson
class StudentLesson(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.user.username} - {self.lesson.subject}"
    

class TestModel(models.Model):
    name = models.CharField(max_length=100)

