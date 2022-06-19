from rest_framework import serializers

from invoice.models import Invoice
from movie.serializers import MovieSerializer
from seat.serializers import SeatSerializer
from show_date.serializers import ShowDateSerializer
from show_time.serializers import ShowTimeSerializer


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


class InvoiceUserSerializer(serializers.Serializer):
    """Serializer for user's invoices"""
    invoice = InvoiceSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    show_date = ShowDateSerializer(read_only=True)
    show_time = ShowTimeSerializer(read_only=True)
