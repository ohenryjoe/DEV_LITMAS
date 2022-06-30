import uuid

from django.db import models

from person.models import person


class org_type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100, default='current_user')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default='current_user')
    updated_timestamp = models.DateTimeField(auto_now=True)


class organisation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    org_type = models.ForeignKey(org_type, default=1, on_delete=models.PROTECT)
    person = models.ForeignKey(person, default=1, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, default='')
    tin = models.CharField(max_length=30, null=True, blank=True)
    pob = models.CharField(max_length=100, null=True, blank=True)
    physical_address = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    phone2 = models.CharField(max_length=15, null=True, blank=True)
    phone3 = models.CharField(max_length=15, null=True, blank=True)
    phone4 = models.CharField(max_length=15, null=True, blank=True)
    phone5 = models.CharField(max_length=15, null=True, blank=True)
    web_url = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100, default='current_user')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default='current_user')
    updated_timestamp = models.DateTimeField(auto_now=True)
