from django import forms
from .models import  Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','subject','body','post','parent')
        #fields = '__all__'