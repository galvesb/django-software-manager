from django.db import models
from department.models import Department


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="department"
    )

    def __str__(self) -> str:
        return self.name
