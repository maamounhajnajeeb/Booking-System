from django.urls import path

from . import views

app_name = "booking"

urlpatterns = [
    # api/v1/booking/
    path("", views.Booking.as_view(), name="add_book"),
    
    # additional endpoint [not an api]
    path("form/", views.booking_form, name="book_form"),
]
