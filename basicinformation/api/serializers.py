from rest_framework import serializers
from basicinformation.models import *
from QuestionsAndPapers.models import *


class SchoolDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = [
            'name',
        ]

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            'name',
            'school',
        ]

class BatchSerializer(serializers.ModelSerializer):
    school = SchoolDisplaySerializer()
    class Meta:
        model = klass
        fields = [
            'id',
            'name',
            'school',
        ]


class StudentModelSerializer(serializers.ModelSerializer):
    #school = SchoolDisplaySerializer()
    #user = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = [
            'name',
        ]

    #def get_user(self,obj):
    #    return str(obj.studentuser.email)

class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            
            'username',
            'email',
            'first_name'
        ]

class SSCOnlineMarksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSCOnlineMarks
        fields = [
            'marks',
            'testTaken'
        ]


class TimeTableModelSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    batch = BatchSerializer()
    class Meta:
        model = TimeTable
        fields = [
            'date',
            'time',
            'teacher',
            'batch',
            'sub',
            'note',

        ]
        read_only_fields = ('created',)
