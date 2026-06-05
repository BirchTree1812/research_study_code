"""This file contains variables - more specifically the different dictionaries that can be useful."""

ton_km = {
    "5700": 4,
    "5800": 4.5, 
    "5520": 7, 
    "5330": 6,
    "2010": 80 
}

asian_origins = {
    "5700": [121.470,  31.230],   
    "5800": [129.040,  35.100], 
    "5520": [106.780,  10.780],
    "5330": [ 69.710,  22.740]
}


us_ports = {
    "1003": [ -74.165,  40.685],  # Newark, NJ (Port Newark/Elizabeth)
    "1303": [ -76.535,  39.265],  # Baltimore, MD (Seagirt Marine Terminal)
    "1401": [ -76.330,  36.880],  # Norfolk/Newport News, VA
    "1601": [ -79.911,  32.852],  # Charleston, SC
    "1703": [ -81.140,  32.115],  # Savannah, GA (Garden City Terminal)
    "1801": [ -82.456,  27.910],  # Tampa, FL
    "1803": [ -81.534,  30.395],  # Jacksonville, FL (Blount Island/Dames Point)
    "1901": [ -88.040,  30.690],  # Mobile, AL
    "2002": [ -90.060,  29.940],  # New Orleans, LA
    "2704": [-118.265,  33.733],  # Los Angeles, CA
    "2709": [-118.216,  33.755],  # Long Beach, CA
    "2809": [-122.395,  37.795],  # San Francisco, CA
    "2811": [-122.290,  37.795],  # Oakland, CA
    "2904": [-122.755,  45.585],  # Portland, OR
    "3001": [-122.330,  47.610],  # Seattle, WA
    "3002": [-122.430,  47.275],  # Tacoma, WA
    "3126": [-149.890,  61.235],  # Anchorage, AK
    "3201": [-157.870,  21.310],  # Honolulu, HI
    "3901": [ -87.620,  41.880],  # Chicago, IL (Great Lakes / inland)
    "4101": [ -81.700,  41.500],  # Cleveland, OH (Great Lakes)
    "4909": [ -66.100,  18.450],  # San Juan, PR
    "5201": [ -80.165,  25.778],  # Miami, FL (PortMiami)
    "5203": [ -80.116,  26.090],  # Port Everglades, FL
    "5206": [ -80.290,  25.796],  # Miami International AIRPORT — exclude from sea analysis
    "5301": [ -95.020,  29.733]  # Houston, TX
}

mexico_start = [-100.310, 25.671]

state_centroids = {
    "CA": [-119.418, 36.778],
    "CO": [-105.548, 38.998],
    "FL": [ -81.516, 27.664],
    "GA": [ -82.907, 32.157],
    "IL": [ -88.986, 40.349],
    "IN": [ -86.258, 39.849],
    "KY": [ -84.670, 37.668],
    "MD": [ -76.802, 39.063],
    "MI": [ -85.602, 44.314],
    "NJ": [ -74.521, 40.298],
    "OH": [ -82.764, 40.388],
    "PA": [ -77.210, 40.590],
    "PR": [ -66.591, 18.220],
    "TX": [ -97.564, 31.054],
    "WA": [-121.490, 47.400]
}