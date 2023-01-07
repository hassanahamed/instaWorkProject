from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Validators():
    """Class to hold custom validator functions"""

    def alphabet_validator(self, value):
        """
        Validate that the provided value contains only alphabetical characters.
        Raise a ValidationError if the value contains non-alphabetical characters.
        """
        if not value.isalpha():
            raise ValidationError(
                _('%(value)s is not valid as it must contain only alphabets'),
                params={'value': value},
            )

    def phone_number_validator(self, value):
        """
        Validate that the provided value is a phone number with 10 digits.
        Raise a ValidationError if the value is not a 10-digit number.
        """
        if not value.isnumeric() or len(value)!=10:
            raise ValidationError(
                _('%(value)s is not valid as it must be phone number with 10 digits'),
                params={'value': value},
            )
