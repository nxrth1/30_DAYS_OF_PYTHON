"""
Topics to Learn
•	if / elif / else conditional statements
•	Comparison operators (==, !=, <, >, <=, >=)
•	Logical operators (and, or, not)
•	for loops and while loops
•	range() and enumerate()
Project: Elevation Zone Classifier — Read a list of elevations (in metres) and classify each point as:
Valley (<500m), Plain (500–1500m), Highland (1500–3000m), Alpine (>3000m).
Count how many points fall in each zone and print a summary.
You Will Learn
•	Use if-elif-else chains to handle multiple conditions
•	Loop over a list with for
•	Use a dictionary to accumulate counts
•	Print a formatted summary report
Bonus Challenge: Sort the elevation list and find the 10th percentile, median, and 90th percentile without using any libraries

"""

counts = {"Valley": 0, "Plain": 0, "Highland": 0, "Alpine": 0}
elevations = [320, 850, 2100, 4200, 750]
"""
incase the elevation was say in a csv,
import csv

with open("elevations.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header row
    elevations = [float(row[0]) for row in reader]

This is a list comprehension — the Pythonic way to build a list in one line. Breaking it down:

for row in reader — loop through every remaining row
row[0] — grab the first column of that row
float(...) — convert it from text to a decimal number
the whole thing builds your elevations list

"""



for elevation in elevations:
    
    if elevation < 500:
        counts["Valley"] += 1
    elif 500 <= elevation <= 1500:
        counts["Plain"] += 1
    elif 1500 <= elevation <= 3000:
        counts["Highland"] += 1
    else:
        counts["Alpine"] += 1

print("\n=== Elevation Zone Summary ===")
for zone, count in counts.items():
    print(f"  {zone}: {count} counts")

sorted_elevations = sorted(elevations)
n = len(sorted_elevations)

# Helper function for linear interpolation percentile calculation
def get_percentile(data, percentile):
    index = (percentile / 100) * (n - 1)
    lower_idx = int(index)
    upper_idx = min(lower_idx + 1, n - 1)
    fraction = index - lower_idx
    return data[lower_idx] + fraction * (data[upper_idx] - data[lower_idx])

# 2. Calculate and print the requested percentiles
p10 = get_percentile(sorted_elevations, 10)
median = get_percentile(sorted_elevations, 50)
p90 = get_percentile(sorted_elevations, 90)

print(f"Sorted List: {sorted_elevations}")
print(f"10th Percentile: {p10}")
print(f"Median (50th): {median}")
print(f"90th Percentile: {p90}")
