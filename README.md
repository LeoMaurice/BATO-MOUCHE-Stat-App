# BATO-MOUCHE/Composition of big cities

## Description

Project on analysing OSM data. Supervised by Paula Tramora and Sarah J. Berkemer.

### Progress

- [ ] Datascrapping
  - [ ] Approfondir à partir de wiki la compréhension des tags
  - [ ] Use the simplify fct of OSMnx
  - [ ] Filter user personnal data
- [ ] First analysis
  - [ ] Faire attention que les calculs sont des projections de GPS : biais
    - Quelles types d'analyse sont effectuables :
      - textuelle sur le nom des POI et des rues ?
      - auto corrélation spatiale ? sur quelle catégorie ?
      - faut t il faire des analyses sur les groupes de restaurants ?
    - Importer d'autres types de données ? :velib, transports en commun, traffic ? opendata de la RATP ?

## Data scrapping

There are multiple ways to get OSM data :

- use the OSMnx library : really complete and easy to use
  - Maybe too many ? Compare to geofabrik ?
  - See the first part of near_eiffel_tower notebook

- using Geofabrick : download and zip already .shp formats : great to use with geopandas
  - See the second part of near_eiffel_tower notebook
  - default : only a selection of towns/regions/countries : enough at least to starts with
  - advantage : files come in OSM data but also in .shp files : easier to open in geopandas

- using OSM datafiles (.osm = op-to-data, .osh = history) with osmium python library. .osm.pbf = contains every OSM elements versions through time.

  - see the example-code folder
  - main default : not easy extraction even with osmium

The OSM files can be dowload through different ways :

- through the [OSM API](https://www.openstreetmap.org/export) : limited, for instance we can't d.ownload the whole Paris (seems logical)
- through API Overpass : mirror data from OSM, without the limitation. Hard to use : encapsulated in OSMnx.
- through Planet OSM : regular copies.
- through [Geofabrik](https://www.geofabrik.de) : regular copies but only a selection of towns/regions/countries. (Geofabrik already suppress user data but the rest of the metadata are the same). Copies diponible in .osm and .shp.
- through [Ohsome](https://hex.ohsome.org/) : for historical data analysis. Comes with an API and a python library.

## Link collection for websites and data that might be useful for the project

### Examples and inspirations

[OSM parser with python](https://oslandia.com/en/2017/07/03/openstreetmap-data-analysis-how-to-parse-the-data-with-python/)

[Urban walkabity using OSMnx](https://gispofinland.medium.com/analysing-urban-walkability-using-openstreetmap-and-python-33815d045204)

[Course on OSMnx by G. Boeing (created OSMnx)](https://github.com/LeoMaurice/osmnx-examples)

### Database

#### Geofabrik: download small chunks of osm mapping data and history files

[Europe](https://osm-internal.download.geofabrik.de/europe.html),
[IdF](https://download.geofabrik.de/europe/france/ile-de-france.html)
[see documentation](https://download.geofabrik.de/osm-data-in-gis-formats-free.pdf)

#### [SIRENE API](https://api.insee.fr/catalogue/site/themes/wso2/subthemes/insee/pages/item-info.jag?name=Sirene&version=V3&provider=insee) to get data for registered company in France and their locations

### Python packages and tools

#### osmium: tool to parse osm files with python bindings pyosmium

[osmium website](https://osmcode.org/osmium-tool/), [documentation](https://osmcode.org/osmium-tool/manual.html)

#### OSMnx: a library that can be used to extract data easily both graph and POI data

[OSMnx git repo](https://github.com/gboeing/osmnx)
and the [Associated examples](https://github.com/LeoMaurice/osmnx-examples)

OSMnx is developped by G. Boeing from USC. It uses the Overpass API but largely encapsulated to gather OSM data. OSMnx also incopores algorithms to simply/make more realistic networks from the OSM graphs and to analyses the network itself.

For now, OSMnx is probably the best way to access OSM data.

#### Ohsome : another library by Heildelberg university for historical data

can be found on [on the git repo for ohsom-py](https://github.com/GIScience/ohsome-py), created by [Heidelberg Institute for Geoinformation Technology](https://heigit.org/big-spatial-data-analytics-en/)

Ohsome-py is a python-based encapsulation of an API named Ohsom by the HeiGIT which allows to access their database to explore historical (meaning the evolution of volontary contribution to OSM). It is closer to the response libary. The API is really oriented tower the evolution of OSM data and so less usefull than OSMnx for graph and POI analysis.

The graphic access through the [OhsomeHEx website](https://hex.ohsome.org/) is really well made and usefull to see for instance where there are enough data.

#### Cartiflette: for working with french geographic data sets

[Cartiflette, git repo](https://github.com/InseeFrLab/cartiflette)
and examples from the [ENSAE data science class](https://pythonds.linogaliana.fr/geopandas/)

### Ressources

#### OSMwiki

- [tags (map features)](https://wiki.openstreetmap.org/wiki/Map_features) for nodes on the map
- [projection](https://wiki.openstreetmap.org/wiki/Projection) of geographic coordinates : OMS is in WGS-84 (EPSG:4326, usual GPS projection)

## Bibliography

### Blog

Ltd, Gispo. « [Analysing urban walkability using OpenStreetMap and Python](https://gispofinland.medium.com/analysing-urban-walkability-using-openstreetmap-and-python-33815d045204) ». Medium (blog), 22 février 2022.

### Scientific articles

#### By the supervisors

Berkemer, Sarah J., et Peter F. Stadler. « Street Name Data as a Reflection of Migration and Settlement History ». Urban Science 4, nᵒ 4 (11 décembre 2020): 74. [doi.org/10.3390/urbansci4040074](https://doi.org/10.3390/urbansci4040074).

#### USC/G. Boeing

« OSMnx: New Methods for Acquiring, Constructing, Analyzing, and Visualizing Complex Street Networks | Elsevier Enhanced Reader ». Consulté le 12 novembre 2022. [doi.org/10.1016/j.compenvurbsys.2017.05.004](https://doi.org/10.1016/j.compenvurbsys.2017.05.004).
