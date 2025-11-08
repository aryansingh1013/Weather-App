from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    weather=""
    if request.method=="POST":
        city = request.POST.get("city")
        url=f"https://wttr.in/{city}?format=3"
        response=requests.get(url)
        weather=response.text
    return render(request, "index.html",{"weather": weather})