from django.db import models

#makemigrations -- create change and store in a file
#migrate-- apply the pending changes create by makemigrations
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=1122)
    email=models.EmailField()
    phone=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()
    

    def __str__(self):
        return self.name

'''
from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Entities(models.Model):
    Description = models.CharFile(max_lenght=100)
    Parameter = models.CharField(max_length=200)
    Probability = models.CharFiled(max_length=100)
    Page=d=models.IntegerField()

    def __str__(self):
        return self.Description

'''


