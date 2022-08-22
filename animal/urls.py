from django.urls import path

import animal.views


urlpatterns = [
                  path('animal_listing', animal.views.list_animal, name='list_animal'),
                  path('animal_registration', animal.views.register_animal, name='register_animal'),
                  path('ajax/load-breeds', animal.views.load_breeds, name='ajax_load_breeds'),
                  path('ajax/load-colours', animal.views.load_colours, name='ajax_load_colours'),
                  path('animal_registry', animal.views.registry, name='animal_registry'),
                  path('animal_transfer', animal.views.registry, name='animal_transfer'),
                  path('animal_profile', animal.views.animal_profile, name='animal_profile'),

              ]
