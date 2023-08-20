from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    list_display = ["id","email", "name",'designation', "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name","designation"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name",'designation', "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email","name"]
    ordering = ["email","id"]
    filter_horizontal = []

admin.site.register(User, UserAdmin)
