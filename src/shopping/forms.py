#from tinymce.widgets import TinyMCE
from django import forms
from django.forms import HiddenInput
from django.forms import ModelForm, Textarea, CharField
from django.forms.widgets import CheckboxSelectMultiple
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
    firma = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Firma'}))
    vorname = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Vorname'}))
    nachnahme = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Nachname'}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'E-Mail Adresse'}))
    adresse = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Adresse'}))
    plz = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'PLZ'}))
    stadt = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Stadt'}))
    land = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Produkt Name'}))
    tax_nr = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'UID Nummer'}))
    tel = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Telefon Nummer'}))

    def __init__(self, *args, **kwargs):
        super(BestellungForm, self).__init__(*args, **kwargs)
        # Making location required
        self.fields['firma'].required = False


    class Meta:
        model = Bestellung
        fields = 'firma', 'vorname', 'nachnahme', 'email', 'adresse', 'plz', 'stadt', 'land', 'tax_nr', 'tel',
        
        error_messages = {
            'firma': {
                'required': ("Application field is required"),
            },
        }
