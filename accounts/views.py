from django.shortcuts import render,redirect
def login_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if username=="joe" and password=="1234":
            request.session["username"]=username
            return redirect("dashboard")
        return render(
            request,
            "accounts/login.html",
            {"error":"invalid username or password"}
        )
    return render(request, "accounts/login.html")

def dashboard(request):
    username=request.session.get("username")
    if not username:
        return redirect("login")
    return render(
        request,
        "accounts/dashboard.html",
        {"username":username}
    )

def logout_view(request):
    request.session.flush()
    return redirect("login")


