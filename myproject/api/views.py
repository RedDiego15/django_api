# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from students.models import Student

from rest_framework import viewsets
from students.models import Student
from students.serializer import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer