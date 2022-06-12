from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.paginator import BasePagination
from invoice.models import Invoice
from invoice.serializers import InvoiceSerializer


class InvoiceViewSet(viewsets.ViewSet,
                     generics.ListAPIView):
    serializer_class = InvoiceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = BasePagination
    queryset = Invoice.objects.filter(is_deleted=False)

    def get_queryset(self):
        user = self.request.user
        invoices = self.queryset
        if user:
            return invoices.filter(user=user)

        return invoices
