from django.contrib import admin
from .models import User

admin.site.site_header = "User Admin"


class UserAdmin(admin.ModelAdmin):
    search_fields = [
        "email",
    ]
    list_display = ("email", "first_name", "last_name")


admin.site.register(User, UserAdmin)
