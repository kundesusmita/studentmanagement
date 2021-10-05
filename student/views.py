from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *

from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer