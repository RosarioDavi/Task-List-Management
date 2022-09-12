from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():

            return redirect("home")
    else:
        form = UserCreationForm()

    context = {"form": form}

    return render(request, "registration/signup.html", context)
