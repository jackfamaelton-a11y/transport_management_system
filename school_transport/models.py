from django.db import models
from django.contrib.auth.models import User

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    profile_photo = models.ImageField(upload_to="drivers/", blank=True, null=True)
    current_location = models.CharField(max_length=100, blank=True)
    destination = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.full_name

class Notification(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver.full_name}: {self.message}"


class Child(models.Model):
    full_name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    residential_area = models.CharField(max_length=100)
    guardian_phone = models.CharField(max_length=20)
    driver = models.ForeignKey('Driver', on_delete=models.SET_NULL, null=True, related_name="children")
    profile_photo = models.ImageField(upload_to="children/", blank=True, null=True)
    pickup_time = models.TimeField(null=True, blank=True)
    drop_time = models.TimeField(null=True, blank=True)
    teacher = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.full_name