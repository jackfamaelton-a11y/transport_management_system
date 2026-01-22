from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Driver, Child

def driver_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("driver_dashboard")

    return render(request, "school_transport/driver_login.html")


def driver_logout(request):
    logout(request)
    return redirect("driver_login")


@login_required
def driver_dashboard(request):
    # get driver linked to logged-in user
    try:
        driver = Driver.objects.get(user=request.user)
    except Driver.DoesNotExist:
        return redirect("driver_login")

    # children assigned to this driver
    children = Child.objects.filter(driver=driver)

    notifications = driver.notifications.order_by('-created_at')

    return render(request, "school_transport/driver_dashboard.html", {
        "driver": driver,
        "children": children,
        "notifications": notifications,
    })