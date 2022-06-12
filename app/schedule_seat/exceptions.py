from rest_framework.exceptions import APIException


class BookedException(APIException):
    status_code = 400
    default_detail = 'These seats are booked.'
    default_code = 'book_unavailable'