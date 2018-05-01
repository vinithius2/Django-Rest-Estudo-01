from rest_framework.serializers import ModelSerializer
from ..models import Student, Teacher


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'name', 'matter')


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'schooling')
