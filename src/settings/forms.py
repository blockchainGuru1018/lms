#from tinymce.widgets import TinyMCE
from django.forms.widgets import CheckboxSelectMultiple
from django.forms import HiddenInput
from django.forms import ModelForm, Textarea
from django import forms

from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, Row, Column

from .models import Settings


class SettingsForm(ModelForm):
    #unternehmens_name = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Produkt Name'}))
    #preis = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Preis'}))
    #description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    #preis = forms.FileField(label='', required=False, widget=forms.FileInput(attrs={"class": 'form-control', "type":'file'}))
    #name = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder':'Kurs Name'}))

    class Meta:
        model = Settings
        fields = 'unternehmens_name', 'datenschutz', 'impressium', 'logo_img', 'strasse', 'strasse2', 'ort', 'land', 'telefon', 'email', 'plz', 'is_active',

        error_meassages ={
            "unternehmens_name": {
                "max_leagth": "Zu lang",
                "required": "ist ein Pflicjtfehlt"
                },
        }

    def __init__(self, *args, **kwargs):
        super(SettingsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.fields['is_active'].widget = HiddenInput()
        self.fields['is_active'].initial = 'True'
        #self.fields['datenschutz'].label = ''

        #self.fields['datenschutz'].help_text = "Please select bla bla bla"

        self.helper.layout = Layout(
            #Field('unternehmens_name', css_class='input-xlarge'),
            #Field('description', rows="3", css_class='input-xlarge'),

            Row(
                Column('unternehmens_name', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('strasse', css_class='form-group col-md-2 mb-0'),
                Column('strasse2', css_class='form-group col-md-2 mb-0'),
                Column('ort', css_class='form-group col-md-2 mb-0'),
                Column('plz', css_class='form-group col-md-2 md-0'),
                Column('land', css_class='form-group col-md-2 mb-0'),
                Column('telefon', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('datenschutz', css_class='form-group col-md-12 mb-0'),
                Column('impressium', css_class='form-group col-md-12 mb-0'),
                Column('is_active', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
        )
        self.helper.layout.append(Submit('login', 'Log me in', css_class='btn btn-primary btn-lg'))

        #self.helper.form_class = 'form-horizontal'
        #self.helper.label_class = 'col-xs-2 hide'
        #self.helper.field_class = 'col-lg-5'
