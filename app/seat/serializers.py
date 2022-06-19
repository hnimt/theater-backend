from rest_framework import serializers

from seat.models import Seat
from ticket.models import Ticket
from ticket.serializers import TicketSerializer


class SeatSerializer(serializers.ModelSerializer):
    ticket = serializers.SerializerMethodField()

    def get_ticket(self, obj):
        ticket = Ticket.objects.filter(type=obj.type).get()
        serializer = TicketSerializer(ticket)
        return serializer.data

    class Meta:
        model = Seat
        fields = ['id', 'row', 'column', 'type', 'room', 'ticket']
