from django.contrib import admin
from django.views.generic.edit import CreateView
from .models import Reviews, WeatherData, Address, ContactUs


admin.site.register([Reviews, WeatherData, Address, ContactUs])

class AddressView(CreateView):
    model = Address
    fields = ['address']
    template_name = 'api/home.html'
    success_url = '/'
