from django.shortcuts import render

# Create your views here.
def home(request):
    contacts = {"email":"david@lubomirsky.com", "phone":"(732) 915-2434", "website":" http://127.0.0.1:8000/", "linkedin":"", "github":"", "twitter":"", "snapchat":"bcecam1"}
    context = {"vars": "hello world", "name":"David Lubomirsky", "description":"profesional gamer", "contacts":contacts}
    return render(request, 'mainapp/index.html', context)
