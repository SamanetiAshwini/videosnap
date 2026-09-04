from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()
def home(request):
    return render(request,"accounts/home.html")


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return redirect("signup")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("signup")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        messages.success(request, "Account created successfully.")
        return redirect("home")

    return render(request, "accounts/signup.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")

            next_url = request.GET.get("next")
            return redirect(next_url or "home")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "accounts/login.html")


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("login")

def dashboard(request):
    return render(request, "accounts/dashboard.html")

def profile(request):
    return render(request, "accounts/profile.html")

def edit_profile(request):
    return render(request, "accounts/edit_profile.html")

def change_password(request):
    return render(request, "accounts/change_password.html")

def services(request):
    return render(request, "accounts/services.html")

def about(request):
    return render(request, "accounts/about.html")

def contact(request):
    return render(request, "accounts/contact.html")

def faq(request):
    return render(request, "accounts/faq.html")

def help_page(request):
    return render(request, "accounts/help.html")

def notifications(request):
    return render(request, "accounts/notifications.html")

def settings(request):
    return render(request, "accounts/settings.html")

def privacy(request):
    return render(request, "accounts/privacy.html")

def terms(request):
    return render(request, "accounts/terms.html")

def gallery(request):
    return render(request, "accounts/gallery.html")

def blog(request):
    return render(request, "accounts/blog.html")

def blog_detail(request):
    return render(request, "accounts/blog_detail.html")

def search(request):
    return render(request, "accounts/search.html")

def results(request):
    return render(request, "accounts/results.html")





@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("login")

def add(request):
    result = None

    if request.method == "POST":
        avalue = int(request.POST.get("Avalue"))
        bvalue = int(request.POST.get("Bvalue"))
        result = avalue + bvalue
        print(result)
        return render(request, "accounts/add.html", {"avalue":avalue, "bvalue":bvalue, "result":result})
    return render(request, "accounts/add.html")


def sub(request):
    result = None

    if request.method == "POST":
        avalue = int(request.POST.get("Avalue"))
        bvalue = int(request.POST.get("Bvalue"))
        result = avalue - bvalue
        print(result)
        return render(request, "accounts/sub.html", {"avalue":avalue, "bvalue":bvalue, "result":result})
    return render(request, "accounts/sub.html")

def mul(request):
    result = None

    if request.method == "POST":
        avalue = int(request.POST.get("Avalue"))
        bvalue = int(request.POST.get("Bvalue"))
        result = avalue * bvalue
        print(result)
        return render(request, "accounts/mul.html", {"avalue":avalue, "bvalue":bvalue, "result":result})
    return render(request, "accounts/mul.html")

def div(request):
    result = None

    if request.method == "POST":
        avalue = int(request.POST.get("Avalue"))
        bvalue = int(request.POST.get("Bvalue"))
        result = avalue / bvalue
        print(result)
        return render(request, "accounts/div.html", {"avalue":avalue, "bvalue":bvalue, "result":result})
    return render(request, "accounts/div.html")

def sq(request):
    result = None

    if request.method == "POST":
        avalue = int(request.POST.get("Avalue"))
        bvalue = int(request.POST.get("Bvalue"))
        result = avalue ** bvalue
        print(result)
        return render(request, "accounts/sq.html", {"avalue":avalue, "bvalue":bvalue, "result":result})
    return render(request, "accounts/sq.html") 