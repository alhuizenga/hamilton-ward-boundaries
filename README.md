# hamilton-ward-boundaries

Python 3 script that retrieves public data from the Hamilton Ward Boundaries mapping service, published by the City of Hamilton at:

https://spatialsolutions.hamilton.ca/webgis/rest/services/General/Political/MapServer/15/query?f=json

Documentation about how to query the service endpoint is available here:

https://developers.arcgis.com/rest/services-reference/enterprise/query-feature-service-layer-.htm

Outputs a JSON file that contains the geographic coordinates for the intersection points that form each ward's polygon, in both [EPSG:3857]|(https://epsg.io/4326) and EPSG:4326 coordinate formats.

https://spatialreference.org/ref/epsg/wgs-84/

Outputs registry data as local CSV and JSON files:

* hamilton_lobbyist_registry_(current-date).json

Uses these modules:

* requests
* datetime
* json
