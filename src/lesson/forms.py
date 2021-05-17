#from tinymce.widgets import TinyMCE
from django.forms.widgets import CheckboxSelectMultiple
from django.forms import HiddenInput
from django.forms import ModelForm, Textarea
from django import forms

from course.models import Category
from .models import Lesson, Lecture

class LessonForm(ModelForm):
    name = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Lektionsname'}))
    order = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Reihenfolgenummer'}))
    link_url = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Viemo link'}))
    description = forms.CharField(label='', required=False, widget=forms.Textarea(attrs={"class": 'form-control', 'style': 'height: 20%;', 'placeholder':'Beschreibung','rows': 4, 'cols': 40}))
    class Meta:
        model = Lesson
        fields = 'category', 'name', 'order', 'link_url', 'is_active', 'description',
        widgets = {
            'category': HiddenInput(),
        }

class LectureForm(ModelForm):
    name = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Name Dokument'}))
    description = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Beschreibung'}))
    photo = forms.FileField(label='', required=True, widget=forms.FileInput(attrs={"class": 'form-control', "type":'file'}))
    class Meta:
        model = Lecture
        fields = 'name', 'lecture', 'description', 'photo'
        widgets = {
            'lecture': HiddenInput(),
        }

class LectureFormUpdate(ModelForm):
    name = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Name Dokument'}))
    description = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Beschreibung'}))
    photo = forms.FileField(label='', required=True, widget=forms.FileInput(attrs={"class": 'form-control', "type":'file'}))
    class Meta:
        model = Lecture
        fields = 'name', 'photo', 'lecture', 'description'
        widgets = {
            'lecture': HiddenInput(),
        }
