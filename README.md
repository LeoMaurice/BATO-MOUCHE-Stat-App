# BATO-MOUCHE/Composition of big cities

## Description

Project on analysing OSM data. Supervised by Paula Tubora and Sarah J. Berkemer.

### Progress

- [ ] Datascrapping
  - [ ] Choice of OSM tags and creation of variables of interests
  - [ ] Creation of "ethnic food" variables ?
  - [ ] Choice of INSEE's variables
- [ ] First analysis
  - [X] Restaurants accessibility, Gini inequality
  - [ ] see this [blog](https://geographicdata.science/book/notebooks/09_spatial_inequality.html) for more ideas
# Data

## INSEE socio-economic data : 
- [Filosofi](https://www.insee.fr/fr/statistiques/4176290?sommaire=4176305#consulter)
- [SIRENE API](https://api.insee.fr/catalogue/site/themes/wso2/subthemes/insee/pages/item-info.jag?name=Sirene&version=V3&provider=insee) to get data for registered company in France and their locations

## OpenStreetMap scrapping

There are multiple ways to get OSM data :

- use the OSMnx library : really complete and easy to use
  - near_eiffel_tower notebook explores OSMnx possibilities
  - Uses Overpass API but simplier
  - It is what we chosen

- using Geofabrick : download and zip already .shp formats : great to use with geopandas
  - See the second part of near_eiffel_tower notebook
  - default : only a selection of towns/regions/countries : enough at least to starts with
  - advantage : files come in OSM data but also in .shp files : easier to open in geopandas
  - See the files : 
[Europe](https://osm-internal.download.geofabrik.de/europe.html),
[IdF](https://download.geofabrik.de/europe/france/ile-de-france.html),
  - [see documentation](https://download.geofabrik.de/osm-data-in-gis-formats-free.pdf)

- using OSM datafiles (.osm = op-to-data, .osh = history) with osmium python library. .osm.pbf = contains every OSM elements versions through time.
  - see the example-code folder
  - main default : not easy extraction even with osmium

The OSM files can be dowload through different ways :

- through the [OSM API](https://www.openstreetmap.org/export) : limited, for instance we can't d.ownload the whole Paris (seems logical)
- through API Overpass : mirror data from OSM, without the limitation. Hard to use : encapsulated in OSMnx.
- through Planet OSM : regular copies.
- through [Geofabrik](https://www.geofabrik.de) : regular copies but only a selection of towns/regions/countries. (Geofabrik already suppress user data but the rest of the metadata are the same). Copies diponible in .osm and .shp.
- through [Ohsome](https://hex.ohsome.org/) : for historical data analysis. Comes with an API and a python library.

# Ressources

## Tutorials and Inspirations

[OSM parser with python](https://oslandia.com/en/2017/07/03/openstreetmap-data-analysis-how-to-parse-the-data-with-python/)

[Urban walkabity using OSMnx](https://gispofinland.medium.com/analysing-urban-walkability-using-openstreetmap-and-python-33815d045204)

[Course on OSMnx by G. Boeing (created OSMnx)](https://github.com/LeoMaurice/osmnx-examples)

[Sergio J. Rey, Dani Arribas-Bel, Levi J. Wolf's book on Geographic Data Science with Python](https://geographicdata.science/book/intro.html)

See also :

- [Online version of the book “Introduction to Python for Geographic Data Analysis” by Henrikki Tenkanen, Vuokko Heikinheimo & David Whipp](https://pythongis.org/)


## OSMwiki

- [tags (map features)](https://wiki.openstreetmap.org/wiki/Map_features) for nodes on the map
- [projection](https://wiki.openstreetmap.org/wiki/Projection) of geographic coordinates : OMS is in WGS-84 (EPSG:4326, usual GPS projection)

# Bibliography

## Blog

Ltd, Gispo. « [Analysing urban walkability using OpenStreetMap and Python](https://gispofinland.medium.com/analysing-urban-walkability-using-openstreetmap-and-python-33815d045204) ». Medium (blog), 22 février 2022.

## INSEE

[Commerces de proximité par l'INSEE](https://www.insee.fr/fr/statistiques/4986837?sommaire=4987235)

## Scientific articles

Berkemer, Sarah J., et Peter F. Stadler. « Street Name Data as a Reflection of Migration and Settlement History ». Urban Science 4, nᵒ 4 (11 décembre 2020): 74. [doi.org/10.3390/urbansci4040074](https://doi.org/10.3390/urbansci4040074).

Boeing, Goeff. « OSMnx: New Methods for Acquiring, Constructing, Analyzing, and Visualizing Complex Street Networks | Elsevier Enhanced Reader ». Consulté le 12 novembre 2022. [https://doi.org/10.1016/j.compenvurbsys.2017.05.004](https://doi.org/10.1016/j.compenvurbsys.2017.05.004).

Knap, Elizabeth, Mehmet Baran Ulak, Karst T. Geurs, Alex Mulders, et Sander van der Drift. « A Composite X-Minute City Cycling Accessibility Metric and Its Role in Assessing Spatial and Socioeconomic Inequalities – A Case Study in Utrecht, the Netherlands ». Journal of Urban Mobility 3 (1 décembre 2023): 100043. [https://doi.org/10.1016/j.urbmob.2022.100043](https://doi.org/10.1016/j.urbmob.2022.100043).

Girres, Jean-François, et Guillaume Touya. « Quality Assessment of the French OpenStreetMap Dataset ». Transactions in GIS 14, no 4 (2010): 435‑59. [https://doi.org/10.1111/j.1467-9671.2010.01203.x](https://doi.org/10.1111/j.1467-9671.2010.01203.x).

PySAL: A Python Library of Spatial Analytical Methods, Rey, S.J. and L. Anselin, Review of Regional Studies 37, 5-27 2007.

# Python packages and tools

## Geographic/spatial packages

### [Geopandas](https://geopandas.org/en/stable/) obviously

### [PySal](https://pysal.org/) and in particular [PySal.lib](https://pysal.org/libpysal/)

An excellent tool with a lot of different spatial statistics functions implemented !

### [NetworkX](https://networkx.org/)

### [r5py](https://r5py.readthedocs.io/en/stable/notebooks/basic-usage.html#introduction) for transport time calculations

### Cartiflette: for working with french geographic data sets

[Cartiflette, git repo](https://github.com/InseeFrLab/cartiflette)
and examples from the [ENSAE data science class](https://pythonds.linogaliana.fr/geopandas/)

## OpenStreetMap directly related to :

### osmium: tool to parse osm files with python bindings pyosmium

[osmium website](https://osmcode.org/osmium-tool/), [documentation](https://osmcode.org/osmium-tool/manual.html)

### OSMnx: a library that can be used to extract data easily both graph and POI data

[OSMnx git repo](https://github.com/gboeing/osmnx)
and the [Associated examples](https://github.com/LeoMaurice/osmnx-examples)

OSMnx is developped by G. Boeing from USC. It uses the Overpass API but largely encapsulated to gather OSM data. OSMnx also incopores algorithms to simply/make more realistic networks from the OSM graphs and to analyses the network itself.

For now, OSMnx is probably the best way to access OSM data.

### Ohsome : another library by Heildelberg university for historical data

can be found on [on the git repo for ohsom-py](https://github.com/GIScience/ohsome-py), created by [Heidelberg Institute for Geoinformation Technology](https://heigit.org/big-spatial-data-analytics-en/)

Ohsome-py is a python-based encapsulation of an API named Ohsom by the HeiGIT which allows to access their database to explore historical (meaning the evolution of volontary contribution to OSM). It is closer to the response libary. The API is really oriented tower the evolution of OSM data and so less usefull than OSMnx for graph and POI analysis.

The graphic access through the [OhsomeHEx website](https://hex.ohsome.org/) is really well made and usefull to see for instance where there are enough data.



