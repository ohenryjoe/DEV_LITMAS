import uuid

from django.db import models

# Create your models here.
from lookup.models import sex, animal_type, breed, status, origin, dominant_color
from person.models import person
from organisation.models import organisation
from establishment.models import establishment


class animal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sex = models.ForeignKey(sex, default=1, on_delete=models.PROTECT)
    animal_type = models.ForeignKey(animal_type, default=1, on_delete=models.PROTECT)
    breed = models.ForeignKey(breed, default=1, on_delete=models.PROTECT)
    dominant_colour = models.ForeignKey(dominant_color, default=1, on_delete=models.PROTECT)
    origin = models.ForeignKey(origin, default=1, on_delete=models.PROTECT)
    status = models.ForeignKey(status, default=1, on_delete=models.PROTECT)
    person = models.ForeignKey(person, default=1, on_delete=models.PROTECT)
    org = models.ForeignKey(organisation, default=1, on_delete=models.PROTECT)
    est = models.ForeignKey(establishment, default=1, on_delete=models.PROTECT)
    animal_number = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=30, default='XXX')
    date_of_birth = models.DateField()
    date_obtained = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    front_photo = models.ImageField(upload_to='animal_photos/front', null=True, blank=True)
    side_photo = models.ImageField(upload_to='animal_photos/front', null=True, blank=True)
    active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100, default='current_user')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default='current_user')
    updated_timestamp = models.DateTimeField(auto_now=True)

