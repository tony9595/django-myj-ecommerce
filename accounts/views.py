from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def login_user(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "로그인이 되었습니다.")
            return redirect("/")
        else:
            messages.success(request, "로그인이 실패 하였습니다.")
            return redirect("/accounts/login")

    else:
        return render(request, "accounts/login.html", {})


def logout_user(request):
    logout(request)
    return redirect("/")
