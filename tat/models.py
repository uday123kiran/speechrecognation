from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class purpose(models.Model):
    text=models.CharField(max_length=1000)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    

    def __str__(self):
        return self.text
