from django.contrib import messages
from django.shortcuts import render, redirect

from animal.forms import register_animal_form
from lookup.models import breed


def register_animal(request):
    form = register_animal_form()
    if request.method == 'POST':
        form = register_animal_form(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Successfully added a new directorate  [' + form.cleaned_data[
                                     'animal_number'] + '!')
            return redirect('animal_register')
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong! Form is not valid')
            return render(request, 'animal/register.html', {'form': form})
    return render(request, 'animal/register.html',
                  {'form': form})


def load_breeds(request):
    animal_type_id = request.GET.get('animal_type')
    type_breed = breed.objects.filter(animal_type_id=animal_type_id).order_by('name')
    return render(request, 'animal/animal_type_dropdown_list.html', {'type_breed': type_breed})
