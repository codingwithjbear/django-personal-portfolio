from django.contrib import admin

# Register your models here.
from .models import Blog

admin.site.register(Blog) # says that I want to see this model inside of admin