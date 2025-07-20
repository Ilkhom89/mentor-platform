from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from core.models import Student, Teacher, Lesson, StudentLesson
from django.test import TestCase
from django.utils import timezone
from datetime import time, date
User = get_user_model()

class UserRegisterTest(APITestCase):
    def test_user_register(self):
        url = reverse('register')
        data = {"username":"testuser","email":"test@example.com","password":"testpassword123","is_student":True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserLoginTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser",email="test@example.com",password="testpassword123")
    def test_user_login(self):
        url = reverse('token_obtain_pair')
        data = {"username":"testuser","password":"testpassword123"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

class LessonCreateTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="teachertest",email="teacher@example.com",password="teachpass123",is_teacher=True)
        self.teacher = Teacher.objects.create(user=self.user, subject="Math")
        url = reverse('token_obtain_pair')
        resp = self.client.post(url, {"username":"teachertest","password":"teachpass123"}, format='json')
        self.token = resp.data['access']
    def test_create_lesson(self):
        url = reverse('lesson-list')
        data = {"subject":"Math","teacher":self.teacher.id,"date":"2025-07-18","start_time":"14:00"}
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

class LessonListTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="teacheruser",email="teacher@example.com",password="password123",is_teacher=True)
        self.client.force_authenticate(user=self.user)
        self.teacher = Teacher.objects.create(user=self.user, subject="Math")
        Lesson.objects.create(subject="Math",teacher=self.teacher,date="2025-07-16",start_time="10:00")
        Lesson.objects.create(subject="Math",teacher=self.teacher,date="2025-07-17",start_time="11:00")
    def test_lesson_list(self):
        url = reverse('lesson-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['results']), 2)

class StudentLessonEnrollTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="studentuser",email="student@example.com",password="password123",is_student=True)
        self.student = Student.objects.create(user=self.user,phone="998901234567")
        self.teacher_user = User.objects.create_user(username="teacheruser",email="teacher@example.com",password="password123",is_teacher=True)
        self.teacher = Teacher.objects.create(user=self.teacher_user, subject="Math")
        self.lesson = Lesson.objects.create(subject="Math",teacher=self.teacher,date="2025-07-16",start_time="10:00")
        self.client.force_authenticate(user=self.user)
    def test_student_enroll_lesson(self):
        url = reverse('studentlesson-list')
        data = {"student":self.student.id,"lesson":self.lesson.id}
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

class StudentListTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="adminuser",email="admin@example.com",password="adminpass",is_staff=True)
        self.client.force_authenticate(user=self.user)
        u1 = User.objects.create_user(username="student1",is_student=True)
        u2 = User.objects.create_user(username="student2",is_student=True)
        Student.objects.create(user=u1,phone="998901234561")
        Student.objects.create(user=u2,phone="998901234562")
    def test_student_list(self):
        url = reverse('student-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['results']), 2)

class TeacherListTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="adminuser2",email="admin2@example.com",password="adminpass",is_staff=True)
        self.client.force_authenticate(user=self.user)
        u1 = User.objects.create_user(username="teacher1",is_teacher=True)
        u2 = User.objects.create_user(username="teacher2",is_teacher=True)
        Teacher.objects.create(user=u1,subject="Math")
        Teacher.objects.create(user=u2,subject="Biology")
    def test_teacher_list(self):
        url = reverse('teacher-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['results']), 2)



class ModelTestCase(TestCase):
    def setUp(self):
        # Foydalanuvchilar
        self.student_user = User.objects.create_user(username="student1", is_student=True)
        self.teacher_user = User.objects.create_user(username="teacher1", is_teacher=True)

        # Student & Teacher
        self.student = Student.objects.create(user=self.student_user, phone="998901234561")
        self.teacher = Teacher.objects.create(user=self.teacher_user, subject="Matematika")

        # Dars
        self.lesson = Lesson.objects.create(
            subject="Matematika",
            teacher=self.teacher,
            date=date.today(),
            start_time=time(10, 0)
        )

        # Student darsga qatnashgan
        self.enrollment = StudentLesson.objects.create(student=self.student, lesson=self.lesson)

    def test_student_model(self):
        self.assertEqual(self.student.user.username, "student1")
        self.assertEqual(self.student.phone, "998901234561")
        self.assertTrue(self.student.user.is_student)

    def test_teacher_model(self):
        self.assertEqual(self.teacher.user.username, "teacher1")
        self.assertEqual(self.teacher.subject, "Matematika")
        self.assertTrue(self.teacher.user.is_teacher)

    def test_lesson_model(self):
        self.assertEqual(self.lesson.subject, "Matematika")
        self.assertEqual(self.lesson.teacher, self.teacher)
        self.assertEqual(self.lesson.start_time, time(10, 0))

    def test_studentlesson_model(self):
        self.assertEqual(self.enrollment.student, self.student)
        self.assertEqual(self.enrollment.lesson, self.lesson)
