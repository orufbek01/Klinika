from rest_framework import serializers
from .models import *


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Employee
        fields = "__all__"
