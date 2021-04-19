import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import pandas as pd 
import folium
%matplotlib inline

Indicators = pd.read_csv('/Indicators.csv')


hist_country = 'USA'
mortality_stage = []
mask3 = Indicators['IndicatorCode'].str.contains('SP.DYN.IMRT.IN') 
mask4 = Indicators['CountryCode'].str.contains(hist_country)

mortality_stage = Indicators[mask3 & mask4]
hist_indicator1 = 'GDP per capita \(constant 2005'
hist_country1 = 'USA'

mask1 = Indicators['IndicatorName'].str.contains(hist_indicator1) 
mask2 = Indicators['CountryCode'].str.contains(hist_country1)

gdp_stage1 = Indicators[mask1 & mask2]


hist_year = 2010
mask5 = Indicators['IndicatorCode'].str.contains('SP.DYN.IMRT.IN') 
mask6 = Indicators['Year'].isin([hist_year])

mortality_stage1 = Indicators[mask5 & mask6]

country_geo = 'https://raw.githubusercontent.com/python-visualization/folium/588670cf1e9518f159b0eee02f75185301327342/examples/data/world-countries.json'
map = folium.Map(location=[100, 0], zoom_start=1.5)
folium.Choropleth(geo_data=country_geo, data=plot_data,
             columns=['CountryCode', 'Value'],
             key_on='feature.id',
             fill_color='YlGnBu', fill_opacity=0.7, line_opacity=0.2,
             legend_name=hist_indicator).add_to(map)
