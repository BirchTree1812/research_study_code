"""This file contains variables - more specifically the different dictionaries that can be useful. 
I will define coordinates for country codes of origin country("cty_code") and codes representing US ports of arrival("port_full")
I assume that each country has one main port, from which it exports its goods."""

ton_km = {
    "5700": 4,
    "5800": 4.5, 
    "5520": 7, 
    "5330": 6,
    "2010": 80 
}

# dictionaries of coordinates are necessary.
asian_origins = {
    "5700": [121.470,  31.230],   
    "5800": [129.040,  35.100], 
    "5520": [106.780,  10.780],
    "5330": [ 69.710,  22.740]
}


us_ports = {
    # --- Northeast / New England ---
    "0401": [ -78.893,  42.883],  # Buffalo, NY (Lake Erie / Niagara Frontier)
    "0712": [ -75.143,  39.940],  # Philadelphia, PA (Packer Ave Marine Terminal)
    "0901": [ -70.960,  42.358],  # Boston, MA (Conley Container Terminal)
    "1001": [ -74.017,  40.700],  # New York, NY (Red Hook, Brooklyn)
    "1003": [ -74.165,  40.685],  # Newark, NJ (Port Newark/Elizabeth)
    "1012": [ -74.010,  40.660],  # New York, NY (secondary terminal)
    "1108": [ -75.143,  39.960],  # Philadelphia, PA (Tioga Marine Terminal)
    # --- Mid-Atlantic / Southeast ---
    "1303": [ -76.535,  39.265],  # Baltimore, MD (Seagirt Marine Terminal)
    "1401": [ -76.330,  36.880],  # Norfolk/Newport News, VA
    "1501": [ -77.955,  34.235],  # Wilmington, NC
    "1601": [ -79.911,  32.852],  # Charleston, SC
    "1703": [ -81.140,  32.115],  # Savannah, GA (Garden City Terminal)
    "1801": [ -82.456,  27.910],  # Tampa, FL
    "1803": [ -81.534,  30.395],  # Jacksonville, FL (Blount Island/Dames Point)
    # --- Gulf Coast ---
    "1901": [ -88.040,  30.690],  # Mobile, AL
    "2002": [ -90.060,  29.940],  # New Orleans, LA
    "2006": [ -89.090,  30.368],  # Gulfport, MS
    # --- Southern border (land/air entry — ves_swt_mo typically 0) ---
    "2303": [ -99.507,  27.520],  # Laredo, TX
    "2304": [ -97.494,  25.961],  # Brownsville, TX
    "2507": [-110.934,  31.340],  # Nogales, AZ
    # --- Southern California ---
    "2704": [-118.265,  33.733],  # Los Angeles, CA
    "2709": [-118.216,  33.755],  # Long Beach, CA
    "2720": [-117.170,  32.706],  # San Diego, CA (10th Ave Marine Terminal)
    # --- Northern California ---
    "2801": [-122.390,  37.800],  # San Francisco, CA (Pier 80)
    "2809": [-122.395,  37.795],  # San Francisco, CA (main terminal)
    "2811": [-122.290,  37.795],  # Oakland, CA
    # --- Pacific Northwest ---
    "2904": [-122.755,  45.585],  # Portland, OR
    "3001": [-122.330,  47.610],  # Seattle, WA
    "3002": [-122.430,  47.275],  # Tacoma, WA
    "3004": [-123.434,  48.118],  # Port Angeles, WA
    # --- Alaska ---
    "3126": [-149.890,  61.235],  # Anchorage, AK
    # --- Hawaii ---
    "3201": [-157.870,  21.310],  # Honolulu, HI
    # --- Pacific territories ---
    "3303": [ 144.794,  13.444],  # Apra Harbor, Guam
    "3310": [ 145.745,  15.188],  # Saipan, CNMI
    # --- Interior / other (approx — ves_swt_mo typically 0 for washing machines) ---
    "3401": [ -87.630,  41.850],  # Interior customs office (approx)
    "3501": [ -93.265,  44.977],  # Minneapolis, MN (Mississippi River port)
    "3604": [-119.213,  34.151],  # Port Hueneme, CA (Channel Islands Harbor)
    # --- Great Lakes (upper) ---
    "3801": [ -92.101,  46.780],  # Duluth-Superior, MN/WI
    "3802": [ -87.447,  41.663],  # Indiana Harbor, IN (Lake Michigan)
    # --- Chicago / inland (exclude from sea analysis) ---
    "3901": [ -87.620,  41.880],  # Chicago, IL (Great Lakes / inland)
    # --- Great Lakes (Lake Erie / Ohio) ---
    "4101": [ -81.700,  41.500],  # Cleveland, OH
    "4102": [ -83.540,  41.663],  # Toledo, OH (Lake Erie)
    "4103": [ -82.706,  41.449],  # Sandusky, OH (Lake Erie)
    "4110": [ -80.799,  41.865],  # Ashtabula, OH (Lake Erie)
    "4115": [ -80.554,  41.966],  # Conneaut, OH (Lake Erie)
    # --- Caribbean ---
    "4909": [ -66.100,  18.450],  # San Juan, PR
    # --- South Florida ---
    "5201": [ -80.165,  25.778],  # Miami, FL (PortMiami)
    "5203": [ -80.116,  26.090],  # Port Everglades, FL
    "5206": [ -80.290,  25.796],  # Miami International AIRPORT — exclude from sea analysis
    # --- Texas ---
    "5301": [ -95.020,  29.733],  # Houston, TX
}

