import math
import uuid

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from animal.forms import register_animal_form, register_animal_to_est_form
from animal.models import animal as animal_model
from establishment.models import establishment
from lookup.models import breed, dom_skin_color
from organisation.models import organisation
from person.models import person
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


def register_animal_to_est(request, est_id):
    est_id = est_id
    form = register_animal_to_est_form()
    if establishment.objects.filter(pk=est_id).count() > 0:
        this_est = establishment.objects.get(id=est_id)
        if this_est.org:
            org_owner = this_est.org.name
        else:
            org_owner = this_est.name
        if this_est.person:
            person_owner = this_est.person.person_fullname()
        else:
            person_owner = this_est.name
    else:
        this_est = ''
        org_owner = 'Unknown'
        person_owner = 'Unknown'
    print('Est Name:', this_est.name)
    context = {'form': form,
               'this_est': this_est,
               'person_owner': person_owner,
               'org_owner': org_owner
               }
    if request.method == 'POST':
        form = register_animal_to_est_form(request.POST or None, request.FILES or None)
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
                person=person_owner,
                org=org_owner,
                est=this_est,
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
                                         'dominant_colour']) + ' in colour to ' + this_est.name + ' ' + this_est.est_type)
            form = register_animal_form()
            return render(request, 'animal/new_registration_to_establishment.html',
                          {'form': form})
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong! Form is not valid')
            return render(request, 'animal/new_registration_to_establishment.html', context)
    return render(request, 'animal/new_registration_to_establishment.html',
                  context)


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
    columns = ['sex',
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
               'created_by',
               'created_timestamp',
               'updated_by',
               'updated_timestamp',
               ]


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
    animals = animal_model.objects.all().order_by('-created_timestamp')
    data = {'animals': animals}
    return render(request, 'animal/registry.html', data)


def registry(request):
    animals = animal_model.objects.all().order_by('-created_timestamp')
    return render(request, 'animal/listing.html', {'animals': animals})
