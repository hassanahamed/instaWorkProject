from django.db import models
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.core.validators import validate_email

# Import custom exception and validator classes
from .team_management_exception import TeamManagementFacadeException
from .validators import Validators

"""
    This are the model classes required for the Django app
    We have two tables - 
            1) Role
            2) Member
    Each member can be assigned a role. For now role table is populated with 
        id      role_name
        1           Admin
        2           Regular
    We can extend this in future to add more roles.
"""

# Create an instance of the Validators class to use as custom validators
custom_validators = Validators()

class Role(models.Model):
    """Model to represent a role within the team"""
    role_name = models.CharField(
        max_length=100, 
        validators=[custom_validators.alphabet_validator]
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.role_name

class Member(models.Model):
    """Model to represent a team member
        FirstName, LastName email and email are mandatory
        FirstName, LastName comes with a custom validator to check for alphabets
        Email comes with default Django validator
        PhoneNumber has a custom validator to check if for numbers if length 10
        Role is foreign key and is set as null on deletion of role ini Role table.
    
    """
    first_name = models.CharField(
        max_length=100, 
        null=False,                                             
        validators=[custom_validators.alphabet_validator]
    )
    last_name = models.CharField(
        max_length=100, 
        null=False, 
        validators=[custom_validators.alphabet_validator]
    )
    email = models.EmailField(
        max_length=100, 
        unique=True, 
        validators=[validate_email], 
        null=False
    )
    phone_number = models.CharField(
        max_length=100, 
        unique=True, 
        validators=[custom_validators.phone_number_validator],
        null=True,
        blank=True
    )
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True) 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Return a string representation of the member with the role appended if the role is 'admin'"""
        if self.role == 1:
            return self.first_name +" "+self.last_name + " (admin)"
        self.first_name +" "+self.last_name
