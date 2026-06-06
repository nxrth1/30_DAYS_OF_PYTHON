"""Survey CSV Processor — Write a script that reads a CSV of 
survey control points (Point_ID, Easting, Northing, Elevation, Description),
filters out any points with elevation < 0 (bad data), 
calculates basic statistics (mean, min, max elevation),
and writes a clean output CSV with a summary header row."""

import csv
import statistics 
import os

if not os.path.exists("data.csv"):
    print("Error: data.csv not found")
    sys.exit(1)

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header row
    rows = []
    for row in reader:
        rows.append({
            "Point_ID":    row[0],
            "Easting":     float(row[1]),
            "Northing":    float(row[2]),
            "Elevation":   float(row[3]),
            "Description": row[4],
        })

for row in rows:

    if row["Elevation"] < 0:
        print("Bad data point, skipping")
    else:
        print("Good data point, keeping")


clean_rows = []
for row in rows:
    if row["Elevation"] < 0:
        print(f"Skipping {row['Point_ID']} — bad elevation: {row['Elevation']}")
    else:
        clean_rows.append(row)

elevations = [row["Elevation"] for row in clean_rows]

mean_elev = sum(elevations) / len(elevations)
min_elev  = min(elevations)
max_elev  = max(elevations)

print(f"\n=== Elevation Statistics ===")
print(f"  Points kept:  {len(clean_rows)}")
print(f"  Mean:         {mean_elev:.2f} m")
print(f"  Min:          {min_elev:.2f} m")
print(f"  Max:          {max_elev:.2f} m")

with open("clean_data.csv", "w", newline="") as out_file:
    writer = csv.DictWriter(out_file, fieldnames=["Point_ID","Easting","Northing","Elevation","Description"])
    writer.writeheader()
    writer.writerows(clean_rows)

print("\nClean CSV written to clean_data.csv")


from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_filename = f"report_{timestamp}.txt"