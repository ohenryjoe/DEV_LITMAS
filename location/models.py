import uuid
from operator import concat

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return concat(concat(self.code, '-'), self.name)

    class Meta:
        verbose_name_plural = 'Regions'
        verbose_name = 'Region'


class sub_region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    region = models.ForeignKey(region, default=None, on_delete=models.PROTECT)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, unique=True)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return concat(concat(self.code, '-'), self.name)

    class Meta:
        verbose_name_plural = 'Sub Regions'
        verbose_name = 'Sub Region'


class district(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    region = models.ForeignKey(region, default=None, on_delete=models.PROTECT)
    sub_region = models.ForeignKey(sub_region, default=None, on_delete=models.PROTECT)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, default=None,)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return concat(concat(self.code, '-'), self.name)

    class Meta:
        verbose_name_plural = 'Districts'
        verbose_name = 'District'


class county(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    region = models.ForeignKey(region, default=None, on_delete=models.PROTECT)
    sub_region = models.ForeignKey(sub_region, default=None, on_delete=models.PROTECT)
    district = models.ForeignKey(district, default=None, on_delete=models.PROTECT)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100,blank=True)
    constituency = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return concat(concat(self.code, '-'), self.name)

    class Meta:
        verbose_name_plural = 'Counties'
        verbose_name = 'County'


class subcounty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    region = models.ForeignKey(region, default=None, on_delete=models.PROTECT)
    sub_region = models.ForeignKey(sub_region, default=None, on_delete=models.PROTECT)
    district = models.ForeignKey(district, default=None, on_delete=models.PROTECT)
    county = models.ForeignKey(county, default=None, on_delete=models.PROTECT)
    code = models.CharField(max_length=20, default=None, unique=True)
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return concat(concat(self.code, '-'), self.name)

    class Meta:
        verbose_name_plural = 'Sub Counties'
        verbose_name = 'Sub County'


class parish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    region = models.ForeignKey(region, default=None, on_delete=models.PROTECT)
    sub_region = models.ForeignKey(sub_region, default=None, on_delete=models.PROTECT)
    district = models.ForeignKey(district, default=None, on_delete=models.PROTECT)
    county = models.ForeignKey(county, default=None, on_delete=models.PROTECT)
    subcounty = models.ForeignKey(subcounty, default=None, on_delete=models.PROTECT)
    code = models.CharField(max_length=20, default=None, unique=True)
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
        return concat(concat(self.code, '-'), self.name)


class village(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    region = models.ForeignKey(region, default=None, on_delete=models.PROTECT)
    sub_region = models.ForeignKey(sub_region, default=None, on_delete=models.PROTECT)
    district = models.ForeignKey(district, default=None, on_delete=models.PROTECT)
    county = models.ForeignKey(county, default=None, on_delete=models.PROTECT)
    subcounty = models.ForeignKey(subcounty, default=None, on_delete=models.PROTECT)
    parish = models.ForeignKey(parish, default=None, on_delete=models.PROTECT)
    code = models.CharField(max_length=20, default=None, unique=True)
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return concat(concat(self.code, '-'), self.name)

    class Meta:
        verbose_name_plural = 'Villages'
        verbose_name = 'Village'
