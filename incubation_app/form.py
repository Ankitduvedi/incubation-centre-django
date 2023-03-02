from django import forms
from .models import Invites


class NewInvites(forms.ModelForm):
    class Meta():
        model = Invites
        fields = '__all__'
