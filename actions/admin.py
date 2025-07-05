from django.contrib import admin
from .models import Azan, Takbeer


@admin.register(Azan)
class AzanAdmin(admin.ModelAdmin):
    # list_display = [
    #     "full_name",
    #     "phone_number",
    #     "date_of_birth_shamsi",
    #     "has_profile"
    # ]
    list_per_page = 20


@admin.register(Takbeer)
class TakbeerAdmin(admin.ModelAdmin):
    # list_display = [
    #     "full_name",
    #     "phone_number",
    #     "date_of_birth_shamsi",
    #     "has_profile"
    # ]
    list_per_page = 20
