from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def homepage(request):
    if request.method == "POST":
        print(request.POST["code"])
        # check if the code exists
        # if exists redirect to the meeting page and record data
    return render(request, 'homepage.html')


def sign_out(request):
    logout(request)
    return redirect('/')


def signin(request):
    if request.user.is_authenticated:
        if not request.user.has_usable_password():
            return redirect("/logout")
        return redirect("/dashboard")
    if request.method == "POST":
        # validate user login details
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session["login_status"] = True
            return redirect('/dashboard')
        else:
            messages.info(request, "User Credentials Not Match")
            request.session["login_status"] = False
    return render(request, 'login.html')


def register(request):
    if request.user.is_authenticated:
        if not request.user.has_usable_password():
            return redirect("/logout")
        return redirect("/dashboard")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        name = request.POST["name"]
        f_name = name.split(' ')[0]
        try:
            l_name = name.split(' ')[1]
        except IndexError:
            l_name = ""
        email = request.POST["email"]
        # contact = request.POST["contact"]
        confpassword = request.POST["confpassword"]
        if password == confpassword:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password,
                                            first_name=f_name,
                                            last_name=l_name, )
            user.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session["login_status"] = True
                return redirect('/dashboard')
            else:
                messages.info(request, "User Credentials Not Match")
                request.session["login_status"] = False
                return render(request, 'login.html')
        else:
            messages.info(request, "Passwords not match")

    return render(request, 'registration.html')


def dashboard(request):
    return render(request, 'dashboard.html')
