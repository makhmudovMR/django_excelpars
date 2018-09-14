from django import forms
from .models import ObjectInfo

class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ObjectInfoForm(forms.ModelForm):

    class Meta:
        model = ObjectInfo
        fields = '__all__'