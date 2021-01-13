from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all() # all the project objects from the database are placed into this variable
    return render(request, 'portfolio/home.html', {'projects':projects}) #pass into the template a dictonary with the key being "projects" then pass forward the project objects 

