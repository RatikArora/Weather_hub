from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
import os,requests
from django.shortcuts import render
import requests

def home(request):
    if request.method == "POST":
        city = request.POST.get('city')

        # Define the API URL with placeholders for the city and API key
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=750622e830114674a414bf9d2692c90b'

        # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
        api_key = '750622e830114674a414bf9d2692c90b'

        # Make the API request
        response = requests.get(url.format(city, api_key))

        if response.status_code == 200:
            # Parse the JSON response to extract weather data
            city_weather = response.json()

            weather = {
                'city': city,
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon'],
                'humidity' : city_weather['main']['humidity'],
                'wind_speed' : city_weather['wind']['speed'],
                
                    }
            print(weather)
        else:
            print("Failed to retrieve weather data. Status code:", response.status_code)
            weather = None

        return render(request, 'a.html', {'weather': weather})

    return render(request, 'a.html')
