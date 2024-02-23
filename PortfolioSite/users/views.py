from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

class LogOut(LogoutView):
    success_url = reverse_lazy("logged_out")

def Logged_Out(request):
    return render(request, 'registration/logged_out.html', context={})