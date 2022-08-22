from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register_establishment, name='register_establishment'),
    path('ajax/load-district', views.load_district, name='ajax_load_district'),
    path('ajax/load-county',views.load_county, name='ajax_load_county'),
    path('ajax/load-subcounty',views.load_subcounty, name='ajax_subcounty'),
    path('ajax/load-parish', views.load_parish, name='ajax_parish'),
    path('ajax/load-village', views.load_village, name='ajax_load_village'),
]
