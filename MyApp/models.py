from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=128)

    def __str__(self):
        return self.city_name


@python_2_unicode_compatible
class Airport(models.Model):
    airport_id = models.IntegerField(primary_key=True)
    airport_name = models.CharField(max_length=128)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.airport_name


@python_2_unicode_compatible
class Airline(models.Model):
    airline_code = models.CharField(max_length=128,primary_key=True)
    airline_name = models.CharField(max_length=128)


    def __str__(self):
        return self.airline_name


@python_2_unicode_compatible
class Flight(models.Model):
    flight_code = models.CharField(max_length=100,primary_key=True)
    airline_code = models.ForeignKey(Airline,on_delete=models.CASCADE)
    passenger_capacity = models.IntegerField()

    def __str__(self):
        return self.flight_code


@python_2_unicode_compatible
class Journey(models.Model):
    flight_code = models.ForeignKey(Flight, on_delete=models.CASCADE)
    origin_airport = models.ForeignKey(Airport, related_name='TheOriginAirport', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(Airport, related_name='TheArrivalAirport', on_delete=models.CASCADE)
    Departure_date_time = models.DateTimeField()
    Arrival_date_time = models.DateTimeField()
    price=  models.CharField(max_length=128)

    def __str__(self):
        return self.flight_code



