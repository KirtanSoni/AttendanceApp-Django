from django.urls import path
from Database.views import student_view,generate_random_class ,direct_profile ,teacher_view , request_attendance, accept_attendance , display_attendance
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('home',direct_profile),
    path('student_view',student_view),
    path('teacher_view',teacher_view),
    path('student_view/<class_id>',request_attendance),
    path('teacher_view/classes/add',generate_random_class),
    path('teacher_view/classes/<class_id>',display_attendance),
    path('teacher_view/classes/<class_id>/<attendance_id>',accept_attendance, name='accept_attendance'),

]
