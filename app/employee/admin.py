from django.contrib import admin
from .models import Employee

admin.site.site_header = "Employee"


class EmployeeAdmin(admin.ModelAdmin):
    search_fields = [
        "email",
    ]
    list_display = ("name", "email")


admin.site.register(Employee, EmployeeAdmin)
