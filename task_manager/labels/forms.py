from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Label


class LabelCreationForm(forms.ModelForm):
    name = forms.CharField(label=_('Name'))

    class Meta:
        model = Label
        fields = ['name']
