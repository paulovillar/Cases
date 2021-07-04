import gmaps
import gmaps.datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point, Polygon
import os

os.getcwd()

gmaps.configure(api_key="AIzaSyDj5GH4CgDqg2qumIftmyIgzO8c_oWdlaA") # Your Google API key

# load a Numpy array of (latitude, longitude) pairs
locations = gmaps.datasets.load_dataset("taxi_rides")

fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations))
fig

