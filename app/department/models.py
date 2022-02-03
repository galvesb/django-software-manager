from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
