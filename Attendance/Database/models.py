from django.db import models

# Create your models here.
from django.db import models
from django.contrib import auth 
from django.contrib.auth.models import User 
import string
import random
def random_word():
    random_word = ['toe','value','level','cause','robin','look','giraffe','spade','cart','snail','root','committee','egg','quill','heat','hands','vein','month','fly','spoon','van','rabbits','team','hall','street','prose','orange','queen']
    return random.choice(random_word)

class Professor(models.Model):
    user = models.OneToOneField(User,default="", on_delete=models.CASCADE)
    def getClasses(self):
        return self.classes_set.all()
    def getAttendanceRequests(self,class_id):
        classes = Classes.objects.get(id=class_id)
        return classes.attendance_set.all().filter(confirmation=False)
    def acceptAttendanceRequest(self,attendance):
        attendance.confirmation=True
        attendance.save()
    def generateRandomClass(self):
        name = random_word()
        return Classes.objects.create(professor=self,name = name)


class Student(models.Model):
    user = models.OneToOneField(User,default="", on_delete=models.CASCADE)    
    #more fields here if needed
    def displayClassesWithoutAttendance(self):
        allClasses = Classes.getAllClasses()
        allAttendance = Attendance.getStudentAttendance(self)
        _classes =[]
        for a in allAttendance:
            _classes.extend(allClasses.filter(id=a.getClass().id))
        classesWithoutAttendance = []
        for c in allClasses:
            if c not in _classes:
                classesWithoutAttendance.append(c)
        return classesWithoutAttendance
    def requestAttendance(self,classObj):
        Attendance.objects.create(classes = classObj,student = self)
       

class Classes(models.Model):
    professor = models.ForeignKey(Professor,default="", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    @staticmethod  #@classmethod
    def getAllClasses():
        return Classes.objects.all()

class Attendance(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    student =models.ForeignKey(Student,default="", on_delete=models.CASCADE)
    classes = models.ForeignKey(Classes,default="", on_delete=models.CASCADE)
    confirmation = models.BooleanField(default=False)
    @staticmethod  #@classmethod
    def getStudentAttendance(student):
        return Attendance.objects.all().filter(student=student)
    def getClass(self):
        return self.classes

