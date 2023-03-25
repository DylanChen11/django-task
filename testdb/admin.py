from django.contrib import admin
from .models import Student, Teacher, Score
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_filter = ["name"]
    list_display = ["name", "age"]
    search_fields = ["name"]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    model = Teacher
    list_filter = ["name"]
    list_display = ["name", "age"]
    search_fields = ["name"]

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    model = Score
    list_filter = ["student"]
    list_display = ["value", "student"]
