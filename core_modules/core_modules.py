"""This module contains all the necessary functions for the research study"""

from geopy.distance import great_circle
import searoute as sr
import coordinates as coord

# a function for computing distances
def compute_distance(row, departure_coords, destination_coords, by_sea, departure_code = None, destination_code = None):
    """This function computes distance based on coordinates of start and end. \n
    Requirements:\n
    - A dataframe with two columns: starting locations, destination locations
    - A dictionary that has coordinates for those locations \n Note, if a dictionary has only one point, that is also accepted"""
    # defines lists of coordinates, which are then connected to corresponding dataframe columns "departure_code" and "destination_code" respectively
    if isinstance(departure_coords, dict):
        origin = departure_coords[row[departure_code]]
    else:
        origin = departure_coords
    if isinstance(destination_coords, dict):
        dest = destination_coords[row[destination_code]]
    else:
        dest = destination_coords
    # if this is sea distance, use the searoute model
    if by_sea == True:
        return sr.searoute(origin, dest).properties["length"]
    # if this is land distance, use great_circle from geopy.distance module. Note that great_circle takes (longitude, latitude) coordinates, 
    # inverse of how they're usually written
    else: 
        return great_circle(origin[::-1], dest[::-1]).km * 1.3

def compute_co2(row, transportation_type):
    weight = row[transportation_type]
    dist = row["distance"]
    co2_coeff = coord.ton_km[row["cty_code"]]
    return weight * dist * co2_coeff