from django.db import models

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100, unique=True)
    is_admin = models.CharField(max_length=100) 

    def __str__(self):
        if self.is_admin:
            return self.first_name +" "+self.last_name + " (admin)"
        self.first_name +" "+self.last_name
