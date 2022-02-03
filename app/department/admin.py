from django.contrib import admin
from .models import Department

admin.site.site_header = "Department"


class DepartmentAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
    ]
    list_display = ("name",)
    list_filter = ("name",)


admin.site.register(Department, DepartmentAdmin)
