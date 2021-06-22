#from tinymce.widgets import TinyMCE
from django.forms.widgets import CheckboxSelectMultiple
from django.forms import HiddenInput
from django.forms import ModelForm, Textarea, CharField
from django import forms

from tinymce.widgets import TinyMCE

from .models import Product, Bestellung


class ProductForm(ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Produkt Name'}))
    preis = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Preis'}))
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    #preis = forms.FileField(label='', required=False, widget=forms.FileInput(attrs={"class": 'form-control', "type":'file'}))

    class Meta:
        model = Product
        fields = 'title', 'preis', 'description', 'course', 'img',
        widgets = {
            'description': forms.Textarea(attrs={"class": 'form-control', 'cols':30, 'rows':3, 'style': 'height: 20%;', 'placeholder':'Beschreibung'}),
            'user': HiddenInput(),
            #'course': HiddenInput(),
        }


class BestellungForm(ModelForm):
    firma = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Firma'}))
    #vorname = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Vorname'}))
    #nachnahme = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Nachname'}))
    #email = forms.FileField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'E-Mail Adresse'}))
    #adresse = forms.FileField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Adresse'}))
    #plz = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'PLZ'}))
    #stadt = forms.FileField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Stadt'}))
    #land = forms.FileField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Produkt Name'}))
    #tax_nr = forms.FileField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'UID Nummer'}))
    #tel = forms.FileField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Telefon Nummer'}))

    class Meta:
        model = Bestellung
        fields = 'firma', 'product', #'vorname', 'nachnahme', 'email', 'adresse', 'plz', 'stadt', 'land', 'tax_nr', 'tel',
        widgets = {
            #'description': forms.Textarea(attrs={"class": 'form-control', 'cols':30, 'rows':3, 'style': 'height: 20%;', 'placeholder':'Beschreibung'}),
            'product': HiddenInput(),
            #'course': HiddenInput(),
        }
