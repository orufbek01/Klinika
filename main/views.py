from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


class Get_Employee(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class Get_Room(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class Get_Address(ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class Get_Cashflow(ListAPIView):
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer


class Get_Patient(ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class Get_Testimonal_patient(ListAPIView):
    queryset = Testimonal_patient.objects.all()
    serializer_class = Testimonal_patientSerializer


class Get_Department(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class Get_Operation(ListAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class Get_Attendance(ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
