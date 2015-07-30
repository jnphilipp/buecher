import autocomplete_light

from buechers.models import List, Possession, Read
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
    default_unit = autocomplete_light.ChoiceField('UnitAutocomplete', required=False)

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

class ListFilterForm(forms.Form):
    lst = autocomplete_light.ModelChoiceField('ListAutocomplete')

class ListForm(autocomplete_light.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ListForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})
        self.fields['user'].widget = forms.HiddenInput()

    class Meta:
        model = List
        fields = ('name', 'user')

class ListAdminForm(autocomplete_light.ModelForm):
    class Meta:
        model = List
        fields = '__all__'

class PossessionForm(autocomplete_light.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PossessionForm, self).__init__(*args, **kwargs)
        self.fields['acquisition'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control', 'placeholder':'yyyy-mm-dd'})
        self.fields['price'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['edition'].widget = forms.HiddenInput()

    class Meta:
        model = Possession
        fields = ('user', 'edition', 'acquisition', 'price', 'unit')

class PossessionAdminForm(autocomplete_light.ModelForm):
    class Meta:
        model = Possession
        fields = '__all__'

class ReadForm(autocomplete_light.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReadForm, self).__init__(*args, **kwargs)
        self.fields['started'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control', 'placeholder':'yyyy-mm-dd'})
        self.fields['finished'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control', 'placeholder':'yyyy-mm-dd'})
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['edition'].widget = forms.HiddenInput()

    class Meta:
        model = Read
        fields = ('user', 'edition', 'started', 'finished')

class ReadAdminForm(autocomplete_light.ModelForm):
    class Meta:
        model = Read
        fields = '__all__'
