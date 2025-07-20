from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Student, Teacher, Lesson, StudentLesson
from .serializers import (
    RegisterSerializer,
    StudentSerializer,
    TeacherSerializer,
    LessonSerializer,
    StudentLessonSerializer
)


# ✅ Ro'yxatdan o'tish view
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Ro‘yxatdan o‘tish muvaffaqiyatli!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ Darslar ro'yxati va yaratish
class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all().order_by('date', 'start_time')  # 🔧 order_by qo‘shildi
    serializer_class = LessonSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['subject', 'date']


# ✅ Darsni bitta ko‘rish/yangilash/o‘chirish
class LessonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all().order_by('date', 'start_time')  # 🔧 order_by qo‘shildi
    serializer_class = LessonSerializer
    permission_classes = (permissions.IsAuthenticated,)


# ✅ O‘qituvchilar ro‘yxati va yaratish
class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all().order_by('id')  # 🔧 order_by qo‘shildi
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]


# ✅ Routers uchun ViewSetlar

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('id')  # 🔧 order_by qo‘shildi
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('id')  # 🔧 order_by qo‘shildi
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all().order_by('date', 'start_time')  # 🔧 order_by qo‘shildi
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentLessonViewSet(viewsets.ModelViewSet):
    queryset = StudentLesson.objects.all().order_by('id')  # 🔧 order_by qo‘shildi
    serializer_class = StudentLessonSerializer
    permission_classes = [permissions.IsAuthenticated]
