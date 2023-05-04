import folium
import pandas as pd
import geopandas as gpd
from matplotlib import colormaps
from matplotlib.colors import ListedColormap


def folium_grid_cat_plot(gdf, var : str, cmap = 'Set1', 
coordinates =(48.8534100,2.3488000),zoom_start=12.1, discrete = False, op = 0.6):
    if discrete:
        colors = colormaps[cmap](range(len(gdf[var].unique())))
        colors = ListedColormap(colors)
        m = folium.Map(coordinates, zoom_start = zoom_start)
        m = gdf.explore(
            m = m,
            column = var,
            tooltip = var,
            tiles = 'OpenStreetMap',
            popup = True,
            cmap = colors,
            categorical = True,
            style_kwds = dict(color = "black", opacity = op,
            fillOpacity = 0.4)
        )
    else:
        m = folium.Map(coordinates, zoom_start = zoom_start)
        m = gdf.explore(
            m = m,
            column = var,
            tooltip = var,
            tiles = 'OpenStreetMap',
            popup = True,
            cmap = cmap,
            style_kwds = dict(color = "black", opacity = op,
            fillOpacity = 0.4)
        )


    return m