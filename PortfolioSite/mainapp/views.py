from django.shortcuts import render

from mainapp.models import Person


# Create your views here.
def home(request):

    user = Person.objects.all()
    print(user[0].first_name)
    contacts = {"email":"david@lubomirsky.com", "phone":"(732) 915-2434", "website":" http://127.0.0.1:8000/", "linkedin":"", "github":"", "twitter":"", "snapchat":"bcecam1"}
    context = {"vars": "hello world", "name":f"{user[0].first_name} {user[0].last_name}", "description":"profesional gamer", "contacts":contacts}
    return render(request, 'mainapp/index.html', context)
