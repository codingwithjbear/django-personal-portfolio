from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/') #upload_to automatically creates a media folder so this would be in media/portfolio/images
    url = models.URLField(blank=True) # blank = true makes the visibity optional
    
    def __str__(self):
        return self.title