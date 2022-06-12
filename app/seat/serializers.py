from rest_framework import serializers

from seat.models import Seat


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'row', 'column', 'type', 'room']
