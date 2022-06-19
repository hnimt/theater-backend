from django.db import transaction
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import (
    viewsets,
    generics, status
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.response import Response
from core import constants
from invoice.models import Invoice
from invoice.serializers import InvoiceSeatsSerializer
from schedule_seat.exceptions import BookedException
from schedule_seat.models import ScheduleSeat
from schedule_seat.serializers import ScheduleSeatSerializer, ScheduleSeatBookSerializer
from ticket.models import Ticket


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'smi',
                OpenApiTypes.INT,
                description='Schedule Movie ID',
            ),
        ]
    )
)
class ScheduleSeatView(viewsets.ViewSet,
                       generics.ListAPIView,
                       generics.UpdateAPIView):
    queryset = ScheduleSeat.objects.filter(is_deleted=False)
    serializer_class = ScheduleSeatSerializer
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        schedule_seats = self.queryset
        schedule_movie_id = self.request.query_params.get("smi")
        if schedule_movie_id:
            schedule_seats = schedule_seats.filter(schedule_movie__id=schedule_movie_id).order_by('seat__row', 'seat__column')
        return schedule_seats

    def get_serializer_class(self):
        if self.action == 'book':
            return ScheduleSeatBookSerializer

        return self.serializer_class

    def get_permissions(self):
        if self.action == 'book':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @transaction.atomic
    @action(methods=['post'], detail=False, url_path='book')
    def book(self, request):
        ids = request.data['schedule_seat_ids']
        tax = constants.TAX
        schedule_seats = ScheduleSeat.objects.filter(pk__in=ids)
        for ss in schedule_seats:
            if ss.is_booked:
                raise BookedException()

        schedule_seats.update(is_booked=True)
        total = 0
        for schedule_seat in schedule_seats:
            ticket = Ticket.objects.get(type=schedule_seat.seat.type, is_deleted=False)
            total += ticket.price
        total += total * tax
        invoice = Invoice.objects.create(tax=tax, total=total, user=request.user)
        schedule_seats.update(invoice=invoice)
        seats = [schedule_seat.seat for schedule_seat in schedule_seats]
        res = InvoiceSeatsSerializer(invoice, context={'request': request, 'seats': seats}).data

        return Response(res, status=status.HTTP_200_OK)
