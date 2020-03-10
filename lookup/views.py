from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        return render(request, 'home.html',{'zipcode': zipcode})
        api_request = requests.get("http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/"+zipcode+"?apikey=xmqEjgG6W3FFyxkj1vQGC01yhfeLZ0jd%20&details=true")
        try:
            api= json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        
        ################################
        #some sort of description can be put here##
        if api[0]['IconPhrase'] == "Sunny" or "Mostly Sunny" or "Partly Sunny" :
            category_description = "Weather is nice outside go enjoy"
            category_color = "good"
        elif api[0]['IconPhrase'] == "Intermittent Clouds" or "Hazy Sunshine" or "Mostly Cloudy" or "Cloudy":
            category_description = "It might rain carry an umbrella"
            category_color = "cloudy"
        else:
            category_description = "Can't say now "
            category_color = "storm"
        #api.openweathermap.org/data/2.5/weather?q=Delhi,IN&appid=7910769d4aef0928627c083d805cdce2
        return render(request, 'home.html',{
            'api':api,
            'category_description': category_description,
            'category_color': category_color,
        })
    else:
        api_request = requests.get("http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/202396?apikey=xmqEjgG6W3FFyxkj1vQGC01yhfeLZ0jd%20&details=true")
        try:
            api= json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        
        ################################
        #some sort of description can be put here##
        if api[0]['IconPhrase'] == "Sunny" or "Mostly Sunny" or "Partly Sunny" :
            category_description = "Weather is nice outside go enjoy"
            category_color = "good"
        elif api[0]['IconPhrase'] == "Intermittent Clouds" or "Hazy Sunshine" or "Mostly Cloudy" or "Cloudy":
            category_description = "It might rain carry an umbrella"
            category_color = "cloudy"
        else:
            category_description = "Can't say now "
            category_color = "storm"
        #api.openweathermap.org/data/2.5/weather?q=Delhi,IN&appid=7910769d4aef0928627c083d805cdce2
        return render(request, 'home.html',{
            'api':api,
            'category_description': category_description,
            'category_color': category_color,
        })

def about(request):
    return render(request, 'about.html',{})