from django.contrib import admin
from .models import Azan, Takbeer
from unfold.admin import ModelAdmin


@admin.register(Azan)
class AzanAdmin(ModelAdmin):
    # list_display = [
    #     "full_name",
    #     "phone_number",
    #     "date_of_birth_shamsi",
    #     "has_profile"
    # ]
    list_per_page = 20


@admin.register(Takbeer)
class TakbeerAdmin(ModelAdmin):
    # list_display = [
    #     "full_name",
    #     "phone_number",
    #     "date_of_birth_shamsi",
    #     "has_profile"
    # ]
    list_per_page = 20
