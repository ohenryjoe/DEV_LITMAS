from crispy_forms.helper import FormHelper
from django import forms

from location.models import village as vill
from .models import establishment


class register_establishment_form(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = establishment

        # specify fields to be used
        fields = [
            'est_type',
            'person',
            'org',
            'name',
            'est_size_acres',
            'village',
            'year_est',
            'gps_lat',
            'gps_long',
            'active',
        ]

        widgets = {
            'est_type': forms.Select(attrs={"class": "form-control select2-show-search form-select"}),
            'person': forms.Select(attrs={"class": "form-control select2 form-select"}),
            'org': forms.Select(attrs={"class": "form-control select2 form-select"}),
            'village': forms.Select(attrs={"class": "form-control select2 form-select"}),
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'est_size_acres': forms.TextInput(attrs={"class": "form-control"}),
            'year_est': forms.TextInput(attrs={"class": "form-control"}),
            'gps_lat': forms.TextInput(attrs={"class": "form-control"}),
            'gps_long': forms.TextInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(register_establishment_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['village'].queryset = vill.objects.none()

        if 'parish' in self.data:
            try:
                parish = self.data.get('parish')
                self.fields['village'].queryset = vill.objects.filter(
                    parish_id=parish).order_by(
                    'name')
            except (ValueError, TypeError):
                self.fields['village'].queryset = vill.objects.none()
