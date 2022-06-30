import uuid

from django.db import models

# Create your models here.
from location.models import village
from lookup.models import sex, identity_doc_type, title, tribe, nationality, education_level, next_of_kin_type


class person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sex = models.ForeignKey(sex, default=1, on_delete=models.PROTECT)
    village = models.ForeignKey(village, default=1, on_delete=models.PROTECT)
    identity_doc_type = models.ForeignKey(identity_doc_type, default=1, on_delete=models.PROTECT)
    title = models.ForeignKey(title, default=1, on_delete=models.PROTECT)
    tribe = models.ForeignKey(tribe, default=1, on_delete=models.PROTECT)
    nationality = models.ForeignKey(nationality, default=1, on_delete=models.PROTECT)
    educ_level = models.ForeignKey(education_level, default=1, on_delete=models.PROTECT)
    nex_of_kin_type = models.ForeignKey(next_of_kin_type, default=1, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=50, default='')
    other_names = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=50, default='')
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15, default='+256')
    phone2 = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    nok_name = models.CharField(max_length=100, default='')
    nok_phone = models.CharField(max_length=15, default='+256')
    nok_email = models.EmailField(max_length=100, null=True, blank=True)
    photo = models.TextField(null=True, blank=True)
    physical_address = models.CharField(max_length=200, null=True, blank=True)
    identity_doc_number = models.CharField(max_length=50, default='00000000')
    # user = models.ForeignKey(User, )
    disabled = models.BooleanField(default=False)
    is_alive = models.BooleanField(default=True)
    is_married = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100, default='current_user')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default='current_user')
    updated_timestamp = models.DateTimeField(auto_now=True)


class physical_address_log(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(person, default=1, on_delete=models.PROTECT)
    from_address = models.CharField(max_length=200, blank=True, null=True)
    to_address = models.CharField(max_length=200, blank=True, null=True)
    created_by = models.CharField(max_length=100, default='current_user')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default='current_user')
    updated_timestamp = models.DateTimeField(auto_now=True)


class village_log(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(person, default=1, on_delete=models.PROTECT)
    from_village = models.CharField(max_length=200, blank=True, null=True)
    to_village = models.CharField(max_length=200, blank=True, null=True)
    created_by = models.CharField(max_length=100, default='current_user')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default='current_user')
    updated_timestamp = models.DateTimeField(auto_now=True)


class nationality_log(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(person, default=1, on_delete=models.PROTECT)
    from_nationality = models.CharField(max_length=200, blank=True, null=True)
    to_nationality = models.CharField(max_length=200, blank=True, null=True)
    created_by = models.CharField(max_length=100, default='current_user')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default='current_user')
    updated_timestamp = models.DateTimeField(auto_now=True)


class marital_status_log(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(person, default=1, on_delete=models.PROTECT)
    from_is_married = models.CharField(max_length=200, blank=True, null=True)
    to_is_married = models.CharField(max_length=200, blank=True, null=True)
    created_by = models.CharField(max_length=100, default='current_user')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default='current_user')
    updated_timestamp = models.DateTimeField(auto_now=True)
