from rest_framework import serializers

from . import models

class BookingSerializer(serializers.ModelSerializer):
    """
    booking post serializer
    """
    class Meta:
        model = models.Book
        fields = (
            "id", "user", "destination", "person_age", "depart_time", "return_time",
        )
