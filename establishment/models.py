import uuid

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext as _

from lookup.models import est_type, max_value_current_year
from organisation.models import organisation
from person.models import person
from location.models import village as vill


def get_next_index():
    try:
        est_index = establishment.objects.count()
        est_index = est_index + 1
    except:
        est_index = 1
    return est_index


class establishment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    est_type = models.ForeignKey(est_type, default=None, on_delete=models.PROTECT)
    person = models.ForeignKey(person, blank=True, null=True, on_delete=models.PROTECT)
    org = models.ForeignKey(organisation, blank=True, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, default=None)
    village = models.ForeignKey(vill, default=None, on_delete=models.PROTECT)
    establishment_number = models.CharField(max_length=20, default=None, unique=True)
    est_size_acres = models.PositiveSmallIntegerField()
    year_est = models.IntegerField(_('year'), validators=[MinValueValidator(1900), max_value_current_year])
    gps_lat = models.DecimalField(max_digits=20, decimal_places=16, default=999.999999)
    gps_long = models.DecimalField(max_digits=20, decimal_places=16, default=999.99999)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        self.establishment_number = get_next_index()
        super().save(**kwargs)

    def __str__(self):
        return self.name
