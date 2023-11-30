from django.shortcuts import render

from mainapp.forms import *
from mainapp.models import *


# Create your views here.
def home(request):

    user = Person.objects.all()
    if not user:
        prof = Profession.objects.create(title="Developer")
        prof.save()
        user = Person.objects.create(first_name="John",
                                     last_name="Conor",
                                     email="john_conor@mail.ru",
                                     number="(732) 915-2434",
                                     url="site.john_conor.ru",
                                     profession=prof,
                                     roles={})
        user.save()
        user = Person.objects.all()
    print(user[0].first_name)
    contacts = {"email": user[0].email, "phone":user[0].number, "website": f"http://{user[0].url}/", "linkedin":"", "github":"", "twitter":"", "snapchat":"bcecam1"}
    context = {"vars": "hello world", "name": f"{user[0].first_name} {user[0].last_name}", "description": user[0].profession.title, "contacts":contacts}
    return render(request, 'mainapp/index.html', context)

def setprofile(request):
    personform=PersonForm(prefix="person")
    if request.method=="POST":
        bound_form=PersonForm(request.POST)
        if bound_form.is_valid():
            first_name = bound_form.cleaned_data["first_name"]
            last_name = bound_form.cleaned_data["last_name"]
            email = bound_form.cleaned_data["email"]
            number = bound_form.cleaned_data["number"]
            url = bound_form.cleaned_data["url"]
            profession = bound_form.cleaned_data["profession"]
            roles = bound_form.cleaned_data["roles"]
