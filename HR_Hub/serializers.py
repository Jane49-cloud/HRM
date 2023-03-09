from .models import User, Employer, Employee, Asset, AssignedAsset
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class EmployerSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = "__all__"


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class AssetSerializer(ModelSerializer):
    class Meta:
        model = Asset
        fields = "__all__"


class AssignedAssetSerializer(ModelSerializer):
    class Meta:
        model = AssignedAsset
        fields = "__all__"
