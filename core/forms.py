from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.core.validators import validate_email
from .models import Member, Role
from .team_management_exception import TeamManagementFacadeException



class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
