from celery import shared_task

from invoice.models import Invoice
from schedule_seat.models import ScheduleSeat


@shared_task(bind=True)
def unbook_schedule_seat(self):
    print("Start unbook schedule_seat")
    Invoice.objects.filter(is_pay=False).update(is_canceled=True)
    invoices = Invoice.objects.filter(is_pay=False, is_canceled=True)
    for invoice in invoices:
        invoice.is_canceled = True
        invoice.save()
        ScheduleSeat.objects.filter(invoice=invoice,is_booked=True).update(is_booked=False)
