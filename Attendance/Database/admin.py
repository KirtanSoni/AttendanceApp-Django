from django.contrib import admin
from .models import Attendance, Classes , Student , Professor
# Register your models here.
admin.site.register(Attendance)
admin.site.register(Classes)
admin.site.register(Student)
admin.site.register(Professor)