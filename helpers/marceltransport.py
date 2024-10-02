import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt
import folium
import pandas as pd
import urllib3
from zipfile import ZipFile
import requests
import osmnx as ox
import geopy.distance
import networkx as nx
from selenium import webdriver
from matplotlib import colormaps
from matplotlib.colors import ListedColormap
import time
import os

"""
this file is in essence very similar to what yubo did, i will just exclude the stuff that i find useless.
it will be easier for me to wrap my head around it.
"""

def calculate_straight_line_distance(point1, point2):
    """Calculate the straight line distance between two points in kilometers."""
    distance = geopy.distance.distance(point1, point2).m
    return distance
