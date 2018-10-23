
from django.contrib import admin
from MyApp import views
from django.conf.urls import url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Flights-Search/', views.get_request)
]
