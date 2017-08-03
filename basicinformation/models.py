from django.db import models
from django.contrib.auth.models import User


class School(models.Model):
    name = models.CharField(max_length=200)
    pincode = models.IntegerField()

    def __str__(self):
        return self.name


class klass(models.Model):
    level_choices = (('9','Ninth'),('10','Tenth'),('11','Eleventh'),('12','Twelveth'))
    school = models.ForeignKey(School)
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=10, choices =
                             level_choices,null=True,blank=True)
    def __str__(self):
        return self.name


class Student(models.Model):
    studentuser = models.OneToOneField(User,blank=True,null=True)
    klass = models.ForeignKey(klass,related_name='klass')
    rollNumber = models.BigIntegerField()
    name = models.CharField(max_length=200)
    dob = models.DateField()
    pincode = models.IntegerField()
    school = \
    models.ForeignKey(School,related_name='school',blank=True,null=True)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    teacheruser = models.OneToOneField(User,blank=True,null=True)
    name = models.CharField(max_length=200)
    experience = models.FloatField()
    school = models.ForeignKey(School,blank=True,null=True)
    

    def __str__(self):
        return self.name


class Subject(models.Model):
    student = models.ForeignKey(Student)
    teacher = models.ForeignKey(Teacher,blank=True,null=True)
    name = models.CharField(max_length=200)
    test1 = models.IntegerField(null=True, blank=True)
    test2 = models.IntegerField(null=True, blank=True)
    test3 = models.IntegerField(null=True, blank=True)
    hy = models.IntegerField(null=True, blank=True)
    test4 = models.IntegerField(null=True, blank=True)
    lab1 = models.IntegerField(null=True, blank=True)
    lab2 = models.IntegerField(null=True, blank=True)
    lab3 = models.IntegerField(null=True, blank=True)
    finalexam = models.IntegerField(null=True, blank=True)
    predicted_hy = models.IntegerField(null=True,blank= True)
    prdicted_final = models.IntegerField(null= True, blank=True)

    def __str__(self):
        return \
    '{}---{}----{}----{}'.format(self.name,self.student,self.teacher,self.student.school)


    

