# Directorate Form
from crispy_forms.helper import FormHelper
from django import forms

from lookup.models import breed, animal_type


class animal_type_form(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = animal_type

        # specify fields to be used
        fields = ['name', 'description', 'active', ]

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Name'}),
            'active': forms.TextInput(attrs={"class": "checkbox"}),
            'description': forms.Textarea(attrs={'rows': 2, 'cols': 12, "class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(animal_type_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


class breed_form(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = breed

        # specify fields to be used
        fields = ['name', 'description', 'active', ]

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Name'}),
            'active': forms.TextInput(attrs={"class": "checkbox"}),
            'description': forms.Textarea(attrs={'rows': 2, 'cols': 12, "class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(breed_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
