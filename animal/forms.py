from crispy_forms.helper import FormHelper
from django import forms

from lookup.models import breed, dom_skin_color
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
            'dominant_colour': forms.Select(attrs={"class": "form-control"}),
            'origin': forms.Select(attrs={"class": "form-control"}),
            'status': forms.Select(attrs={"class": "form-control"}),
            'person': forms.Select(attrs={"class": "form-control"}),
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "", "required": "True"}),
            'org': forms.Select(attrs={"class": "form-control"}),
            'est': forms.Select(attrs={"class": "form-control"}),
            'front_photo': forms.ClearableFileInput(
                attrs={"type": "file", "class": "col-lg-6 dropify", "data-height": "200", 'multiple': False, }),
            'side_photo': forms.ClearableFileInput(
                attrs={"type": "file", "class": "col-lg-6  dropify", "data-height": "200", 'multiple': False, }),
            'date_of_birth': DatePickerInput(attrs={"class": "form-control"}),
            'date_obtained': DatePickerInput(attrs={"class": "form-control"}),
            'date_of_death': DatePickerInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={'id': 'summernote', }),
        }

    def clean_avatar(self):
        side_photo = self.cleaned_data['side_photo']
        front_photo = self.cleaned_data['front_photo']

    def __init__(self, *args, **kwargs):
        super(register_animal_form, self).__init__(*args, **kwargs)
        self.fields['breed'].queryset = breed.objects.none()
        self.fields['dominant_colour'].queryset = dom_skin_color.objects.none()
        self.helper = FormHelper()

        # if 'animal_type' in self.data:
        #     try:
        #         this_animal_type = int(self.data.get('animal_type'))
        #         self.fields['breed'].queryset = breed.objects.filter(animal_type__id=this_animal_type).order_by('name')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     # self.fields['dominant_colour'].queryset = self.instance.animal_type.breed_set.order_by('name')

        if 'animal_type' in self.data:
            try:
                this_animal_type = int(self.data.get('animal_type'))
                self.fields['breed'].queryset = breed.objects.filter(animal_type__id=this_animal_type).order_by(
                    'name')
                if 'breed' in self.data:
                    try:
                        BreedId = int(self.data.get('breed'))
                        self.fields['dominant_colour'].queryset = dom_skin_color.objects.filter(
                            breed_id=BreedId).order_by(
                            'name')
                    except (ValueError, TypeError):
                        pass  # invalid input from the client; ignore and fallback to empty City queryset
                elif self.instance.pk:
                    self.fields['dominant_colour'].queryset = self.instance.breed.dom_skin_color_set.order_by(
                        'name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            # self.fields['breed'].queryset = self.instance.animal_type.breed_set.order_by('name')
            pass