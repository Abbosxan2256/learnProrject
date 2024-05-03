from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegisterModelForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')


def clean_password(self):
    return make_password(self.clean_data.get('password'))
