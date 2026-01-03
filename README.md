#  Offline Terrain Analyzer (Day 2)

**Day 2** focuses on handling geospatial data locally, removing the dependency on external APIs.

##  Objective
To process raw satellite imagery (GeoTIFF format) offline. This ensures low-latency data access, which is essential for real-time decision-making systems in autonomous vehicles or drones operating in remote areas.

##  Tech Stack
* **Python 3.14.0**
* **Rasterio:** The industry-standard library for reading and writing geospatial raster data.
* **NumPy:** For efficient array manipulation.

##  How It Works
The script consists of two parts:
1.  **Synthetic Data Generation:** Since I am not distributing large satellite files, the script first generates a synthetic `GeoTIFF` file representing a terrain with random elevation values (e.g., a Mars surface simulation).
2.  **Coordinate Mapping:** It translates physical coordinates (Latitude/Longitude) into the file's pixel coordinates (Row/Column) to retrieve the exact elevation value.

### Sample Output:
```text
 Generating synthetic Mars surface data...
 Created: fake_mars_terrain.tif

 Analyzing Rover path on local terrain file..
 File Metadata: 100x100 pixels, CRS:EPSG:4326
--------------------------------------------------
 point_1              | Lon: 30.150, Lat: 19.850 | Elevation: 4815 m
 point_2              | Lon: 30.500, Lat: 19.500 | Elevation: -752 m
 point_3              | Lon: 30.800, Lat: 19.200 | Elevation: 102 m
 unknown void         is OUT OF MAP BOUNDS!
