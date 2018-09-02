import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=e2b4cbb34ecc98fad8652368366b1898'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    weather_data = []
    cities = City.objects.all()
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city' : city.name,
            'temparature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form': form}
    return render(request, 'weather/weather.html' ,context)
