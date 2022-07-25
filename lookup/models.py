import datetime
import uuid

from django.core.validators import MaxValueValidator
from django.db import models


# Year fields


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year + 1)]


# Person Lookups

class org_type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Organization Types'
        verbose_name = 'Organization Type'

    def __str__(self):
        return self.name


class sex(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Sex'
        verbose_name = 'Sex'

    def __str__(self):
        return self.name


class identity_doc_type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Identity Document Types'
        verbose_name = 'Identity Document type'


class title(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Titles'
        verbose_name = 'Title'


class tribe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Person Tribes'
        verbose_name = 'Person Tribe'


class nationality(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Person Nationalities'
        verbose_name = 'Person Nationality'


class education_level(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Person Education Levels'
        verbose_name = 'Person Education Level'


class next_of_kin_type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Next Of Kin'
        verbose_name = 'Next of Kin'

    # Animal Lookup


class animal_type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Animal Types'
        verbose_name = 'Animal Type'


class ownership_change_type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Ownership Change Types'
        verbose_name = 'Ownership Change Type'


class animal_action_type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Animal Action Types'
        verbose_name = 'Animal Action Type'


class breed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal_type = models.ForeignKey(animal_type, db_constraint=False, default=None, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Animal Breeds'
        verbose_name = 'Animal Breed'


class dom_skin_color(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal_type = models.ForeignKey(animal_type, on_delete=models.PROTECT)
    breed = models.ForeignKey(breed, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Animal Dominant Colours'
        verbose_name = 'Animal Dominant Colour'


class origin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Origins'
        verbose_name = 'animal_origin'


class animal_status(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Animal Statuses'
        verbose_name = 'Animal Status'


# Establishment
class est_type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Establishment Types'
        verbose_name = 'Establishment Type'


# device lookups
class tag_status(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tag Statuses'
        verbose_name = 'Tag Status'


# Incident Lookups
class incident_type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Incident Types'
        verbose_name = 'Incident Type'


class incident_priority_level(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    colour_code = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Incident Levels'
        verbose_name = 'Incident Level'


# TagInstaller
class operation_status(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Operation Statuses'
        verbose_name = 'Operation Status'

    # Animal Transfer Purpose


class transfer_purpose(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Transfer Purposes'
        verbose_name = 'Transfer Purpose'


class transit_category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Transit Categories'
        verbose_name = 'Transit Category'


class movement_type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Movement Types'
        verbose_name = 'Movement Type'


class transfer_status(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Transfer Statuses'
        verbose_name = 'Transfer Status'


# Vehicle

class vehicle_make(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Vehicle Makes'
        verbose_name = 'Vehicle Models'


class vehicle_model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Vehicle Models'
        verbose_name = 'Vehicle Model'


class transfer_fee_type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Transfer Fee Types'
        verbose_name = 'Transfer Fee Type'


class payment_mode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Payment Modes'
        verbose_name = 'Payment Mode'


class payment_channel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Payment Channels'
        verbose_name = 'Payment Channel'


# Quarantine Reason/Status

class quarantine_reason(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Quarantine Reasons'
        verbose_name = 'Quarantine Reason'


class quarantine_status(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Quarantine Statuses'
        verbose_name = 'Quarantine Status'


class role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Role'
        verbose_name = 'Roles'


class transfer_action_type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Transfer Action Types'
        verbose_name = 'Transfer Action Type'


class mode_of_transport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Transport Modes'
        verbose_name = 'Transport Mode'


# Market Lookup
class market_type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Market Types'
        verbose_name = 'Market Type'
