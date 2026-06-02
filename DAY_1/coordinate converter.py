import math

try:
    latitude = float(input("Please input your latitude in decimals: "))
    longitude = float(input("Please input your longitude in decimals: "))

    if not(-90 <= latitude <= 90):
        raise ValueError("Latitude must be between -90 and 90")
    if not(-180 <= longitude <= 180):
        raise ValueError("Longitude must be between -180 and 180")
except ValueError as e:
    raise TypeError(str(e))


def dd_to_dms(decimal_degree, is_longitude = True):
    if is_longitude:
        direction = "E" if decimal_degree >= 0 else "W"
    else:
        direction = "N" if decimal_degree >= 0 else "S"
    abs_dd = abs(decimal_degree)
    degrees= int(abs_dd)
    minutes_float = (abs_dd - degrees)*60
    minutes_int = int(minutes_float)
    minutes = abs(minutes_int)
    seconds = (minutes_float-minutes_int)*60
    seconds = round(seconds,3)
    if seconds >= 60.0:
        seconds = 0.0
        minutes += 1

    if minutes >= 60.0:
        minutes = 0.0
        degrees += 1

    dms_string = f"{degrees}° {minutes}' {seconds}\" {direction}"
    
    return degrees, minutes, seconds, direction, dms_string

lat_deg, lat_min, lat_sec, lat_dir, lat_str = dd_to_dms(latitude, is_longitude=False)
lon_deg, lon_min, lon_sec, lon_dir, lon_str = dd_to_dms(longitude, is_longitude=True)

print(f"Longitude:  {lon_str}")
print(f"Latitude: {lat_str}")

