# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:42:56 2020

@author: Shihab
"""

import pandas as pd
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature


"""
importing both csv files "airport.csv" "otselennud.csv" 
from "otselennud.csv" - imported with ";" separated to removed the City colum
"""
all_airport_data = pd.read_csv("airport.csv")
# using "sep=';'" to get the columns correctly
direct_flight = pd.read_csv("otselennud.csv", sep=';') 

# Merging both CSV files based on IATA   
merged = direct_flight.merge(all_airport_data, left_on='IATA', right_on='IATA', how='left')
print(merged)
merged.to_csv('merged.csv')

#declaring tallin's coordinates
origin_lat = 59.41329956 
origin_lon= 24.83279991

"""
importing "merged.csv" row in data, skipping the first row which contains coordinate of Tallinn 

"""
data = pd.read_csv("merged.csv", skiprows=[1])



#here map is being created using cartopy

fig = plt.figure(figsize=(5*4,5*4))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.LambertCylindrical())
ax.set_extent([-20, 50,70, 30], crs=ccrs.PlateCarree())
ax.stock_img()
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.BORDERS, linestyle=':')


plt.title('Direct flights from Tallinn')

# adding TLL label to point out tallinn airport
plt.text(origin_lon, origin_lat, 'TLL',
         horizontalalignment='right',
         transform=ccrs.Geodetic())
"""
below for loop plotting the destination routes from tallinn and labeling the destination based longititude and latidude.
labels are taken from IATA column
"""
for i in range(len(data)):
    lon = data['Longitude'][i]
    lat =  data['Latitude'][i]
    label = data['IATA'][i]

    plt.plot([origin_lon, lon], [origin_lat, lat],
         color='red', linewidth=1,marker='o',
         transform=ccrs.Geodetic(),
         )
    
    plt.text(lon, lat, label,
     horizontalalignment='right',
     transform=ccrs.Geodetic())

#Saving the flight map in .png format
plt.savefig('flights.png',dpi=100)
#displaying to flight map
plt.show()






