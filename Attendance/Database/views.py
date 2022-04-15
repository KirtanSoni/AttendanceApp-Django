from django.shortcuts import render
import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse , Http404
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from .models import Attendance, Classes , Student , Professor

# Create your views here.
def direct_profile(request):
    user = request.user
    try:
        profile=user.student
    except ObjectDoesNotExist:
        try:
            profile=user.professor
        except ObjectDoesNotExist:
            return Http404("you are not a student or professor")
        return HttpResponseRedirect("/database/teacher_view")
    return HttpResponseRedirect("/database/student_view")

def student_view(request):
    user = request.user
    try:
        profile=user.student
    except ObjectDoesNotExist:
         return Http404("you are not a student")
    classes = profile.displayClassesWithoutAttendance()
    try :
        return render(request, 'student.html', {'classes':classes})
    except ObjectDoesNotExist:
            return Http404("invalid class id")

def request_attendance(request,class_id):
    user = request.user
    try:
        profile=user.student
    except ObjectDoesNotExist:
         return Http404("you are not a Student")
    try:
        classObj = Classes.objects.get(id=class_id)
    except ObjectDoesNotExist:
         return Http404("invalid class id")
    profile.requestAttendance(classObj)
    return HttpResponseRedirect("/database/student_view")


def teacher_view(request):
    user = request.user
    try:
        profile=user.professor
    except ObjectDoesNotExist:
         return Http404("you are not a professor")
    classes = profile.getClasses()
    
    return render(request, 'classes.html', {'classes' :classes}) 

def display_attendance(request,class_id):
    user = request.user
    try:
        profile=user.professor
    except ObjectDoesNotExist:
         return Http404("you are not a professor")
    try:
        classObj = Classes.objects.get(id=class_id)
    except ObjectDoesNotExist:
         return Http404("invalid class id")
    attendance = Attendance.objects.all().filter(classes=classObj,confirmation=True)
    attendanceRequests = profile.getAttendanceRequests(class_id)
    return render(request, 'teacher.html', {'attendance':attendance, 'req':attendanceRequests, 'class_id':class_id})

def generate_random_class(request):
    user = request.user
    try:
        profile=user.professor
    except ObjectDoesNotExist:
         return Http404("you are not a professor")
    profile.generateRandomClass()
    return HttpResponseRedirect("/database/teacher_view")

def accept_attendance(request,class_id,attendance_id):
    user = request.user
    try:
        profile=user.professor
    except ObjectDoesNotExist:
         return Http404("you are not a professor")
    try:
        attendance = Attendance.objects.get(id=attendance_id)
    except ObjectDoesNotExist:
         return Http404("invalid attendance id")
    profile.acceptAttendanceRequest(attendance)
    return HttpResponseRedirect("/database/teacher_view/classes/"+class_id)
