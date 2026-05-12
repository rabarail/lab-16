"""The program's name,
author: Rajani Baraili
The purpose of the program: Reads the world_fires_1_day.csv file that contains one day of
                global fire detection data from NASA FIRMS, and plots each
                fire's latitude and longitude on an interactive world map using
                plotly express.
Any info about starter code (If used, where it came from, link, etc.), and the: none
Date5/11/2026 """

 
import plotly.express as ex
import csv 

latitudes = []
longitudes = []
brightnesses = []
dates        = []

with open ("world_fires_1_day.csv") as csvfile:
    reader = csv.reader(csvfile)

    for index, row in enumerate(reader):
        if index == 0:
            continue 

        try:
            latitude = float(row[0])
            latitudes.append(latitude) 
            longitude = float(row[1])
            longitudes.append(longitude)
            brightness = float(row[2])
            brightnesses.append(brightness)
            date = row[5]
            dates.append(date)
        except ValueError:
            print(f"Warning- Skipping row {index} due to invalid data.")
        

figure = ex.scatter_geo(
    lat=latitudes,
    lon=longitudes,
    color=brightnesses,
    hover_name=dates,
    title="Global Fire Detection",
    projection= "orthographic",
    color_continuous_scale="YlOrRd",
)

