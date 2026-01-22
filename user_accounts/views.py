from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from school_transport.models import Driver, Child, Assignment

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("driver_dashboard.css")
        else:
            return render(request, "user_accounts/login.html", {"error": "Invalid credentials"})
    return render(request, "user_accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def driver_dashboard(request):
    driver = Driver.objects.filter(user=request.user).first()
    children = Child.objects.filter(driver=driver) if driver else []
    assignments = Assignment.objects.filter(driver=driver) if driver else []

    context = {
        "driver": driver,
        "children": children,
        "assignments": assignments,
    }
    return render(request, "user_accounts/driver_dashboard.css.html", context)