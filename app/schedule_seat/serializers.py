from rest_framework import serializers

from schedule_seat.models import ScheduleSeat
from seat.serializers import SeatSerializer


class ScheduleSeatSerializer(serializers.ModelSerializer):
    seat = SeatSerializer(read_only=True)

    class Meta:
        model = ScheduleSeat
        fields = ['id', 'seat', 'is_booked', 'schedule_movie']
        read_only_fields = ['id', 'seat', 'schedule_movie']


class ScheduleSeatBookSerializer(serializers.ModelSerializer):
    schedule_seat_ids = serializers.ListField(
        child=serializers.IntegerField()
    )

    class Meta:
        model = ScheduleSeat
        fields = ['schedule_seat_ids']
