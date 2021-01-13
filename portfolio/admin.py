from django.contrib import admin

# Register your models here.

from .models import Project

admin.site.register(Project) # says that I want to see this model inside of admin