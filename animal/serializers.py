from rest_framework import serializers
from animal.models import animal as animal_model


class AnimalSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = animal_model
        fields = (
            'id',
            'sex',
            'animal_type',
            'breed',
            'dominant_colour',
            'origin',
            'status',
            'person',
            'org',
            'est',
            'name',
            'date_of_birth',
            'date_obtained',
            'date_of_death',
            'description',
            'front_photo',
            'side_photo',
            'active',
        )
