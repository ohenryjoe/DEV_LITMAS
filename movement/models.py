import uuid
from decimal import Decimal

from django.db import models

from animal.models import animal
from location.models import village
from lookup.models import animal_type, transfer_fee_type, mode_of_transport, transfer_status, transit_category, \
    movement_type, transfer_purpose, quarantine_reason, quarantine_status, transfer_action_type, payment_mode, \
    payment_channel
from organisation.models import organisation
from person.models import person
from service_provider.models import vehicle


class transfer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal = models.ManyToManyField(animal, through='animal_transfer')
    vehicle = models.ManyToManyField(vehicle, through='vehicle_transfer')
    village = models.ForeignKey(village, default=1, on_delete=models.PROTECT)
    person_ben = models.ForeignKey(person, related_name='beneficiary', default=1, on_delete=models.PROTECT)
    org_ben = models.ForeignKey(organisation, default=1, on_delete=models.PROTECT)
    transfer_purpose = models.ForeignKey(transfer_purpose, default=1, on_delete=models.PROTECT)
    transit_category = models.ForeignKey(transit_category, default=1, on_delete=models.PROTECT)
    movement_type = models.ForeignKey(movement_type, default=1, on_delete=models.PROTECT)
    transfer_status = models.ForeignKey(transfer_status, default=1, on_delete=models.PROTECT)
    transfer_initiated_by = models.ForeignKey(person, related_name='initiated_by', default=1, on_delete=models.PROTECT)
    mode_of_transport = models.ForeignKey(mode_of_transport, default=1, on_delete=models.PROTECT)
    transfer_date = models.DateField()
    expected_arrival_date = models.DateField()
    permit_number = models.CharField(max_length=50, default=None)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)


class animal_transfer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal = models.ForeignKey(animal, default=1, on_delete=models.PROTECT)
    transfer = models.ForeignKey(transfer, default=1, on_delete=models.PROTECT)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)


class vehicle_transfer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transfer = models.ForeignKey(transfer, default=1, on_delete=models.PROTECT)
    vehicle = models.ForeignKey(vehicle, default=1, on_delete=models.PROTECT)
    driver = models.ForeignKey(person, default=1, on_delete=models.PROTECT)
    driver_permit_number = models.CharField(max_length=50, default=None)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)


class animal_transfer_action(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transfer = models.ForeignKey(transfer, default=1, on_delete=models.PROTECT)
    action_type = models.ForeignKey(transfer_action_type, default=1, on_delete=models.PROTECT)
    action_date = models.DateField()
    action_reason = models.CharField(max_length=400, default=None)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)


class animal_transfer_transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transfer = models.ForeignKey(transfer, default=1, on_delete=models.PROTECT)
    fee_type = models.ForeignKey(transfer_fee_type, default=1, on_delete=models.PROTECT)
    payment_mode = models.ForeignKey(payment_mode, default=1, on_delete=models.PROTECT)
    payment_channel = models.ForeignKey(payment_channel, default=1, on_delete=models.PROTECT)
    fee_amount = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    payment_date = models.DateField()
    invoice_number = models.CharField(max_length=60, default=None)
    invoice_date = models.DateField()
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)


class transfer_route_checkpoint(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transfer = models.ForeignKey(transfer, default=1, on_delete=models.PROTECT)
    checkpoint_location = models.ForeignKey(village, default=1, on_delete=models.PROTECT)
    checkpoint_order = models.PositiveIntegerField(unique=True)
    checkpoint_name = models.CharField(max_length=200, default='xxx')
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)


class transfer_route_readerpoint(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transfer = models.ForeignKey(transfer, default=1, on_delete=models.PROTECT)
    readerpoint_location = models.ForeignKey(village, default=1, on_delete=models.PROTECT)
    readerpoint_order = models.PositiveIntegerField(unique=True)
    readerpoint_name = models.CharField(max_length=200, default='xxx')
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)


class quarantine_notice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reason = models.ForeignKey(quarantine_reason, default=1, on_delete=models.PROTECT)
    animal_type = models.ManyToManyField(animal_type, through='quarantine_animal_type')
    status = models.ForeignKey(quarantine_status, default=1, on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)
    start_date = models.DateField()
    expected_end_date = models.DateField()
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)


class quarantine_animal_type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quarantine_notice = models.ForeignKey(quarantine_notice, default=1, on_delete=models.PROTECT)
    animal_type = models.ForeignKey(animal_type, default=1, on_delete=models.PROTECT)
    active = models.BooleanField(default=False)
    start_date = models.DateField()
    expected_end_date = models.DateField()
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)
