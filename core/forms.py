from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))



class SignupForm(UserCreationForm):

    is_verified = forms.BooleanField(initial=False, required=True, widget=forms.CheckboxInput())

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'is_verified')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Your username',
            'class': 'w-full py-4 px-6 rounded-xl',
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Your password',
            'class': 'w-full py-4 px-6 rounded-xl',
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Repeat password',
            'class': 'w-full py-4 px-6 rounded-xl',
        })
