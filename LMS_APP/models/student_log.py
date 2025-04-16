from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # You can hash this if using Django auth

    def __str__(self):
        return self.name
