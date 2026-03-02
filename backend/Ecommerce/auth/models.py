from django.db import models

# Create your models here.
class Userprofile(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)
    linkedin = models.URLField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.name
