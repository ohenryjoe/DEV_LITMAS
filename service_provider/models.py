import uuid
from decimal import Decimal

from django.db import models

from location.models import village
from lookup.models import operation_status, vehicle_model, vehicle_make
from organisation.models import organisation
from person.models import person
from animal.models import animal_type


class tag_installer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(person, default=1, on_delete=models.PROTECT)
    org = models.ForeignKey(organisation, default=1, on_delete=models.PROTECT)
    village = models.ForeignKey(village, default=1, on_delete=models.PROTECT)
    operation_status = models.ForeignKey(operation_status, default=1, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)
    license_issue_date = models.DateField()
    date_est = models.DateField()
    active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100, default='current_user')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default='current_user')
    updated_timestamp = models.DateTimeField(auto_now=True)


class vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle_make = models.ForeignKey(vehicle_make, default=1, on_delete=models.PROTECT)
    vehicle_model = models.ForeignKey(vehicle_model, default=1, on_delete=models.PROTECT)
    number_plate = models.CharField(max_length=100, unique=True)
    date_installed = models.DateField()
    active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100, default='current_user')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default='current_user')
    updated_timestamp = models.DateTimeField(auto_now=True)


class slaughterhouse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(person, default=1, on_delete=models.PROTECT)
    org = models.ForeignKey(organisation, default=1, on_delete=models.PROTECT)
    village = models.ForeignKey(village, default=1, on_delete=models.PROTECT)
    operation_status = models.ForeignKey(operation_status, default=1, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)
    animal_type = models.ManyToManyField(animal_type, through='animal_type_slaughter_house')
    license_issue_date = models.DateField()
    date_est = models.DateField()
    gps_lat = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    gps_long = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100, default='current_user')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default='current_user')
    updated_timestamp = models.DateTimeField(auto_now=True)


class animal_type_slaughter_house(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slaughterhouse = models.ForeignKey(slaughterhouse, default=1, on_delete=models.PROTECT)
    animal_type = models.ForeignKey(animal_type, default=1, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100, default='current_user')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default='current_user')
    updated_timestamp = models.DateTimeField(auto_now=True)

