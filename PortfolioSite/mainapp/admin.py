from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Person)
admin.site.register(Profession)
admin.site.register(Education)
admin.site.register(School)
admin.site.register(Languages)
admin.site.register(Interests)
admin.site.register(Experiences)
admin.site.register(Project)
admin.site.register(Skills)
