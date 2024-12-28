import requests

city_name = input("Enter the city name: ")

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=5803505a150cba8f0b5dbe49c7bdc738'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("The Weather is :", data['weather'][0]['description'])    
    print("The current temperature is : ", data['main']['temp'])
    print("The current temperature looks like : ", data['main']['feels_like'])
    print("The huumidity is : ", data['main']['humidity'])