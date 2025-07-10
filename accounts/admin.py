from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group
from accounts.models import CustomUser

from unfold.forms import (
    AdminPasswordChangeForm,
    UserChangeForm,
    UserCreationForm
)
from unfold.admin import ModelAdmin

admin.site.unregister(Group)


@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "phone_number",
                    "username",
                    "password",
                    "otp",
                    "otp_expires_at"
                ],
            },
        ),
        (
            "Personal info",
            {
                "classes": ["collapse"],
                "fields": [
                    "profile",
                    "first_name",
                    "last_name",
                    "email",
                    "date_of_birth"
                ],
            },
        ),
        (
            "Permissions",
            {
                "classes": ["collapse"],
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions"
                ],
            },
        ),
        (
            "Important dates",
            {
                "classes": ["collapse"],
                "fields": [
                    "last_login",
                    "date_joined"
                ],
            },
        ),
    ]


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    fields = ["name", "permissions"]
