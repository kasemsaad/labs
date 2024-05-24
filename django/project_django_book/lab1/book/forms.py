from django import forms
from author.models import *
from .models import *
class NewBookForm(forms.Form):
    title = forms.CharField(max_length=200,required=True)
    version = forms.IntegerField()
    image = forms.FileField(max_length=100)
    author=forms.ChoiceField(choices=Author.get_all())
class NewBookFormModel(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'
