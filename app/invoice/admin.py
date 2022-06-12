from django.contrib import admin

from invoice.models import Invoice


class InvoiceAdmin(admin.ModelAdmin):
    class Meta:
        model = Invoice

    readonly_fields = ['id', 'user', 'tax', 'total']


admin.site.register(Invoice, InvoiceAdmin)
