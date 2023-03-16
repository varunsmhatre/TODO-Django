from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RequestPasswordResetForm(forms.Form):
    email = forms.EmailField(label='Enter your Email')

    def clean_email(self):
        email = self.cleaned_data['email']

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email doesn't exists, Please Register first.")
        return email
