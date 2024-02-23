from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Employee
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Room
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Address
        fields = "__all__"


class CashflowSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Cashflow
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Patient
        fields = "__all__"


class Testimonal_patientSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Testimonal_patient
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Department
        fields = "__all__"


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Operation
        fields = "__all__"


<<<<<<< HEAD
=======
class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        depht = 1
        model = Equipment
        fields = "__all__"

>>>>>>> 2ec677803d99f6122a2cdc3885d6a7cd53f9e30f
class CassaSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Cassa
        fields = "__all__"

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Attendance
        fields = "__all__"


