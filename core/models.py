from django.db import models
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.core.validators import validate_email
from .team_management_exception import TeamManagementFacadeException
from .validators import Validators

# Create your models here.

custom_validators = Validators()

class Role(models.Model):
    role_name = models.CharField(max_length=100, validators=[custom_validators.alphabet_validator])
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.role_name

class Member(models.Model):
    first_name = models.CharField(max_length=100, null=False, validators=[custom_validators.alphabet_validator])
    last_name = models.CharField(max_length=100, null=False, validators=[custom_validators.alphabet_validator])
    email = models.EmailField(max_length=100, unique=True, validators=[validate_email], null=False)
    phone_number = models.CharField(max_length=100, unique=True, validators=[custom_validators.phone_number_validator])
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True) 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.role == 1:
            return self.first_name +" "+self.last_name + " (admin)"
        self.first_name +" "+self.last_name

