import matplotlib.pyplot as plt
import pandas as pd
import requests
from PIL import Image
import json
# Enter API key
api_key = 'f70e260a636bad384a68cb089c0c0549'
# Enter the city name and date
city=input("Enter your city where you would like a weather graph for:")
date = input("Enter the date you wish to know the weather in this format 2023-04-24:")
url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
# Make a GET request to the API endpoint
response = requests.get(url)
# Convert the response into a JSON object
data = json.loads(response.text)
# Extract the temperature data for the specified date
temperatures = []
times=[]
for item in data["list"]:
    if item["dt_txt"].startswith(date):
        tempinkelvin = item["main"]["temp"]
        temperature=str(round(tempinkelvin-273))+'C'
        temperatures.append(temperature)
        del temperatures[7:]
        time = item["dt_txt"]
        temperatures.append(temperature)
        times.append(time)
print(times)
# Create the plot
plt.plot(times, temperatures)
plt.xlabel('Date')
plt.ylabel('Temperature(C)')
plt.title('Temperatures in '+ city+' for '+date)
plt.savefig('weathergraph.png')


