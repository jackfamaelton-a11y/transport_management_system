from django.contrib import admin
from .models import Driver, Child

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("id","full_name", "phone_number", "current_location", "destination")
    search_fields = ("full_name", "phone_number")
    list_filter = ("destination",)

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ("id","full_name", "level", "residential_area", "guardian_phone", "driver")
    search_fields = ("full_name", "guardian_phone")
    list_filter = ("level", "driver")