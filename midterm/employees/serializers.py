from rest_framework import serializers
from employees.models import Employee
class EmployeesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(min_length=5, max_length=100, allow_null=False)
    position = serializers.CharField(max_length=255, allow_null=False)
    salary = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        employees = Employee(**validated_data)
        employees.save()
        return employees

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.save()
        return instance