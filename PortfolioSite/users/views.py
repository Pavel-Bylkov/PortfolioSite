from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
from django.shortcuts import render
from django.contrib.auth import logout as auth_logout

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

def Logged_Out(request):
    auth_logout(request)
    return render(request, 'logged_out.html', context={})
