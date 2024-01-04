from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Person)
admin.site.register(Profession)
admin.site.register(Education)
admin.site.register(School)
