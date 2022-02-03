from django.urls import path

from .views import EmployeeAPIView, EmployeeGenericAPIView

urlpatterns = [
    path("employees", EmployeeAPIView.as_view()),
    path("employee/register", EmployeeGenericAPIView.as_view()),
    path("employee/<str:pk>", EmployeeGenericAPIView.as_view()),
]
