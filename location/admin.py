from django.contrib import admin
from .models import *

admin.site.register(district)
admin.site.register(region)
admin.site.register(sub_region)
admin.site.register(county)
admin.site.register(subcounty)
admin.site.register(parish)
admin.site.register(village)

# Register your models here.
