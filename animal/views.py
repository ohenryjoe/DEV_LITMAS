import math

from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render

from animal.forms import register_animal_form
from animal.models import animal as animal_model
from lookup.models import breed, dom_skin_color

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AnimalSerializer


def animal_profile(request, id):
    try:
        this_animal = animal_model.objects.get(pk=id)
    except animal_model.DoesNotExist:
        return render(request, 'error404.html', )
    return render(request, 'animal/animal_profile.html', {'this_animal': this_animal})


def register_animal(request):
    form = register_animal_form()
    if request.method == 'POST':
        form = register_animal_form(request.POST or None, request.FILES or None)
        front_photo = request.FILES.get('front_photo')
        side_photo = request.FILES.get('side_photo')
        if form.is_valid():
            new_animal = animal_model(
                sex=form.cleaned_data['sex'],
                animal_type=form.cleaned_data['animal_type'],
                breed=form.cleaned_data['breed'],
                dominant_colour=form.cleaned_data['dominant_colour'],
                origin=form.cleaned_data['origin'],
                status=form.cleaned_data['status'],
                person=form.cleaned_data['person'],
                org=form.cleaned_data['org'],
                est=form.cleaned_data['est'],
                name=form.cleaned_data['name'],
                date_of_birth=form.cleaned_data['date_of_birth'],
                date_obtained=form.cleaned_data['date_obtained'],
                date_of_death=form.cleaned_data['date_of_death'],
                description=form.cleaned_data['description'],
                front_photo=front_photo,
                side_photo=side_photo,
                created_by=request.user,
                updated_by=request.user,
            )
            new_animal.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Successfully added a new ' + str(form.cleaned_data['sex']) + ' ' +
                                 str(form.cleaned_data['animal_type']) +
                                 ' dominantly ' + str(
                                     form.cleaned_data[
                                         'dominant_colour']) + ' in colour!')
            form = register_animal_form()
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


class AnimalListViewSet(viewsets.ModelViewSet):
    queryset = animal_model.objects.all().order_by('-created_timestamp')[:100]
    serializer_class = AnimalSerializer
    # columns = ['sex',
    #            'animal_type',
    #            'breed',
    #            'dominant_colour',
    #            'origin',
    #            'status',
    #            'person',
    #            'org',
    #            'est',
    #            'animal_number',
    #            'name',
    #            'date_of_birth',
    #            'date_obtained',
    #            'date_of_death',
    #            'description',
    #            'front_photo',
    #            'side_photo',
    #            'active',
    #            'created_by',
    #            'created_timestamp',
    #            'updated_by',
    #            'updated_timestamp',
    #            ]


def list_animal(request):
    animals = animal_model.objects.all()[:20]
    _start = request.GET.get('start')
    _length = request.GET.get('length')
    if _start and _length:
        start = int(_start)
        length = int(_length)
        page = math.ceil(start / length) + 1
        per_page = length

        animals = animals[start:start + length]

    data = serializers.serialize('json', animals)
    return HttpResponse(data, content_type='application/json')


def home(request):
    animals = animal_model.objects.all().order_by('-created_timestamp')[:20]
    data = {'animals': animals}
    return render(request, 'animal/registry.html',data )


def registry(request):
    animals = animal_model.objects.all().order_by('-created_timestamp')[:20]
    return render(request, 'animal/listing.html', {'animals': animals})
