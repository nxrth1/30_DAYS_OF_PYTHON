 
"""Survey Control Point Class — Design a ControlPoint class with attributes:
 point_id, easting, northing, elevation, order (1st/2nd/3rd order).
   Add methods: to_dict(), to_wkt(), distance_to(other_point), 
   and a class method from_csv_row(row). 
   Create a ControlNetwork class that holds a list of ControlPoints
     and can export them as GeoJSON.
import math
import json
class SurveyControlPoint:
    def __init__(self, point_id, easting, northing, elevation, order):
        self.point_id = point_id
        self.easting = float(easting)
        self.northing = float(northing)
        self.elevation = float(elevation)
        self.order = order
        
    def to_dict(self):
        return {
            "point_id": self.point_id,
            "easting": self.easting,
            "northing":self.northing,
            "elevation":self.elevation,
            "order": self.order,
        }

    def to_wkt(self):
        return f"POINT ({self.easting} {self.northing})"
    
    def distance_to(self, other):
        dx = self.easting - other.easting
        dy = self.northing - other.northing
        return math.sqrt(dx**2 + dy**2)
    
    @classmethod
    def from_csv_row(cls, row):
        return cls (
            point_id = row[0],
            easting = row[1],
            northing = row[2],
            elevation = row[3],
            order = row[4],
        )

    

class ControlNetwork:
    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)


    def export_to_geojson(self):
    feature_list = []

    for pt in self.points:
        single_feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [pt.easting, pt.northing, pt.elevation],
            },
            "properties": {"point_id": pt.point_id, "order": pt.order},
        }
        feature_list.append(single_feature)

    geojson_final = {
        "type": "FeatureCollection",
        "features": feature_list,
    }
    return json.dumps(geojson_final, indent=2)
# ── Create individual points ──────────────────────────────────────────────────
p1 = SurveyControlPoint("NRP01", 237025.0, 9857378.0, 1240.0, "1st")
p2 = SurveyControlPoint("NRP02", 237100.0, 9857500.0, 1255.0, "2nd")
p3 = SurveyControlPoint("NRP03", 237200.0, 9857600.0, 1260.0, "3rd")

# ── Test individual methods ───────────────────────────────────────────────────
print("=== Single Point Tests ===")
print(p1.to_wkt())
print(p1.to_dict())
print(f"Distance p1 to p2: {p1.distance_to(p2):.3f} m")

# ── Test from_csv_row ─────────────────────────────────────────────────────────
csv_row = ["NRP04", "237300.0", "9857700.0", "1270.0", "1st"]
p4 = SurveyControlPoint.from_csv_row(csv_row)
print(f"\nPoint from CSV row: {p4.to_dict()}")

# ── Test ControlNetwork ───────────────────────────────────────────────────────
print("\n=== Network GeoJSON Export ===")
network = ControlNetwork()
network.add_point(p1)
network.add_point(p2)
network.add_point(p3)
network.add_point(p4)

print(network.export_to_geojson())"""


import math
import json

class SurveyControlPoint:
    def __init__(self, point_id, easting, northing, elevation, order):
        self.point_id  = point_id
        self.easting   = float(easting)
        self.northing  = float(northing)
        self.elevation = float(elevation)
        self.order     = order

    def to_dict(self):
        return {
            "point_id":  self.point_id,
            "easting":   self.easting,
            "northing":  self.northing,
            "elevation": self.elevation,
            "order":     self.order,
        }

    def to_wkt(self):
        return f"POINT ({self.easting} {self.northing})"

    def distance_to(self, other):
        dx = self.easting  - other.easting
        dy = self.northing - other.northing
        return math.sqrt(dx**2 + dy**2)

    @classmethod
    def from_csv_row(cls, row):
        return cls(
            point_id  = row[0],
            easting   = row[1],
            northing  = row[2],
            elevation = row[3],
            order     = row[4],
        )


class ControlNetwork:
    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def export_to_geojson(self):
        feature_list = []

        for pt in self.points:
            single_feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [pt.easting, pt.northing, pt.elevation],
                },
                "properties": {
                    "point_id": pt.point_id,
                    "order":    pt.order,
                },
            }
            feature_list.append(single_feature)

        geojson_final = {
            "type":     "FeatureCollection",
            "features": feature_list,
        }
        return json.dumps(geojson_final, indent=2)


# ── Create individual points ──────────────────────────────────────────────────
p1 = SurveyControlPoint("NRP01", 237025.0, 9857378.0, 1240.0, "1st")
p2 = SurveyControlPoint("NRP02", 237100.0, 9857500.0, 1255.0, "2nd")
p3 = SurveyControlPoint("NRP03", 237200.0, 9857600.0, 1260.0, "3rd")

# ── Test individual methods ───────────────────────────────────────────────────
print("=== Single Point Tests ===")
print(p1.to_wkt())
print(p1.to_dict())
print(f"Distance p1 to p2: {p1.distance_to(p2):.3f} m")

# ── Test from_csv_row ─────────────────────────────────────────────────────────
csv_row = ["NRP04", "237300.0", "9857700.0", "1270.0", "1st"]
p4 = SurveyControlPoint.from_csv_row(csv_row)
print(f"\nPoint from CSV row: {p4.to_dict()}")

# ── Test ControlNetwork ───────────────────────────────────────────────────────
print("\n=== Network GeoJSON Export ===")
network = ControlNetwork()
network.add_point(p1)
network.add_point(p2)
network.add_point(p3)
network.add_point(p4)

print(network.export_to_geojson())