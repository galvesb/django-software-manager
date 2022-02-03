from rest_framework import serializers

from .models import Employee
from department.serializers import DepartmentSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.ReadOnlyField(source="department.name")
    # department = DepartmentSerializer(many=True)

    class Meta:
        model = Employee
        fields = ("id", "name", "email", "department", "department_name")

        extra_kwargs = {"department": {"write_only": True}}

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance