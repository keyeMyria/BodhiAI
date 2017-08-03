from django.contrib import admin
from .models import School,klass,Student,Subject,Teacher


class TeacherInline(admin.StackedInline):
    model = Teacher
    extra = 1
class StudentInline(admin.StackedInline):
    model = Student
    extra = 1

class SchoolAdmin(admin.ModelAdmin):
    inlines = [TeacherInline]
class KlassAdmin(admin.ModelAdmin):
    inlines = [StudentInline]


admin.site.register(School,SchoolAdmin)
admin.site.register(klass,KlassAdmin)
admin.site.register(Subject)
