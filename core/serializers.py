from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Student, Teacher, Lesson, StudentLesson

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_student', 'is_teacher']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            is_student=validated_data.get('is_student', False),
            is_teacher=validated_data.get('is_teacher', False),
        )
        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'phone']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'user', 'subject']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'teacher', 'date', 'start_time']


class StudentLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLesson
        fields = ['id', 'student', 'lesson']
