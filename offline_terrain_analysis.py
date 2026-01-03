import rasterio 
from rasterio.transform import from_origin
import numpy as np

def generate_synthetic_mars_terrain(filename):
    """
     GeoTIFF dosyası simülasyonu yapacağız
     rastgele yükseklik verileriyle 'fake_mars_terrain.tif' oluşturacağız
    """

    print("\n\n Generating synthetic Mars surface data...")

    # 100*100 piksellik bir alan yüksekliilikler -3000m(krater) ile 5000m(dağ) arasinda olacak
    data = np.random.randint(low=-3000, high=5000, size=(100, 100)).astype(rasterio.int16)
    
    # koordinat sistemi ayarlari
    transform = from_origin(30.0, 20.0, 0.01, 0.01)# Batı, Kuzey, Piksel Boyutu

    with rasterio.open(
        filename, 'w',
        driver= 'GTiff',
        height=data.shape[0],
        width=data.shape[1],
        count=1,
        dtype=data.dtype,
        crs='+proj=latlong',
        transform=transform,
    ) as dst:
        dst.write(data, 1)
    print(f" Created: {filename}")

def analyze_rover_path(filename, coordinates):
    """
    yerel bir GeoTIFF dosyasından belirlli koordinatların yüksekliğini okunacak
    internet bağlantısı gerektirmez hızlıdır 
    """
    print("\n Analyzing Rover path on local terrain file..")

    with rasterio.open(filename) as src:
        print(f" File Metadata: {src.width}x{src.height} pixels, CRS:{src.crs}")
        print("-"*50)

        for name, (lon, lat) in coordinates.items():
            # Coğrafi koordinatı lat/lon dosyadaki piksel sırasına row/col çevirilecek
            row, col = src.index(lon,lat)

            #veriyi oku
            try:
                elevation = src.read(1)[row, col]
                print(f" {name:<20} | Lon: {lon:.3f}, Lat: {lat:.3f} | Elevation: {elevation} m")
            except IndexError:
                print(f" {name:<20} is OUT OF MAP BOUNDS!")

#--------------
if __name__ == "__main__":
    tif_file= "fake_mars_terrain.tif"

    # önce sahte veriyi oluşturalım 
    generate_synthetic_mars_terrain(tif_file)

    # roverin gideceği noktalar 

    rover_stops = {
        "point_1":        (30.15, 19.85),
        "point_2":        (30.50, 19.50),
        "point_3":        (30.80, 19.20),
        "unknown void":   (35.00, 10.00) # Harita dışı
    }

    #analiz
    analyze_rover_path(tif_file, rover_stops)



