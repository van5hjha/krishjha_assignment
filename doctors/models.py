from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Doctors(models.Model):
    creator = models.ForeignKey(User, on_delete =models.CASCADE, default=None, null=True)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField(help_text="Years of experience")
    hospital = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}-> {self.specialization}"

