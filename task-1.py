import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = 'bb2aa63eb2514106fd542c7e15b2dec9'
city = 'vadodara'

url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

dates = []
temps = []

for entry in data['list']:
    dates.append(entry['dt_txt'])
    temps.append(entry['main']['temp'])

plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temps)
plt.xticks(rotation=45)
plt.title(f'Temperature Forecast for {city} (°C)')
plt.xlabel("Date and Time")
plt.ylabel("Temperature (°C)")
import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = 'bb2aa63eb2514106fd542c7e15b2dec9'
city = 'vadodara'

url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

dates = []
temps = []

for entry in data['list']:
    dates.append(entry['dt_txt'])
    temps.append(entry['main']['temp'])

plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temps)
plt.xticks(rotation=45)
plt.title(f'Temperature Forecast for {city} (°C)')
plt.xlabel("Date and Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.savefig("forecast.png")  # Optional: saves the file
plt.show()                   # Shows the graph window

