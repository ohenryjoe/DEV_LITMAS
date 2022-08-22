import uuid

from django.contrib import messages
from django.shortcuts import render, redirect

from establishment.forms import register_establishment_form
from establishment.models import establishment
from location.models import sub_region as sreg, sub_region
from location.models import district as dist
from location.models import county as cty
from location.models import subcounty as scty
from location.models import parish as par
from location.models import village as vill


def register_establishment(request):
    form = register_establishment_form()
    subregion = sub_region.objects.all().order_by('name')
    if request.method == 'POST':
        form = register_establishment_form(request.POST or None)
        thisvill = request.POST.get('village')
        village_uuid = vill.objects.get(id=uuid.UUID(thisvill).hex)
        if form.is_valid():
            est = establishment(
                est_type=form.cleaned_data['est_type'],
                person=form.cleaned_data['person'],
                org=form.cleaned_data['org'],
                village=village_uuid,
                name=form.cleaned_data['name'],
                est_size_acres=form.cleaned_data['est_size_acres'],
                year_est=form.cleaned_data['year_est'],
                gps_lat=form.cleaned_data['gps_lat'],
                gps_long=form.cleaned_data['gps_long'],
                created_by=request.user,
                updated_by=request.user,
            )
            est.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Successfully added a new establishment  [' + form.cleaned_data[
                                     'name'] + '!')
            return render(request, 'establishment/new_registration.html',
                          {'form': form, 'subregion': subregion})
        else:
            print(village_uuid)
            messages.add_message(request, messages.ERROR, 'Something went wrong! Form is not valid')
            return render(request, 'establishment/new_registration.html', {'form': form, 'subregion': subregion})
    return render(request, 'establishment/new_registration.html',
                  {'form': form, 'subregion': subregion})


def load_district(request):
    sub_region = request.GET.get('sub_region')
    district = dist.objects.filter(sub_region__id=sub_region).order_by('name')
    return render(request, 'establishment/district_dropdown_list.html', {'district': district})


def load_county(request):
    district = request.GET.get('district')
    county = cty.objects.filter(district__id=district).order_by('name')
    return render(request, 'establishment/county_dropdown_list.html', {'county': county})


def load_subcounty(request):
    county = request.GET.get('county')
    subcounty = scty.objects.filter(county__id=county).order_by('name')
    return render(request, 'establishment/subcounty_dropdown_list.html', {'subcounty': subcounty})


def load_parish(request):
    subcounty = request.GET.get('subcounty')
    parish = par.objects.filter(subcounty__id=subcounty).order_by('name')
    return render(request, 'establishment/parish_dropdown_list.html', {'parish': parish})


def load_village(request):
    parish = request.GET.get('parish')
    village = vill.objects.filter(parish__id=parish).order_by('name')
    return render(request, 'establishment/village_dropdown_list.html', {'village': village})
