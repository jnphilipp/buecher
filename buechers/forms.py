import autocomplete_light

from buechers.models import Possession, Read
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm as AuthAuthenticationForm, UserChangeForm as AuthUserChangeForm, UserCreationForm as AuthUserCreationForm

class AuthenticationForm(AuthAuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'username'
        self.fields['username'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control', 'placeholder':'username'})
        self.fields['password'].label = 'password'
        self.fields['password'].widget = forms.PasswordInput(attrs={'autocomplete':'off', 'class':'form-control', 'placeholder':'password'})

class UserChangeForm(AuthUserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})
        self.fields['email'].widget = forms.EmailInput(attrs={'autocomplete':'off', 'class':'form-control'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

class UserCreationForm(AuthUserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'autocomplete':'off', 'class':'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'autocomplete':'off', 'class':'form-control'})

class PossessionForm(autocomplete_light.ModelForm):
    class Meta:
        model = Possession
        fields = '__all__'

class ReadForm(autocomplete_light.ModelForm):
    class Meta:
        model = Read
        fields = '__all__'
