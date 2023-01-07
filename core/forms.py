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

    # def clean(self):

    #     try:
    #         data = self.cleaned_data
    #         email = data.get("email")
    #         validate_email(email)
    #         return data

    #     except ValidationError as e:
    #         e = list(e)
    #         print(e[0])
    #         raise TeamManagementFacadeException(message=e[0])
    #         # return render(request, 'new.html', {'member': new_member, 'errorMessage':e[0]})

    #     except IntegrityError as e:
    #         print(e)
    #         e = str(e)
    #         error_message = e
    #         if 'core_member.email' in e:
    #             error_message = 'Email Address already exists'
    #         if 'core_member.phone_number' in e:
    #             error_message = 'Phone number already exists'
    #         raise TeamManagementFacadeException(message=error_message)
    #         # return render(request, 'new.html', {'member': new_member, 'errorMessage':error_message})

    

    
    

            

