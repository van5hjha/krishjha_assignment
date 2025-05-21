from django.db import models

# Create your models here.
class Doctors(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField(help_text="Years of experience")
    hospital = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}-> {self.specialization}"

