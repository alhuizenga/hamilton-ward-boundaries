# hamilton-ward-boundaries

Python 3 script that retrieves public data from the Hamilton ward boundaries mapping service, published by the City of Hamilton. Outputs a date-stamped JSON file that contains the geographic coordinates for the intersection points that form the boundaries for each ward in Hamilton, in both [EPSG:3857](https://epsg.io/4326) and [EPSG:4326](https://epsg.io/4326) coordinate formats.

The mapping service endpoint is published by the City of Hamilton here:

https://spatialsolutions.hamilton.ca/webgis/rest/services/General/Political/MapServer/15/query?f=json

Documentation about how to query the endpoint is available here: 

https://developers.arcgis.com/rest/services-reference/enterprise/query-feature-service-layer-.htm

Uses these modules:

* requests
* datetime
* json
