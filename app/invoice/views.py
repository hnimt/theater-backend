from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.paginator import MyPagination
from invoice.models import Invoice
from invoice.serializers import InvoiceSerializer, InvoiceUserSerializer


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
        invoices = self.queryset.filter(user=self.request.user)\
            .order_by('-created_at')
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
