from django.core.exceptions import ValidationError


class PasswordMustBeOfUnique:
    def validate(self, password, user=None):
        if len(set(password)) < 6:
            raise ValidationError('Password must contain at least 6 symbols')

    def get_help_text(self):
        return 'password must contain at least 6 symbols '
