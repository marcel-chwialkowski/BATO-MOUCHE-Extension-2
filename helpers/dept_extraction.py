import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon, mapping
from shapely.ops import unary_union
import json

# Load the complete departments GeoJSON file
gdf = gpd.read_file("france-departments.geojson")

# Define department codes and output file names
departments = {
   #76: "dep75-paris.geojson",
    93: "dep92-hauts-de-seine.geojson",
    94: "dep93-seine-saint-denis.geojson",
    95: "dep94-val-de-marne.geojson"
}

# list of department geojsons shortened
dep_list = []

for code in departments.keys():
    # Filter for the department using the appropriate column name
    dept_gdf = gdf[gdf["cartodb_id"] == code]  # Replace "code" with the actual column name
    dept_gdf = dept_gdf.iloc[0, 5]
    dep_list.append(dept_gdf)

combined = unary_union(dep_list)

# Convert Polygon to GeoJSON using json library
polygon_geojson = json.dumps({
    "type": "Feature",
    "geometry": mapping(combined),
    "properties": {}  # Add any properties here if needed
})

with open('Petite-Couronne-Sans-Paris.geojson', 'w') as f:
    f.write(polygon_geojson)
