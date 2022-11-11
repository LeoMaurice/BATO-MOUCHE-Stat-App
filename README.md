# BATO-MOUCHE

Project on analysing OSM data

## Link collection for websites and data that might be useful for the project


### Geofabrik: download small chunks of osm mapping data and history files
[Europe](https://osm-internal.download.geofabrik.de/europe.html),
[IdF](https://download.geofabrik.de/europe/france/ile-de-france.html)

#### osmium: tool to parse osm files with python bindings pyosmium
[osmium](https://osmcode.org/osmium-tool/), [documentation](https://osmcode.org/osmium-tool/manual.html)

### OSMnx: another library that can be used to extract data from OSM files
https://github.com/gboeing/osmnx

### cartiflette: working with french geographic data sets
https://github.com/InseeFrLab/cartiflette
and examples
https://pythonds.linogaliana.fr/geopandas/

### SIRENE API to get data for registered company in France and their locations
https://api.insee.fr/catalogue/site/themes/wso2/subthemes/insee/pages/item-info.jag?name=Sirene&version=V3&provider=insee


### OSMwiki
- tags (map features) for nodes on the map: https://wiki.openstreetmap.org/wiki/Map_features
- projection of geographic coordinates: https://wiki.openstreetmap.org/wiki/Projection

# Examples and inspirations

## [OSM parser with python](https://oslandia.com/en/2017/07/03/openstreetmap-data-analysis-how-to-parse-the-data-with-python/)

# Upgrades

## On OSM/Geofabrik data
- [ ] Téléchargement et dézippage à partir du lien geofabrik
- [ ] Ou alternativement utiliser l'[API](https://www.openstreetmap.org/#map=10/45.0000/0.0000) d'OSM : voir le dossier ./example-code/
- [ ] Obtenir les adresses
