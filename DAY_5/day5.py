"""Parcel Attribute Store — Model a land parcel database using 
a list of dictionaries. Each parcel has: 
parcel_id, area_ha, land_use, owner, county. 
Write functions to: filter by county, 
find the largest parcel, 
list all unique land uses, 
and merge two parcel lists removing duplicates by parcel_id."""


parcels = [
    {
        "parcel_id": "LR21",
        "area_ha": 12.6,
        "land_use": "africulture",
        "owner": "Kenya",
        "county": "Nakuru"
    },
    {
       "parcel_id": "LR34",
        "area_ha": 123,
        "land_use": "fishing",
        "owner": "nyanya",
        "county": "Nairrru" 
    },
]

def filter_by_county(parcels, county):
    results = []
    for parcel in parcels:
        if parcel["county"] == county:
            results.append(parcel)
    return results

nakuru_parcels = filter_by_county(parcels, "Nakuru")
print(nakuru_parcels)



def largest_area(parcels):
    largest = parcels[0]
    for parcel in parcels:
        if parcel["area_ha"] > largest["area_ha"]:
            largest = parcel
    return largest

biggest = largest_area(parcels)
print(f"Largest parcel: {biggest['parcel_id']} - {biggest['area_ha']} in {biggest['county']}")


def list_land_uses(parcels):
    land_uses = set()
    for parcel in parcels:
        land_uses.add(parcel["land_use"])

    #return land_uses

    return {parcel["land_use"] for parcel in parcels}


uses = list_land_uses(parcels)
print(f"Unique: {uses}")


def merge_parcels(parcels, new_parcels):
    combined = parcels + new_parcels
    seen_ids = set()
    results = []
    for parcel in combined:
        if parcel["parcel_id"] not_in seen_ids:
            results.append(parcel)
            seen_ids.add(parcel["parcel_id"])
        return results

merged = merge_parcels(parcels, new_parcels)
print(f"Total PArcels: {merged}")