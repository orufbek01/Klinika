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
        model = Cashflow
        fields = "__all__"


class Patients_aboutSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Patients_about
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


