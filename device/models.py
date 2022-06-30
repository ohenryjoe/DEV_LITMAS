import uuid
from decimal import Decimal

from django.db import models
from lookup.models import animal_type, tag_status
from person.models import person


class tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal_type = models.ForeignKey(animal_type, default=1, on_delete=models.PROTECT)
    tag_status = models.ForeignKey(tag_status, default=1, on_delete=models.PROTECT)
    installed_by = models.ForeignKey(person, default=1, on_delete=models.PROTECT)
    date_installed = models.DateField()
    rfid = models.CharField(max_length=40, default='xx')
    active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100, default='current_user')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default='current_user')
    updated_timestamp = models.DateTimeField(auto_now=True)


class chip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = models.ForeignKey(tag, default=1, on_delete=models.PROTECT)
    manufacturer = models.CharField(max_length=40, default='')
    frequency = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    iso_standard = models.CharField(max_length=40, default='ISO')
    configurable = models.BooleanField()
    uid_size = models.PositiveSmallIntegerField()
    user_memory = models.PositiveSmallIntegerField()
    write_protection = models.BooleanField()
    access_key = models.CharField(max_length=200, blank=True, null=True)
    write_endurance=models.PositiveSmallIntegerField()
    active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100, default='current_user')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default='current_user')
    updated_timestamp = models.DateTimeField(auto_now=True)

