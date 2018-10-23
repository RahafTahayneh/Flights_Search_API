from datetime import datetime
from django.http import JsonResponse
from MyApp.filter import Flights

journeys_list = {}


def get_request(request):
    origin = request.GET.get('flying_from')
    arrival = request.GET.get('flying_to')
    departure_date = request.GET.get('departuring_date')
    datetime_filter_departure = convert_to_date_format(departure_date)

    if request.GET.get('returning_date'):
        returning_date = request.GET.get('returning_date')
        datetime_filter_returning = convert_to_date_format(returning_date)
        flight = Flights(origin, arrival, datetime_filter_departure, datetime_filter_returning )
        journeys_list = flight.check_and_list_roundtrip()

    else:
        flight = Flights(origin, arrival, datetime_filter_departure)
        journeys_list = flight.check_and_list_one_way()

    return JsonResponse(journeys_list, safe=False)


def convert_to_date_format(departure_date):
    departure_date = departure_date.split("-")
    datetime_filter = datetime(int(departure_date[0]), int(departure_date[1]), int(departure_date[2]))
    return datetime_filter
