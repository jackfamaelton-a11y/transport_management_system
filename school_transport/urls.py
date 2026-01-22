from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("driver/login/", views.driver_login, name="driver_login"),
    path("driver/logout/", views.driver_logout, name="driver_logout"),
    path("driver/dashboard/", views.driver_dashboard, name="driver_dashboard"),
]