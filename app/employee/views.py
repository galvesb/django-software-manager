from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions, status, generics, mixins

from department.models import Department

from .models import Employee
from user.authentication import JWTAuthentication
from .serializers import EmployeeSerializer


class EmployeeAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = EmployeeSerializer(
            data={
                "name": request.data["name"],
                "email": request.data["email"],
                "department": request.data["department"],
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def get(self, request):
        links = Employee.objects.all().order_by("-id")
        serializer = EmployeeSerializer(links, many=True)
        return Response(serializer.data)


class EmployeeGenericAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})

        return self.list(request)

    def put(self, request, pk=None):
        return Response({"data": self.partial_update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)
