from MyApp.models import City, Airport, Airline, Flight, Journey

journeys_list = {}


class Flights:
    def __init__(self, flying_from, flying_to, departure_date=None, returning_date=None):
        self.flying_from = flying_from
        self.flying_to = flying_to
        self.departure_date= departure_date
        self.returning_date = returning_date

    # return one way journeys
    def check_and_list_one_way(self):
        flying_list=[self.flying_from,self.flying_to]
        if City.objects.filter(city_name__in=flying_list).exists():
            origin_airport = Airport.objects.filter(city_id=City.objects.get(city_name=self.flying_from).city_id).values('airport_id')
            origin_airport_list = []
            for airport in origin_airport:
                origin_airport_list.append(airport['airport_id'])

            arrival_airport = Airport.objects.filter(city_id=City.objects.get(city_name=self.flying_to).city_id).values('airport_id')
            arrival_airport_list = []
            for airport in arrival_airport:
                arrival_airport_list.append(airport['airport_id'])

            list_of_journeys = Journey.objects.filter(origin_airport__in=origin_airport_list,
                                                     arrival_airport__in=arrival_airport_list,
                                                     Departure_date_time__startswith=self.departure_date.date(),
                                                      journey_type='One Way').values()
            return list(list_of_journeys)

        elif Airport.objects.filter(airport_name__in=flying_list).exists():
            list_of_journeys = Journey.objects.filter(origin_airport=Airport.objects.get(airport_name = self.flying_from), arrival_airport=
                                                    Airport.objects.get(airport_name = self.flying_to),
                                                     Departure_date_time__startswith=self.departure_date.date(),
                                                      journey_type='One Way').values()
            return list(list_of_journeys)

    # return roundtrip journeys
    def check_and_list_roundtrip(self):
        flying_list = [self.flying_from, self.flying_to]
        if City.objects.filter(city_name__in=flying_list).exists():
            origin_airport = Airport.objects.filter(
                city_id=City.objects.get(city_name=self.flying_from).city_id).values('airport_id')
            origin_airport_list = []
            for airport in origin_airport:
                origin_airport_list.append(airport['airport_id'])

            arrival_airport = Airport.objects.filter(
                city_id=City.objects.get(city_name=self.flying_to).city_id).values('airport_id')
            arrival_airport_list = []
            for airport in arrival_airport:
                arrival_airport_list.append(airport['airport_id'])

            list_of_journeys = Journey.objects.filter(origin_airport__in=origin_airport_list,
                                                          arrival_airport__in=arrival_airport_list,
                                                          Departure_date_time__startswith=self.departure_date.date(),
                                                      journey_type='Roundtrip').values()
            return list(list_of_journeys)

        elif Airport.objects.filter(airport_name__in=flying_list).exists():
            list_of_journeys = Journey.objects.filter(
                origin_airport=Airport.objects.get(airport_name=self.flying_from), arrival_airport=
                Airport.objects.get(airport_name=self.flying_to),
                Departure_date_time__startswith=self.departure_date.date(),
                journey_type='Roundtrip').values()
            return list(list_of_journeys)


def check_if_city_exists(city):
    if City.objects.filter(city_name=city).exists():
        return True
    return False









