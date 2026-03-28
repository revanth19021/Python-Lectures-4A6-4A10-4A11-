from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField()
    
    def __str__(self):
        return self.username