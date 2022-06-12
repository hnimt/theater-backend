from rest_framework import serializers

from invoice.models import Invoice
from seat.serializers import SeatSerializer


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'tax', 'total', 'user']


class InvoiceSeatsSerializer(InvoiceSerializer):
    seats = serializers.SerializerMethodField()

    def get_seats(self, obj):
        seats = self.context['seats']
        return SeatSerializer(seats, many=True).data

    class Meta(InvoiceSerializer.Meta):
        fields = InvoiceSerializer.Meta.fields + ['seats']
