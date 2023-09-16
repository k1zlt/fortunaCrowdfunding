from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'avatar', 'biography')

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['role'].widget = forms.Select(choices=User.roles)

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])  # Use 'password1' instead of 'password'
        if commit:
            user.save()
        return user