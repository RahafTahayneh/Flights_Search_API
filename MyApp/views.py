from datetime import datetime

from MySQLdb import DATE
from django.http import JsonResponse
from django.utils.dateformat import DateFormat, TimeFormat
from MyApp.models import City, Airport, Airline, Flight, Journey
from django.core.exceptions import ObjectDoesNotExist
from MyApp.filter import Flights

journeys_list = {}


def get_request(request):
    origin = request.GET.get('Flying_from')
    arrival = request.GET.get('Flying_to')
    departure_date = request.GET.get('Departuring_Date')
    datetime_filter = convert_to_date_format(departure_date)

    flight = Flights(origin, arrival, datetime_filter)
    journeys_list = flight.list_journeys()

    return JsonResponse(journeys_list, safe=False)



   # try:
    #    origin_airport = Airport.objects.get(city_name=origin)
     #   arrival_airport = Airport.objects.get(airport_name=arrival)
      #  list_of_journys = Journey.objects.filter(origin_airport=origin_airport, arrival_airport=arrival_airport, Departure_date_time__startswith=datetime_filter.date())
       # if list_of_journys:
        #    for journey in list_of_journys:
         #       print(journey.flight_code)
           #     print(journey.origin_airport)
            #    print(journey.arrival_airport)
             #   print(journey.Departure_date_time)

    #except ObjectDoesNotExist:
        #return


def convert_to_date_format(departure_date):
    departure_date = departure_date.split("-")
    datetime_filter = datetime(int(departure_date[0]), int(departure_date[1]), int(departure_date[2]))
    return datetime_filter