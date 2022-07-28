from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register_animal, name='register_animal'),
    path('ajax/load-breeds', views.load_breeds, name='ajax_load_breeds'),
    path('ajax/load-colours', views.load_colours, name='ajax_load_colours'),

]
