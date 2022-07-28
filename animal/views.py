from django.contrib import messages
from django.shortcuts import render, redirect

from animal.forms import register_animal_form
from lookup.models import breed, dom_skin_color


def register_animal(request):
    form = register_animal_form()
    if request.method == 'POST':
        form = register_animal_form(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Successfully added a new directorate  [' + form.cleaned_data[
                                     'animal_number'] + '!')
            return render(request, 'animal/new_registration.html',
                          {'form': form})
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong! Form is not valid')
            return render(request, 'animal/new_registration.html', {'form': form})
    return render(request, 'animal/new_registration.html',
                  {'form': form})


def load_breeds(request):
    animal_type = request.GET.get('animal_type')
    type_breed = breed.objects.filter(animal_type__id=animal_type).order_by('name')
    return render(request, 'animal/animal_type_dropdown_list.html', {'type_breed': type_breed})


def load_colours(request):
    breed = request.GET.get('breed')
    dom_colour = dom_skin_color.objects.filter(breed__id=breed).order_by('name')
    return render(request, 'animal/dom_colour_dropdown_list.html', {'dom_colour': dom_colour})
