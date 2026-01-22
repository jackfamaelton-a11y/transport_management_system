from django.urls import path
from .views import login_view, logout_view, driver_dashboard

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', driver_dashboard, name='driver_dashboard.css'),
]