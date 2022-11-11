# BATO-MOUCHE/Composition of big cities

Project on analysing OSM data.
Progress :
- [ ] Datascrapping
- [ ] First analys
## Data scrapping

There are two ways to get OSM data :
- use the OSMnx library : really complete
- using Geofabrick : download and zip already .shp formats : great to use with geopands
    - See the near_eiffel_tower notebook
    - default : only a selection of towns/regions/countries : enough at least to starts with
    - advantage : files come in OSM data but also in .shp files : easier to open in geopandas

- using OSM datafiles (.osm = op-to-data, .osh = history) with osmium python library. .osm.pbf = contains every OSM elements versions through time.
     - see the example-code folder
     - main default : not easy extraction for more complicated shapes than a poi ?

The OSM files can be dowload through different ways :
- through the [API](https://www.openstreetmap.org/export) : limited, for instance we can't download the whole Paris (seems logical)
- through API overpass : mirror data from OSM
- through Planet OSM : regular copies
- through [Geofabrik](https://www.geofabrik.de) : regular copies but only a selection of towns/regions/countries. (Geofabrik already suppress user data but the rest of the metadata are the same)
## Link collection for websites and data that might be useful for the project

### Examples and inspirations

[OSM parser with python](https://oslandia.com/en/2017/07/03/openstreetmap-data-analysis-how-to-parse-the-data-with-python/)

[Urban walkabity using OSMnx](https://gispofinland.medium.com/analysing-urban-walkability-using-openstreetmap-and-python-33815d045204)

### Database
#### Geofabrik: download small chunks of osm mapping data and history files
[Europe](https://osm-internal.download.geofabrik.de/europe.html),
[IdF](https://download.geofabrik.de/europe/france/ile-de-france.html)
[see documentation](https://download.geofabrik.de/osm-data-in-gis-formats-free.pdf)

#### SIRENE API to get data for registered company in France and their locations
https://api.insee.fr/catalogue/site/themes/wso2/subthemes/insee/pages/item-info.jag?name=Sirene&version=V3&provider=insee

### Python packages and tools
#### osmium: tool to parse osm files with python bindings pyosmium
[osmium](https://osmcode.org/osmium-tool/), [documentation](https://osmcode.org/osmium-tool/manual.html)

#### OSMnx: another library that can be used to extract data from OSM files
https://github.com/gboeing/osmnx, 
https://github.com/GIScience/ohsome-py

#### Ohsome : another library by Heildelberg university for historical data
https://heigit.org/big-spatial-data-analytics-en/

#### Cartiflette: for working with french geographic data sets
https://github.com/InseeFrLab/cartiflette
and examples
https://pythonds.linogaliana.fr/geopandas/

### Ressources
#### OSMwiki
- tags (map features) for nodes on the map: https://wiki.openstreetmap.org/wiki/Map_features
- projection of geographic coordinates: https://wiki.openstreetmap.org/wiki/Projection : OMS is in WGS-84

#### Heigit
https://heigit.org/big-spatial-data-analytics-en/ 