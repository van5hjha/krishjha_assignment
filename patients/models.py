from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Patients(models.Model):
    creator = models.ForeignKey(User, on_delete =models.CASCADE, default=None, null=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    disease = models.CharField(max_length=225)

    def __str__(self):
        return self.name
    
