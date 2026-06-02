from pyproj import Transformer
import sys

# ── Input ────────────────────────────────────────────────────────────────────
print("=== Coordinate Converter ===")
print("Converts DD → DMS and UTM (WGS84 or Arc 1960)")
print()

try:
    latitude  = float(input("Enter latitude  (decimal degrees): "))
    longitude = float(input("Enter longitude (decimal degrees): "))

    if not (-90 <= latitude <= 90):
        raise ValueError("Latitude must be between -90 and 90")
    if not (-180 <= longitude <= 180):
        raise ValueError("Longitude must be between -180 and 180")

except ValueError as e:
    print(f"Invalid input: {e}")
    sys.exit(1)

datum_choice = input("Datum — enter 1 for WGS84, 2 for Arc 1960: ").strip()
if datum_choice == "2":
    source_datum = "EPSG:4210"
    datum_label  = "Arc 1960"
else:
    source_datum = "EPSG:4326"
    datum_label  = "WGS84"


# ── DD to DMS ────────────────────────────────────────────────────────────────
def dd_to_dms(decimal_degree, is_longitude=True):
    """Convert a decimal degree value to a DMS string."""

    if is_longitude:
        direction = "E" if decimal_degree >= 0 else "W"
    else:
        direction = "N" if decimal_degree >= 0 else "S"  # fixed: was "E"

    abs_dd        = abs(decimal_degree)
    degrees       = int(abs_dd)
    minutes_float = (abs_dd - degrees) * 60
    minutes       = int(minutes_float)
    seconds       = (minutes_float - minutes) * 60   # fixed: was minutes_int - minutes
    seconds       = round(seconds, 3)

    # Handle floating point overflow
    if seconds >= 60.0:
        seconds  = 0.0
        minutes += 1
    if minutes >= 60:
        minutes  = 0
        degrees += 1                                  # fixed: was degree += 1

    dms_string = f"{degrees}° {minutes}' {seconds}\" {direction}"
    return degrees, minutes, seconds, direction, dms_string


# ── UTM Zone ─────────────────────────────────────────────────────────────────
def get_utm_epsg(longitude, latitude):
    """Calculate UTM zone number and EPSG code from decimal degrees."""
    zone = int((longitude + 180) / 6) + 1
    if latitude >= 0:
        epsg = 32600 + zone   # WGS84 UTM Northern hemisphere
    else:
        epsg = 32700 + zone   # WGS84 UTM Southern hemisphere
    return epsg, zone


# ── DD to UTM ────────────────────────────────────────────────────────────────
def dd_to_utm(latitude, longitude, source_datum="EPSG:4326"):
    """Transform decimal degree coordinates to UTM Easting/Northing."""
    epsg, zone   = get_utm_epsg(longitude, latitude)
    hemisphere   = "N" if latitude >= 0 else "S"

    transformer          = Transformer.from_crs(source_datum, epsg, always_xy=True)
    easting, northing    = transformer.transform(longitude, latitude)

    return easting, northing, zone, hemisphere, epsg


# ── Run conversions ───────────────────────────────────────────────────────────
lat_deg, lat_min, lat_sec, lat_dir, lat_str = dd_to_dms(latitude,  is_longitude=False)
lon_deg, lon_min, lon_sec, lon_dir, lon_str = dd_to_dms(longitude, is_longitude=True)

easting, northing, zone, hemisphere, epsg = dd_to_utm(latitude, longitude, source_datum)


# ── Output ───────────────────────────────────────────────────────────────────
print()
print("=" * 40)
print(f"  Datum:      {datum_label}")
print(f"  Latitude:   {lat_str}")
print(f"  Longitude:  {lon_str}")
print("-" * 40)
print(f"  UTM Zone:   {zone}{hemisphere}")
print(f"  EPSG:       {epsg}")
print(f"  Easting:    {easting:.3f} m")
print(f"  Northing:   {northing:.3f} m")
print("=" * 40)
