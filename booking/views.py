from rest_framework.generics import CreateAPIView

from django.shortcuts import render

from .utils import Request
from . import serializer, models

# Create your views here.
class Booking(CreateAPIView):
    """
    booking post view
    """
    serializer_class = serializer.BookingSerializer
    queryset = models.Book.objects.all()
    
    def post(self, request, *args, **kwargs):
        new_request = Request(request)
        new_request.retrieve_from(request.data)
        return super().post(new_request, *args, **kwargs)


def booking_form(request):
    """
    booking testing form view
    """
    return render(request, "booking_form.html", {})