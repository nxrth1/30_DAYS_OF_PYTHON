from math import atan2, cos, degrees, radians, sin, sqrt
EARTH_RADIUS_M = 6_371_008.8


def haversine(lat1, lon1, lat2, lon2, radius=EARTH_RADIUS_M):
   
    phi1 = radians(lat1)
    phi2 = radians(lat2)

    delta_phi = radians(lat2 - lat1)
    delta_lambda = radians(lon2 - lon1)

    a = (
        sin(delta_phi / 2) ** 2
        + cos(phi1) * cos(phi2) * sin(delta_lambda / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return radius * c


def bearing(lat1, lon1, lat2, lon2):
 
    phi1 = radians(lat1)
    phi2 = radians(lat2)
    delta_lambda = radians(lon2 - lon1)

    x = sin(delta_lambda) * cos(phi2)
    y = cos(phi1) * sin(phi2) - sin(phi1) * cos(phi2) * cos(delta_lambda)

    return (degrees(atan2(x, y)) + 360) % 360


def midpoint(lat1, lon1, lat2, lon2):

    phi1 = radians(lat1)
    lambda1 = radians(lon1)
    phi2 = radians(lat2)
    delta_lambda = radians(lon2 - lon1)

    bx = cos(phi2) * cos(delta_lambda)
    by = cos(phi2) * sin(delta_lambda)

    mid_lat = atan2(
        sin(phi1) + sin(phi2),
        sqrt((cos(phi1) + bx) ** 2 + by**2),
    )
    mid_lon = lambda1 + atan2(by, cos(phi1) + bx)

    lat = degrees(mid_lat)

    lon = (degrees(mid_lon) + 540) % 360 - 180

    return lat, lon


def traverse_total_length(points_list):
 
    points = list(points_list)
    total = 0.0

    for index in range(len(points) - 1):
        lat1, lon1 = points[index]
        lat2, lon2 = points[index + 1]

        total += haversine(lat1, lon1, lat2, lon2)

    return total


def main():

    lokichar = (2.3867, 35.6406)
    lodwar = (3.1191, 35.5973)

    sample_traverse = [
        lokichar,
        (2.6500, 35.6200),
        (2.8900, 35.6100),
        lodwar,
    ]

    distance_m = haversine(*lokichar, *lodwar)
    azimuth_deg = bearing(*lokichar, *lodwar)
    mid_lat, mid_lon = midpoint(*lokichar, *lodwar)
    traverse_m = traverse_total_length(sample_traverse)

    print("Turkana corridor sample: Lokichar to Lodwar")
    print(f"Distance: {distance_m:,.2f} m ({distance_m / 1000:.2f} km)")
    print(f"Bearing: {azimuth_deg:.2f} degrees")
    print(f"Midpoint: ({mid_lat:.6f}, {mid_lon:.6f})")
    print(f"Sample traverse length: {traverse_m:,.2f} m")


if __name__ == "__main__":
    main()
