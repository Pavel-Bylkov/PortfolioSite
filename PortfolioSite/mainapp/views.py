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
    contacts = {"email": user[0].email, "phone":user[0].number, "website": f"{user[0].url}", "linkedin":"", "github":"", "twitter":"", "snapchat":"bcecam1"}
    context = {"vars": "hello world", "name": f"{user[0].first_name} {user[0].last_name}", "description": user[0].profession.title, "contacts":contacts}
    return render(request, 'mainapp/index.html', context)

def setprofile(request):
    user = Person.objects.all().values()[0]
    personform=PersonForm(initial=user, prefix="person")
    professionform=ProfessionForm(prefix="prof")
    if request.method=="POST":

        if "person" in request.POST:
            bound_form=PersonForm(request.POST, prefix="person")
            print(bound_form.data)
            #cleaneddata=bound_form.clean()
            #if bound_form.is_valid():
            user = Person.objects.all()[0]
            if user.first_name != bound_form.data.get("person-first_name"):
                user.first_name= bound_form.data.get("person-first_name")
            if user.last_name != bound_form.data.get("person-last_name"):
                user.last_name= bound_form.data.get("person-last_name")
            if user.email != bound_form.data.get("person-email"):
                user.email= bound_form.data.get("person-email")
            if user.number != bound_form.data.get("person-number"):
                user.number= bound_form.data.get("person-number")
            if user.url != bound_form.data.get("person-url"):
                user.url= bound_form.data.get("person-url")
            if user.linkedin != bound_form.data.get("person-linkedin"):
                user.linkedin= bound_form.data.get("person-linkedin")
            if user.twitter != bound_form.data.get("person-twitter"):
                user.twitter= bound_form.data.get("person-twitter")
            if user.github != bound_form.data.get("person-github"):
                user.github= bound_form.data.get("person-github")
            if user.photo != bound_form.data.get("person-photo"):
                user.photo= bound_form.data.get("person-photo")

            user.save()
        if "prof" in request.POST:
            PROFform=ProfessionForm(request.POST, prefix="prof")
            print(PROFform.data)
            PROFform.save()



    context={'form':personform, "professionform":professionform}
    return render(request, 'mainapp/Profile.html', context)
