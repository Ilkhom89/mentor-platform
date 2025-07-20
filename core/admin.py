from django.contrib import admin
from .models import User, Student, Teacher, Lesson, StudentLesson

# 🔹 Umumiy admin klasslar
class BaseUserInlineAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)
    list_display = ('id', 'user')

class BaseNamedAdmin(admin.ModelAdmin):
    search_fields = ('subject',)
    list_display = ('id', 'subject')


# 🔹 ModelAdmin klasslari

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_student', 'is_teacher', 'is_staff')
    list_filter = ('is_student', 'is_teacher', 'is_staff')
    search_fields = ('username', 'email')

@admin.register(Student)
class StudentAdmin(BaseUserInlineAdmin):
    list_display = ('id', 'user', 'phone')
    search_fields = ('user__username', 'phone')

@admin.register(Teacher)
class TeacherAdmin(BaseUserInlineAdmin):
    list_display = ('id', 'user', 'subject')
    search_fields = ('user__username', 'subject')

@admin.register(Lesson)
class LessonAdmin(BaseNamedAdmin):
    list_display = ('id', 'subject', 'teacher', 'date', 'start_time')
    list_filter = ('date', 'subject')
    search_fields = ('subject', 'teacher__user__username')

@admin.register(StudentLesson)
class StudentLessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'lesson')
    list_filter = ('lesson__date',)
    search_fields = ('student__user__username', 'lesson__subject')
