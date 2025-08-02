import pyproj

def get_geoid_height(lat, lon):
    # Define the geoid model (EGM96 is commonly used with WGS84)
    geoid = pyproj.Geoid("egm96")

    # Get geoid height above the ellipsoid at the given location
    height = geoid.height(lat, lon)
    return height