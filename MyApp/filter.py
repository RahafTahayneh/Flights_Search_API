import requests
import json
from MyApp.models import City, Airport, Airline, Flight, Journey

journeys_list = {}


class Flights:
    def __init__(self, flying_from, flying_to, departure_date=None, returning_date=None):
        self.flying_from = flying_from
        self.flying_to = flying_to
        self.departure_date= departure_date
        self.returning_date = returning_date
        print("WELCOME to our Flights")

    def list_journeys(self):
        if City.objects.filter(city_name=self.flying_from).exists():
            origin_city=City.objects.get(city_name=self.flying_from)
            origin_airport = Airport.objects.get(city_id=origin_city.city_id)
            if City.objects.filter(city_name=self.flying_to).exists():
                arrival_city = City.objects.get(city_name=self.flying_to)
                arrival_airport = Airport.objects.get(city_id=arrival_city.city_id)
            else:
                arrival_airport = Airport.objects.get(airport_name=self.flying_to)
            list_of_journys = Journey.objects.filter(origin_airport=origin_airport, arrival_airport=arrival_airport,
                                                     Departure_date_time__startswith=self.departure_date.date()).values()
            if list_of_journys:
                journeys_list = {"The Journeys are" : list(list_of_journys)}
                return journeys_list
            else:
                status = "Failed"
                result_dict = {
                    status: "Bad Request, Hello1"}
                return result_dict
        else:
            origin_airport = Airport.objects.get(airport_name=self.flying_from)
            if City.objects.filter(city_name=self.flying_to).exists():
                arrival_city = City.objects.get(city_name=self.flying_to)
                arrival_airport = Airport.objects.get(city_id=arrival_city.city_id)
            else:
                arrival_airport = Airport.objects.get(airport_name=self.flying_to)
            list_of_journys = Journey.objects.filter(origin_airport=origin_airport, arrival_airport=arrival_airport,
                                                     Departure_date_time__startswith=self.departure_date.date()).values()
            if list_of_journys:
                journeys_list = {"The Journeys are": list(list_of_journys)}
                return journeys_list
            else:
                status = "Failed"
                result_dict = {
                    status: "Bad Request, Hello2"}
                return result_dict

