#from tinymce.widgets import TinyMCE
from django.forms.widgets import CheckboxSelectMultiple
from django.forms import HiddenInput
from django.forms import ModelForm, Textarea, CharField
from django import forms
from .models import *


class CourseForm(ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Kurs Name'}))
    img = forms.FileField(label='', required=False, widget=forms.FileInput(attrs={"class": 'form-control', "type":'file'}))
    #description = forms.Textarea(label='', widget=forms.Textarea(attrs={"class": 'form-control', 'cols': 80, 'rows': 20}))
    class Meta:
        model = Course
        fields = 'name', 'owner', 'img', 'description',
        widgets = {
            'description': forms.Textarea(attrs={"class": 'form-control', 'cols':30, 'rows':3, 'style': 'height: 20%;', 'placeholder':'Beschreibung'}),
            'owner': HiddenInput(),
        }


class CategoryForm(ModelForm):
    titel = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Kategorie Name'}))
    order = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Reihenfolgenummer'}))
    description = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Beschreibung'}))
    class Meta:
        model = Category
        fields = 'titel', 'course', 'order', 'description'
        widgets = {
            'course': HiddenInput(),
        }
