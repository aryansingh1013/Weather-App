import requests

def getWheather(city):
    url=f"https://wttr.in/{city}?format=3"
    
    response=requests.get(url)

    return response.text

if __name__=="__main__":
    print("===Simple Weather App===")
    city=input("Enter city name: ")
    print(getWheather(city))