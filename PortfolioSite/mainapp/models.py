from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40, blank=True)
    number = models.CharField(max_length=20, blank=True)
    url = models.URLField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=50, blank=True)
    github = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    profession = models.ForeignKey("Profession", on_delete=models.CASCADE)
    education = models.ManyToManyField("Education", blank=True)
    career_profile = models.TextField(max_length=1000, blank=True)
    languages = models.ManyToManyField("Languages", blank=True)
    interests = models.ManyToManyField("Interests", blank=True)
    experiences = models.ManyToManyField("Experiences", blank=True)
    companies = models.ManyToManyField("Companies", blank=True)
    roles = models.JSONField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/", blank=True)
    projects = models.ManyToManyField("Project", blank=True)
    project_description = models.TextField(max_length=1000, blank=True)
    def __str__(self):
        return self.first_name +" "+ self.last_name



class Profession(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=50)
    school = models.ForeignKey("School", on_delete=models.CASCADE)
    time = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return self.title
class School(models.Model):
    title = models.CharField(max_length=60)
    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=50, blank=True)
    country = models.ForeignKey("Country", on_delete=models.CASCADE, related_name="Cities")
    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.title


class Languages(models.Model):
    title = models.CharField(max_length=50, blank=True)
    skill = models.CharField(max_length=25, blank=True)
    def __str__(self):
        return self.title + self.skill


class Interests(models.Model):
    title = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.title


class Experiences(models.Model):
    title = models.CharField(max_length=50, blank=True)
    time = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    def __str__(self):
        return self.title


class Companies(models.Model):
    title = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=50, blank=True)
    url = models.URLField(max_length=200, blank=True)
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title
