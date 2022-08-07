from rest_framework import serializers

from invoice.models import Invoice
from movie.serializers import MovieSerializer
from seat.serializers import SeatSerializer
from show_date.serializers import ShowDateSerializer
from show_time.serializers import ShowTimeSerializer
from django.utils.translation import gettext_lazy as _


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'tax', 'total', 'user', 'is_deleted', 'is_pay', 'is_canceled']
        read_only_fields = ('id', 'tax', 'total', 'user', 'is_pay')

    def update(self, instance, validated_data):
        user = self.context['request'].user
        schedule_seats = instance.schedule_seats.all()
        for ss in schedule_seats:
            ss.is_booked = False
            ss.save()
        if instance.user == user:
            return super().update(instance, validated_data)
        raise serializers.ValidationError(_("Not permission to update invoice."))


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
