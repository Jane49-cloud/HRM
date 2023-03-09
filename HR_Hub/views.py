from rest_framework import generics, mixins
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.response import Response

from .models import User, Employer, Employee, Asset, AssignedAsset
from .serializers import UserSerializer, EmployeeSerializer, EmployerSerializer, AssetSerializer, AssignedAssetSerializer


class ListCreateEmployerView(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        if not request.user.is_employer:
            return Response({'error': 'Only employers can create employer accounts.'}, status=400)

        return super().post(request, *args, **kwargs)
