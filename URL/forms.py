from django import forms
from django.forms import ModelForm, TextInput
from .models import URL

class URLForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(URLForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = URL
        fields = ['url']
        widgets = {
            'url': TextInput(attrs={'required':True}),
        }