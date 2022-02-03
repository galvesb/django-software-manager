from rest_framework import serializers

from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ("id", "name")

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
