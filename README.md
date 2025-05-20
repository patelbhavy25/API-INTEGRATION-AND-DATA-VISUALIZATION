# API-INTEGRATION-AND-DATA-VISUALIZATION

COMPANY : CODTECH IT SOLUTION

NAME : patel bhavy

INTERN ID : CT04DL1286

DOMAIN : PYTHON PROGRAMMING

DURATION : 4 WEEKS

MENTOR : NEELA SANTOSH

## DESCRIPTION OF TASK

## About the Project

This is a small project I built to explore how we can use APIs to fetch real-time data and turn that into something visual and meaningful. I decided to use the OpenWeatherMap API to get the weather forecast of my city, Vadodara, and then plot the temperature changes using Python.

The idea was simple: get the 5-day forecast from the API, extract the temperature data, and visualize it using a line graph. I wanted to keep it minimal, clean, and understandable — both in code and in output.

## How the API is Used

For this project, I used the (OpenWeatherMap's forecast endpoint), which gives weather predictions for every 3 hours over the next 5 days. I used the requests library in Python to make a GET request and added parameters like the city name (Vadodara), API key, and temperature unit (metric for Celsius).

Once I got the response in JSON, I extracted just the parts I needed — the timestamp (dt_txt) and temperature (main['temp']). These are stored in two lists: one for dates and one for corresponding temperatures.

It’s a good exercise if you’re trying to understand how to work with APIs, especially when the data is nested like in this case.

## Data Processing

The data from the API is pretty detailed and comes in 3-hour intervals, so I looped through the forecast list and picked out the values I wanted. There was no major cleaning needed since the API data was already structured well, but formatting the date and choosing what to display on the x-axis took a bit of tweaking to make the graph readable.

## Visualization

For the visualization part, I used Matplotlib and Seaborn. I chose Seaborn’s lineplot because it automatically makes the graphs look a bit nicer without needing too much customization.

I also rotated the x-axis labels because otherwise, they overlapped — a small touch, but it made a big difference. The final plot shows the temperature changes over the next few days, with each point representing a 3-hour forecast.

I saved the graph as forecast.png using plt.savefig() and also displayed it with plt.show().

## Tech Stack

Here’s what I used in this project:

Python
requests (for API calls)
Matplotlib (for plotting)
Seaborn (for better visuals)
OpenWeatherMap API (for real-time data)

## Why I Built This

This project was part of my learning process during my internship, where I was exploring real-world applications of Python, especially in data visualization and working with external APIs. I also wanted to challenge myself to take something raw (like API data) and make it visually meaningful.

It’s a small step, but seeing the temperature trend of your city plotted live is kind of satisfying. It also opens up a lot of ideas — like adding more features, supporting multiple cities, building a web interface, or making a daily weather report bot.

## Future Improvements

There’s definitely room to grow. Some ideas I have:

Add input support so users can choose any city
Show other weather info like humidity, wind, etc.
Use Plotly or Streamlit to make it interactive
Schedule it to run daily and send the image via email or Telegram

# output

![Image](https://github.com/user-attachments/assets/471e0fb1-1c65-47de-8d15-b6fc01e3fe25)
