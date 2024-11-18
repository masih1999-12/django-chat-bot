from django.core.validators import RegexValidator
mobile_validator = RegexValidator(
    regex=r'^09\d{9}$',
    message="Phone number must start with 09 and have a total of 11 digits.",
    code='invalid_phone_number',
)