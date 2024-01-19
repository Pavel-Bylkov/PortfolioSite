from django.shortcuts import render

from mainapp.forms import *
from mainapp.models import *


# Create your views here.
def home(request):

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
    print(user[0].first_name)
    contacts = {"email": user[0].email, "phone":user[0].number, "website": f"{user[0].url}", "linkedin":"", "github":"", "twitter":"", "snapchat":"bcecam1"}
    edu=user[0].education.all()[0]
    education = {"title": edu.title, "school": edu.school.title, "time": edu.time}
    print(list(user[0].languages.all()))
    context = {"name": f"{user[0].first_name} {user[0].last_name}", "description": user[0].profession.title, "contacts":contacts,
               "edu": education, "user":user[0], "languages": user[0].languages.all(), "interests": user[0].interests.all(), "experiences": user[0].experiences.all(),
               "projects": user[0].projects.all(), "skills": user[0].skills.all()}
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
