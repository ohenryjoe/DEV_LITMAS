import uuid

from django.db import models

from animal.models import animal
from lookup.models import incident_type, incident_level


class incident(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal = models.ForeignKey(animal, default=1, on_delete=models.PROTECT)
    incident_type = models.ForeignKey(incident_type, default=1, on_delete=models.PROTECT)
    incident_level = models.ForeignKey(incident_level, default=1, on_delete=models.PROTECT)
    description = models.TextField(default='description')
    reporting_date = models.DateField()
    active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100, default='current_user')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default='current_user')
    updated_timestamp = models.DateTimeField(auto_now=True)


