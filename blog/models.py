from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    
    def __str__(self): # functions have nothing to do with the database so it doesn't need to be migrated
        return self.title