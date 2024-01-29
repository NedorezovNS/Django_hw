from django.contrib import admin

from .models import Student, Teacher


class TeachersInline(admin.TabularInline):
    model = Student.teachers.through
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [TeachersInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [TeachersInline]
