from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Validators():

    def alphabet_validator(self, value):
        if not value.isalpha():
            raise ValidationError(
                _('%(value)s is not valid as it must contain only alphabets'),
                params={'value': value},
            )

    def phone_number_validator(self, value):
        if not value.isnumeric() or len(value)!=10:
            raise ValidationError(
                _('%(value)s is not valid as it must be phone number with 10 digits'),
                params={'value': value},
            )
