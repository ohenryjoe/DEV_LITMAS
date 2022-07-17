import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Regions'
        verbose_name = 'Region'



class sub_region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    region = models.ForeignKey(region, default=1, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sub Regions'
        verbose_name = 'Sub Region'

class district(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sub_region = models.ForeignKey(sub_region, default=1, on_delete=models.PROTECT)
    region = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100, unique=True)
    hckey = models.CharField(max_length=10, blank=True, null=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Districts'
        verbose_name = 'District'


class county(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    district = models.ForeignKey(district, default=1, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Counties'
        verbose_name = 'County'


class subcounty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    county = models.ForeignKey(county, default=1, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sub Counties'
        verbose_name = 'Sub County'


class parish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subcounty = models.ForeignKey(subcounty, default=1, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Parishes'
        verbose_name = 'Parish'

    def __str__(self):
        return self.name


class village(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parish = models.ForeignKey(parish, default=1, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Villages'
        verbose_name = 'Village'
