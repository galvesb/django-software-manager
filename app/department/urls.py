from django.urls import path

from .views import DepartmentAPIView

urlpatterns = [
    path("departments", DepartmentAPIView.as_view()),
]
