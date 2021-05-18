from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    # on Flight list page, display the following fields in a tabular layout
    # see http://127.0.0.1:8000/admin/flights/flight/
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    # on Passenger detail page, use a horizontal layout to select/deselect Flights 
    # see http://127.0.0.1:8000/admin/flights/passenger/<passenger_id>
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
