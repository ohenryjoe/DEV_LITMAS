import uuid
from decimal import Decimal
import datetime
from django.core.validators import MinValueValidator
from django.db import models

from location.models import village
from lookup.models import est_type, max_value_current_year
from organisation.models import organisation
from person.models import person
from django.utils.translation import gettext as _


class establishment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    est_type = models.ForeignKey(est_type, default=1, on_delete=models.PROTECT)
    person = models.ForeignKey(person, default=1, on_delete=models.PROTECT)
    org = models.ForeignKey(organisation, default=1, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, default='')
    est_size_acres = models.PositiveSmallIntegerField()
    year_est = models.IntegerField(_('year'), validators=[MinValueValidator(1900), max_value_current_year])
    gps_lat = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    gps_long = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)


