from django import forms
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _("Ім'я")}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Email"}) ,max_length=50, validators=[EmailValidator(message='Введено не коректний email')])
    subject_message = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _("Тема")}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), max_length=2000)
    button = forms.CharField(label='', widget=forms.TextInput(attrs={'type':'submit', 'class':'btn btn-info', 'value': _('Надіслати'), 'style': 'width: 100%'}))