from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from django_select2.forms import Select2Widget

from lookup.models import animal_type, breed
from .models import animal
from .widget import DatePickerInput


class register_animal_form(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = animal

        # specify fields to be used
        fields = [
            'sex',
            'animal_type',
            'breed',
            'dominant_colour',
            'origin',
            'status',
            'person',
            'org',
            'est',
            'animal_number',
            'name',
            'date_of_birth',
            'date_obtained',
            'date_of_death',
            'description',
            'front_photo',
            'side_photo',
            'active',
        ]

        widgets = {
            'animal_type': forms.Select(attrs={"class": "form-control"}),
            'breed': forms.Select(attrs={"class": "form-control"}),
            'sex': forms.Select(attrs={"class": "form-control"}),
            'dominant_color': forms.Select(attrs={"class": "form-control"}),
            'origin': forms.Select(attrs={"class": "form-control"}),
            'status': forms.Select(attrs={"class": "form-control"}),
            'person': forms.Select(attrs={"class": "form-control"}),
            'org': forms.Select(attrs={"class": "form-control"}),
            'est': forms.Select(attrs={"class": "form-control"}),
            'front_photo': forms.ClearableFileInput(attrs={"class": "form-control", 'multiple': False, }),
            'side_photo': forms.ClearableFileInput(attrs={"class": "form-control", 'multiple': False, }),
            'name': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Employee Full Names'}),
            'date_of_birth': DatePickerInput(attrs={"class": "form-control"}),
            'date_obtained': DatePickerInput(attrs={"class": "form-control"}),
            'date_of_death': DatePickerInput(attrs={"class": "form-control"}),
        }

    def clean_avatar(self):
        side_photo = self.cleaned_data['side_photo']
        front_photo = self.cleaned_data['front_photo']
