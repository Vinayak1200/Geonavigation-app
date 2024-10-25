from django.db import models
import geocoder

mapbox_access_token = 'pk.eyJ1IjoidmluYXlhazEyMDAiLCJhIjoiY2xhOXo3YXVnMDJ2azNybzh3ODBpanF3ayJ9.3wPa3e8CFCAuj0lU3ZJv9A'

# Create your models here.
class Reviews(models.Model):
    username = models.CharField(max_length=100, null=True)
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now=True)

    

class WeatherData(models.Model):
    JourneyWeather = models.JSONField()

    #def __str__(self):
    #    return self.JourneyWeather

class Address(models.Model):
    address = models.TextField(null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng
        self.latitude = g[0] 
        self.longitude = g[1]
        return super(Address, self).save(*args, **kwargs)
    
class ContactUs(models.Model):
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    message = models.TextField(null=True)
    
    



