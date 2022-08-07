from time import sleep

from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist

from invoice.models import Invoice
from schedule_seat.models import ScheduleSeat


@shared_task()
def unbook_schedule_seat(invoice_id):
    sleep(60)
    try:
        invoice = Invoice.objects.get(pk=invoice_id,is_pay=False)
        invoice.is_canceled = True
        invoice.save()
        ScheduleSeat.objects.filter(invoice=invoice, is_booked=True).update(is_booked=False)
    except ObjectDoesNotExist:
        pass
