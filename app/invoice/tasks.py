from celery import shared_task

from invoice.models import Invoice
from schedule_seat.models import ScheduleSeat


@shared_task(bind=True)
def unbook_schedule_seat(self):
    print("Start unbook schedule_seat")
    invoices = Invoice.objects.filter(is_pay=False)
    for invoice in invoices:
        ScheduleSeat.objects.filter(invoice=invoice,is_booked=True).update(is_booked=False)
