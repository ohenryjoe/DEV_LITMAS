from django.contrib import admin

from animal.models import animal
from lookup.admin import est_typeAdmin


class animalAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(animalAdmin, self).get_form(request, obj, **kwargs)
        return form


admin.site.register(animal, animalAdmin)
