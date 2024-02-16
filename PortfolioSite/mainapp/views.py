from django.http import HttpResponseRedirect
from django.shortcuts import render

from mainapp.forms import *
from mainapp.models import *

topic = "css/styles.css"
# Create your views here.
def home(request, id=0):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/auth/login')
    print(request.user, id)
    user = Person.objects.all()
    if not user:
        prof = Profession.objects.create(title="Developer")
        prof.save()
        school = School.objects.create(title="University")
        school.save()
        education = Education.objects.create(title="Specialty", school=school, time="Time")
        education.save()
        languages = Languages.objects.create(title="English", skill="native")
        languages.save()
        interests = Interests.objects.create(title="Interests")
        interests.save()
        experiences = Experiences.objects.create(title="Experiences")
        experiences.save()
        companies = Companies.objects.create(title="Companies")
        companies.save()
        user = Person.objects.create(first_name="John",
                                     last_name="Conor",
                                     email="john_conor@mail.ru",
                                     number="(732) 915-2434",
                                     url="site.john_conor.ru",
                                     profession=prof,
                                     roles={})

        #education.set(user)
        user.save()
        user.education.add(education)
        user.languages.add(languages)
        user.interests.add(interests)
        user.experiences.add(experiences)
        user.companies.add(companies)
        user.save()
       # education.save()
        user = Person.objects.all()
    if id >= len(user):
        id=0
    print(user[id].first_name)
    contacts = {"email": user[id].email, "phone":user[id].number, "website": f"{user[id].url}", "linkedin":"", "github":"", "twitter":"", "snapchat":"bcecam1"}
    edu=user[id].education.all()[0]
    education = {"title": edu.title, "school": edu.school.title, "time": edu.time}
    print(list(user[id].languages.all()))
    context = {"name": f"{user[id].first_name} {user[id].last_name}", "description": user[id].profession.title, "contacts":contacts,
               "edu": education, "user":user[id], "languages": user[id].languages.all(), "interests": user[id].interests.all(), "experiences": user[id].experiences.all(),
               "projects": user[id].projects.all(), "skills": user[id].skills.all(), "topic": topic}
    return render(request, 'mainapp/index.html', context)

def setprofile(request):
    user = Person.objects.all().values()[0]
    personform=PersonForm(initial=user, prefix="person")
    professionform=ProfessionForm(prefix="prof")
    educationform=EducationForm(prefix= "edu")
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
            if user.profession != bound_form.data.get("person-profession"):
                prof_id= int(bound_form.data.get("person-profession"))
                user.profession= Profession.objects.get(id=prof_id)
            if user.education != bound_form.data.get("person-education"):
                edu_id = int(bound_form.data.get("person-education"))
                user.education = Education.objects.get(id=edu_id)


            user.save()
        if "prof" in request.POST:
            PROFform=ProfessionForm(request.POST, prefix="prof")
            print(PROFform.data)
            PROFform.save()
        if "edu" in request.POST:
            EDUform = EducationForm(request.POST, prefix="edu")
            print(EDUform.data)
            EDUform.save()



    context={'form':personform, "professionform":professionform, "educationform":educationform}
    return render(request, 'mainapp/Profile.html', context)



def change(request):
    global topic
    if request.method == "POST":
        styles = {"1":"styles.css", "2":"styles-2.css", "3":"styles-3.css", "4":"styles-4.css",
                  "5":"styles-5.css", "6":"styles-6.css", "7":"styles-7.css", "8":"styles-8.css"}
        topic = "css/"+styles.get(request.POST.get("change"),"styles.css")
        print(request.POST.get("change"))
        print(request.path_info)
    return HttpResponseRedirect("/")

def setprofile2(request):
    user = Person.objects.all().values()[0]
    personform=PersonForm(initial=user, prefix="person")
    professionform=ProfessionForm(prefix="prof")
    educationform=EducationForm(prefix= "edu")
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
            if user.profession != bound_form.data.get("person-profession"):
                prof_id= int(bound_form.data.get("person-profession"))
                user.profession= Profession.objects.get(id=prof_id)
            if user.education != bound_form.data.get("person-education"):
                edu_id = int(bound_form.data.get("person-education"))
                user.education = Education.objects.get(id=edu_id)


            user.save()
        if "prof" in request.POST:
            PROFform=ProfessionForm(request.POST, prefix="prof")
            print(PROFform.data)
            PROFform.save()
        if "edu" in request.POST:
            EDUform = EducationForm(request.POST, prefix="edu")
            print(EDUform.data)
            EDUform.save()



    context={'form':personform, "professionform":professionform, "educationform":educationform}
    return render(request, 'mainapp/EditScreen.html', context)