from django import forms
from .models import *
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "email", "number", "url",
                  "linkedin", "github", "twitter", "photo"]
        labels = {"first_name":"First Name", "last_name":"Last Mame", "email":"Email", "number":"Number", "url":"URL",
                  "linkedin":"Linkedin", "github":"Github", "twitter":"Twitter", "photo":"Photo"}
        widgets = {"first_name":forms.TextInput(), "last_name":forms.TextInput(), "email":forms.EmailInput(), "number":forms.TextInput(), "url":forms.URLInput(),
                  "linkedin":forms.TextInput(), "github":forms.TextInput(), "twitter":forms.TextInput(),
                   "photo":forms.FileInput()},
class ProfessionForm(forms.ModelForm):
    class Meta:
        model = Profession
        fields = ["title"]
        labels = {"title":"profession"}
        widgets ={"title":forms.Select()}


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ["title", "location"]
        labels = {"title": "Education", "location": "Location"}
        widgets = {"title": forms.Select(), "location": forms.Select()}


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ["title", "country"]
        labels = {"title": "City", "country": "Country"}
        widgets = {"title": forms.Select(), "country": forms.Select()}

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ["title"]
        labels = {"title":"country"}
        widgets ={"title":forms.Select()}

class LanguagesForm(forms.ModelForm):
    class Meta:
        model = Languages
        fields = ["title"]
        labels = {"title":"languages"}
        widgets ={"title":forms.SelectMultiple()}

class InterestsForm(forms.ModelForm):
    class Meta:
        model = Interests
        fields = ["title"]
        labels = {"title":"interests"}
        widgets ={"title":forms.Select()}

class ExperiencesForm(forms.ModelForm):
    class Meta:
        model = Experiences
        fields = ["title"]
        labels = {"title":"experiences"}
        widgets ={"title":forms.Select()}

class CompaniesForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = ["title"]
        labels = {"title":"experiences"}
        widgets ={"title":forms.Select()}