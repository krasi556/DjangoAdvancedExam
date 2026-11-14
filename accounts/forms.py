from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.fields import EmailField

from accounts.models import User


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#
# UserModel = get_user_model()
#
#
# class NewUserForm(UserCreationForm):
#     class Meta:
#         model = NewUser
#         fields = ['email']
#
#
# class NewUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = NewUser
