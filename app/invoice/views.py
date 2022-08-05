from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.paginator import MyPagination
from invoice.models import Invoice
from invoice.serializers import InvoiceSerializer, InvoiceUserSerializer

@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'is_pay',
                OpenApiTypes.STR,
                description='Is payed',
            ),
        ]
    )
)
class InvoiceViewSet(viewsets.ViewSet,
                     generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset =  Invoice.objects.filter(is_deleted=False)
    serializer_class = InvoiceSerializer
    pagination_class = MyPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return InvoiceUserSerializer

        return self.serializer_class

    def list(self, request):
        filtered_invoices = self.queryset
        is_canceled = request.query_params.get('is_canceled')
        if is_canceled and is_canceled != "":
            filtered_invoices = filtered_invoices.filter(is_canceled=is_canceled)

        invoices = (
            filtered_invoices.filter(user=self.request.user)
            .order_by('-created_at')
        )
        res = []

        for invoice in invoices:
            schedule_seats = invoice.schedule_seats.all()
            if len(schedule_seats) > 0:
                schedule_movie = schedule_seats.all()[0].schedule_movie
                movie = schedule_movie.movie
                show_date = schedule_movie.show_date
                show_time = schedule_movie.show_time

                res.append({
                    'invoice': invoice,
                    'movie': movie,
                    'show_date': show_date,
                    'show_time': show_time,
                })
            else:
                pass

        qs = self.paginator.paginate_queryset(res, request)
        serializer = self.get_serializer(qs, many=True)
        return self.paginator.get_paginated_response(serializer.data)


class UpdateInvoiceViewSet(viewsets.ViewSet,
                           generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Invoice.objects.filter(is_deleted=False)
    serializer_class = InvoiceSerializer