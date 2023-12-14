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
    education_start = models.CharField(max_length=50, blank=True)
    education_end = models.CharField(max_length=50, blank=True)
    career_profile = models.TextField(max_length=1000, blank=True)
    languages = models.ManyToManyField("Languages", blank=True)
    interests = models.ManyToManyField("Interests", blank=True)
    experiences = models.ManyToManyField("Experiences", blank=True)
    companies = models.ManyToManyField("Companies", blank=True)
    roles = models.JSONField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/", blank=True)


class Profession(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=50, blank=True)
    location = models.ForeignKey("City", on_delete=models.CASCADE)


class City(models.Model):
    title = models.CharField(max_length=50, blank=True)
    country = models.ForeignKey("Country", on_delete=models.CASCADE, related_name="Cities")


class Country(models.Model):
    title = models.CharField(max_length=50, blank=True)


class Languages(models.Model):
    title = models.CharField(max_length=15, blank=True)


class Interests(models.Model):
    title = models.CharField(max_length=50, blank=True)


class Experiences(models.Model):
    title = models.CharField(max_length=50, blank=True)


class Companies(models.Model):
    title = models.CharField(max_length=50, blank=True)

