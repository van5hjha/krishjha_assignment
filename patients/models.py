from django.db import models

# Create your models here.
class Patients(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    disease = models.CharField(max_length=225)

    def __str__(self):
        return self.name
    
