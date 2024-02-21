from django.shortcuts import render
from main.serializers import *
from rest_framework.response import Response
from main.models import *
from rest_framework.generics import ListAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView



''' Start CRUD Employee '''
class CreateEmployee(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UpdateEmployee(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeleteEmployee(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

''' End CRUD Employee '''




''' Start CRUD Adress '''

class CreateAdress(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class UpdateAdress(UpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class DeleteAdress(DestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


''' End CRUD Adress '''



''' Start CRUD Cashflow '''

class CreateCashflow(ListCreateAPIView):
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer


class UpdateCashflow(UpdateAPIView):
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer


class DeleteCashflow(DestroyAPIView):
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer

''' End CRUD Cashflow '''



''' Start CRUD Room '''

class CreateRoom(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class UpdateRoom(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class DeleteRoom(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

''' End CRUD Room '''


''' Start CRUD Patient '''

class CreatePatient(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class UpdatePatient(UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DeletePatient(DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

''' End CRUD Patient '''



''' Start CRUD Department '''

class CreateDepartment(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class UpdateDepartment(UpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DeleteDepartment(DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

''' End CRUD Department '''



''' Start CRUD Operation '''

class CreateOperation(ListCreateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class UpdateOperation(UpdateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class DeleteOperation(DestroyAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer

''' End CRUD Operation '''


''' Start CRUD Equipment '''

class CreateEquipment(ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class UpdateEquipment(UpdateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class DeleteEquipment(DestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

''' End CRUD Equipment '''


''' Start CRUD Cassa '''

class CreateCassa(ListCreateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializer


class UpdateCassa(UpdateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializer


class DeleteCassa(DestroyAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializer

''' End CRUD Cassa '''


''' Start CRUD Testimonila_patient '''

class CreateTestimonial_patient(ListCreateAPIView):
    queryset = Testimonal_patient.objects.all()
    serializer_class = Testimonal_patientSerializer


class UpdateTestimonial_patient(UpdateAPIView):
    queryset = Testimonal_patient.objects.all()
    serializer_class = Testimonal_patientSerializer


class DeleteTestimonial_patient(DestroyAPIView):
    queryset = Testimonal_patient.objects.all()
    serializer_class = Testimonal_patientSerializer

''' End CRUD Testimonial_patient '''
