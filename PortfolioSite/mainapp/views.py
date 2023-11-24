from django.shortcuts import render

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
