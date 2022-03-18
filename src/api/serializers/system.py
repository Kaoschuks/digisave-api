from rest_framework import serializers
from api.models.system import Employee, Branch


class BranchSerializer(serializers.ModelSerializer):
    employees = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model = Branch
        fields = ('pk', "name", 'location', 'dateCreated', 'createdBy', 'employees')
        read_only_fields = ("createdBy", "dateCreated",)


class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    user_id = serializers.IntegerField()
    branch = BranchSerializer(read_only=True)
    branch_id = serializers.IntegerField()

    class Meta:
        model = Employee
        fields = ('pk','workId', 'type', 'employedDate', 'user', 'user_id',  'createdBy', 'branch', 'branch_id')
        read_only_fields =("employedDated","createdBy")
