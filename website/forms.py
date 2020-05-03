from django import forms
from .models import  ContactTickets

class ContactTicketsForm(forms.ModelForm):
    class Meta:
        model = ContactTickets
        fields = ('name','email','subject','message')
        #fields = '__all__'