mexico_start = [-100.310, 25.671]

state_centroids = {
    "AK": [-153.369, 64.200],
    "AL": [ -86.902, 32.799],
    "AR": [ -92.373, 34.970],
    "AZ": [-111.431, 34.049],
    "CA": [-119.418, 36.778],
    "CO": [-105.548, 38.998],
    "CT": [ -72.757, 41.603],
    "DC": [ -77.016, 38.907],
    "DE": [ -75.528, 38.910],
    "FL": [ -81.516, 27.664],
    "GA": [ -82.907, 32.157],
    "HI": [-155.665, 20.293],
    "IA": [ -93.098, 42.012],
    "ID": [-114.479, 44.068],
    "IL": [ -88.986, 40.349],
    "IN": [ -86.258, 39.849],
    "KS": [ -98.484, 38.527],
    "KY": [ -84.670, 37.668],
    "LA": [ -91.962, 31.169],
    "MA": [ -71.382, 42.407],
    "MD": [ -76.802, 39.063],
    "ME": [ -69.445, 44.694],
    "MI": [ -85.602, 44.314],
    "MN": [ -94.636, 46.392],
    "MO": [ -92.603, 38.456],
    "MS": [ -89.679, 32.742],
    "MT": [-109.642, 46.880],
    "NC": [ -79.019, 35.760],
    "ND": [-100.470, 47.528],
    "NE": [ -99.902, 41.493],
    "NH": [ -71.572, 43.194],
    "NJ": [ -74.521, 40.298],
    "NM": [-106.018, 34.307],
    "NV": [-116.419, 38.803],
    "NY": [ -75.524, 42.165],
    "OH": [ -82.764, 40.388],
    "OK": [ -97.093, 35.468],
    "OR": [-120.554, 43.804],
    "PA": [ -77.210, 40.590],
    "PR": [ -66.591, 18.220],
    "RI": [ -71.477, 41.580],
    "SC": [ -81.164, 33.836],
    "SD": [ -99.902, 44.500],
    "TN": [ -86.580, 35.518],
    "TX": [ -97.564, 31.054],
    "UT": [-111.094, 39.321],
    "VA": [ -78.657, 37.431], # alternative name for Virginia
    "VT": [ -72.578, 44.068],
    "WA": [-121.490, 47.400],
    "WI": [ -89.617, 44.268],
    "WV": [ -80.455, 38.491],
    "WY": [-107.290, 43.076],
}