import uuid
from operator import concat

from django.db import models

# Create your models here.
from lookup.models import sex, animal_type, breed, animal_status, origin, dom_skin_color, ownership_change_type, \
    animal_action_type
from person.models import person
from organisation.models import organisation
from establishment.models import establishment


class animal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sex = models.ForeignKey(sex, default=None, on_delete=models.PROTECT)
    animal_type = models.ForeignKey(animal_type, null=True, blank=True, on_delete=models.PROTECT)
    breed = models.ForeignKey(breed, default=None, on_delete=models.PROTECT)
    dominant_colour = models.ForeignKey(dom_skin_color, default=None, on_delete=models.PROTECT)
    origin = models.ForeignKey(origin, on_delete=models.PROTECT)
    status = models.ForeignKey(animal_status, on_delete=models.PROTECT)
    person = models.ForeignKey(person, null=True, blank=True, on_delete=models.PROTECT)
    org = models.ForeignKey(organisation, null=True, blank=True, on_delete=models.PROTECT)
    est = models.ForeignKey(establishment, default=None, on_delete=models.PROTECT)
    animal_number = models.CharField(max_length=30, default=None)
    name = models.CharField(max_length=100, default=None)
    date_of_birth = models.DateField()
    date_obtained = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    front_photo = models.ImageField(upload_to='animal_photos/front', null=True, blank=True)
    side_photo = models.ImageField(upload_to='animal_photos/side', null=True, blank=True)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.animal_number


class change_of_ownership(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal = models.ForeignKey(animal, default=None, on_delete=models.PROTECT)
    from_person = models.ForeignKey(person, related_name='from_person', default=None, on_delete=models.PROTECT)
    to_person = models.ForeignKey(person, default=None, related_name='to_person', on_delete=models.PROTECT)
    from_org = models.ForeignKey(organisation, related_name='from_org', default=None, on_delete=models.PROTECT)
    to_org = models.ForeignKey(organisation, default=None, related_name='to_org', on_delete=models.PROTECT)
    ownership_change_type = models.ForeignKey(ownership_change_type, default=None, on_delete=models.PROTECT)
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return concat(concat(self.animal.animal_number, self.from_person.person_fullname()),
                      self.to_person.person_fullname())


class animal_action_logbook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal = models.ForeignKey(animal, default=None, on_delete=models.PROTECT)
    animal_action_type = models.ForeignKey(animal_action_type, default=None, on_delete=models.PROTECT)
    action_date = models.DateField()
    active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return concat(self.animal.animal_number, self.animal_action_type.name)
