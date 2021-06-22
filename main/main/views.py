
from django.http.response import HttpResponseRedirect

from django.urls import reverse
from django.contrib.auth import login as l
from django.contrib.auth import logout as lo
from .models import SignupForm
from django.contrib.auth.models import User
from django.shortcuts import render

from django.contrib import messages

def signup(r):
    if r.method == 'POST':
        username = r.POST['username']
        email = r.POST['email']
        re_password = r.POST['re_password']
        password = r.POST['password']

        form = SignupForm(r.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email =  form.cleaned_data['email']
            password =  form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)

            messages.success(r, "Registration Sucess. Please login...")

            return HttpResponseRedirect(reverse('login'))
    else:
        form = SignupForm()

    return render(r, "registration/signup.html", {'form': form})


# def login(r):
#     if r.user.is_authenticated:
#         return HttpResponseRedirect(reverse('todolist:index')) 
#     else:
#         l(r, r.user)

# def logout(r):
#     lo(r)
#     return HttpResponseRedirect(reverse('todolist:index'))

# def reset_pass(r):
#     pass