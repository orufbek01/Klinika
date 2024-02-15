from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


class Employee_all(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


