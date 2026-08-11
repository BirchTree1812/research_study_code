"""This file contains variables - more specifically the different dictionaries that can be useful. 
I will define coordinates for country codes of origin country("cty_code") and codes representing US ports of arrival("port_full")
I assume that each country has one main port, from which it exports its goods."""


# Correct colspecs for ISTHS6M (State HS6 Imports), record length 258
colspecs_land = [
    (0, 6),      # commodity (6-digit HS code)
    (6, 10),     # cty_code (4-digit country code)
    (10, 12),    # state (2-letter postal)
    (12, 16),    # year
    (16, 18),    # month
    (18, 33),    # gen_val_mo (general imports total value)
    (33, 48),    # con_val_mo (imports for consumption value)
    (48, 63),    # air_val_mo
    (63, 78),    # air_swt_mo (air shipping weight, kg)
    (78, 93),    # ves_val_mo
    (93, 108),   # ves_swt_mo (vessel shipping weight, kg)
    (108, 123),  # cnt_val_mo (containerized vessel value)
    (123, 138),  # cnt_swt_mo (containerized vessel weight)
    (138, 153),  # gen_val_yr (year-to-date)
    (153, 168),  # con_val_yr
    (168, 183),  # air_val_yr
    (183, 198),  # air_swt_yr
    (198, 213),  # ves_val_yr
    (213, 228),  # ves_swt_yr
    (228, 243),  # cnt_val_yr
    (243, 258),  # cnt_swt_yr
]
names_land = ['commodity', 'cty_code', 'state', 'year', 'month',
         'gen_val_mo', 'con_val_mo', 'air_val_mo', 'air_swt_mo',
         'ves_val_mo', 'ves_swt_mo', 'cnt_val_mo', 'cnt_swt_mo',
         'gen_val_yr', 'con_val_yr', 'air_val_yr', 'air_swt_yr',
         'ves_val_yr', 'ves_swt_yr', 'cnt_val_yr', 'cnt_swt_yr']

str_cols_land = ['commodity', 'cty_code', 'state', 'year', 'month']

# dictionary of tariff rates for washing machines in 2025 tied to country codes
# Mexico is the exception, since some goods fell under the USMCA exemption in August.
# Thus, we can assume that for Mexico, the dose is between 0 and 0.25 * (1-0.84)
tariff_rate = {"5700": 0.20, "5800": 0.15, "5520": 0.20, "5330": 0.50, "2010": 0.04}

# and this is information for how to unpack PORTHS6MM files
colspecs_sea = [
    (0, 6),      # commodity (6-digit HS code)
    (6, 10),     # cty_code (Schedule C, 4-digit)
    (10, 12),    # dist_unlade (Schedule D district, 2-digit)
    (12, 14),    # port_unlade (Schedule D port within district, 2-digit)
    (14, 18),    # year
    (18, 20),    # month
    (20, 35),    # gen_val_mo  (general imports value, this month)
    (35, 50),    # air_val_mo
    (50, 65),    # air_swt_mo  (air shipping weight, kg)
    (65, 80),    # ves_val_mo
    (80, 95),    # ves_swt_mo  (vessel shipping weight, kg)
    (95, 110),   # cnt_val_mo  (containerized vessel value)
    (110, 125),  # cnt_swt_mo  (containerized vessel weight)
    (125, 140),  # gen_val_yr  (year-to-date totals begin)
    (140, 155),  # air_val_yr
    (155, 170),  # air_swt_yr
    (170, 185),  # ves_val_yr
    (185, 200),  # ves_swt_yr
    (200, 215),  # cnt_val_yr
    (215, 230),  # cnt_swt_yr
]
names_sea = ['commodity', 'cty_code', 'dist_unlade', 'port_unlade', 'year', 'month',
         'gen_val_mo', 'air_val_mo', 'air_swt_mo', 'ves_val_mo', 'ves_swt_mo',
         'cnt_val_mo', 'cnt_swt_mo',
         'gen_val_yr', 'air_val_yr', 'air_swt_yr', 'ves_val_yr', 'ves_swt_yr',
         'cnt_val_yr', 'cnt_swt_yr']
str_cols_sea = ['commodity', 'cty_code', 'dist_unlade', 'port_unlade', 'year', 'month']


ton_km = {
    "5700": 4,
    "5800": 4.5,
    "5520": 7,
    "5330": 6,
    "2010": 80,
}

# dictionaries of coordinates are necessary.
asian_origins = {
    "5700": [121.470,  31.230],   # China
    "5800": [129.040,  35.100], # South Korea
    "5520": [106.780,  10.780], # Vietnam
    "5330": [ 69.710,  22.740] # India
}

# this is an exhaustive list of US ports of arrival and their coordinates. It is necessary to avoid a key error, even though not all ports are used in the analysis.
# the coordinates are approximate and represent the main port of arrival for each port code. The coordinates are in the format [longitude, latitude].
us_ports = {
    # --- Maine (District 01) ---
    "0106": [ -68.780,  44.801],  # Bangor, ME
    "0115": [ -67.000,  44.900],  # Eastport, ME (border crossing)
    # --- Champlain / Vermont border (District 02) ---
    "0209": [ -73.363,  44.993],  # Rouses Point, NY
    "0212": [ -73.447,  44.975],  # Champlain, NY
    # --- Buffalo, NY / Niagara Frontier (District 04) ---
    "0401": [ -78.893,  42.883],  # Buffalo, NY (Lake Erie / Niagara Frontier)
    "0408": [ -79.061,  43.095],  # Niagara Falls, NY
    "0417": [ -79.040,  43.170],  # Lewiston, NY
    # --- Philadelphia area (District 07) ---
    "0701": [ -75.143,  39.940],  # Philadelphia, PA (area port)
    "0708": [ -75.360,  39.850],  # Chester, PA area
    "0712": [ -75.143,  39.940],  # Philadelphia, PA (Packer Ave Marine Terminal)
    # --- Boston (District 09) ---
    "0901": [ -70.960,  42.358],  # Boston, MA (Conley Container Terminal)
    # --- New York (District 10) ---
    "1001": [ -74.017,  40.700],  # New York, NY (Red Hook, Brooklyn)
    "1002": [ -74.017,  40.700],  # New York, NY (alternate terminal)
    "1003": [ -74.165,  40.685],  # Newark, NJ (Port Newark/Elizabeth)
    "1012": [ -74.010,  40.660],  # New York, NY (secondary terminal)
    # --- Philadelphia area (District 11) ---
    "1101": [ -75.143,  39.940],  # Philadelphia, PA
    "1102": [ -75.150,  39.895],  # Philadelphia, PA (alternate terminal)
    "1104": [ -75.140,  39.960],  # Philadelphia, PA (alternate terminal)
    "1108": [ -75.143,  39.960],  # Philadelphia, PA (Tioga Marine Terminal)
    "1109": [ -75.155,  39.940],  # Philadelphia, PA (alternate terminal)
    # --- Baltimore (District 13) ---
    "1301": [ -76.535,  39.265],  # Baltimore, MD (main)
    "1303": [ -76.535,  39.265],  # Baltimore, MD (Seagirt Marine Terminal)
    # --- Norfolk / Newport News (District 14) ---
    "1401": [ -76.330,  36.880],  # Norfolk/Newport News, VA
    # --- Wilmington, NC (District 15) ---
    "1501": [ -77.955,  34.235],  # Wilmington, NC
    "1503": [ -77.955,  34.235],  # Wilmington, NC (alternate terminal)
    "1512": [ -77.955,  34.235],  # Wilmington, NC (alternate terminal)
    # --- Charleston, SC (District 16) ---
    "1601": [ -79.911,  32.852],  # Charleston, SC
    "1603": [ -79.911,  32.852],  # Charleston, SC (alternate terminal)
    # --- Savannah, GA (District 17) ---
    "1701": [ -81.490,  31.150],  # Brunswick, GA
    "1703": [ -81.140,  32.115],  # Savannah, GA (Garden City Terminal)
    "1704": [ -81.140,  32.115],  # Savannah, GA (alternate terminal)
    "1791": [ -81.140,  32.115],  # Savannah, GA (residual code)
    # --- Florida (District 18) ---
    "1801": [ -82.456,  27.910],  # Tampa, FL
    "1803": [ -81.534,  30.395],  # Jacksonville, FL (Blount Island/Dames Point)
    "1808": [ -80.625,  28.415],  # Port Canaveral, FL
    "1809": [ -80.076,  26.718],  # Port of Palm Beach, FL
    "1816": [ -80.625,  28.415],  # Port Canaveral, FL
    # --- Mobile, AL (District 19) ---
    "1901": [ -88.040,  30.690],  # Mobile, AL
    "1910": [ -88.040,  30.690],  # Mobile, AL (alternate)
    # --- New Orleans / Gulf Coast (District 20) ---
    "2001": [ -90.060,  29.940],  # New Orleans, LA (alternate)
    "2002": [ -90.060,  29.940],  # New Orleans, LA
    "2006": [ -89.090,  30.368],  # Gulfport, MS
    "2007": [ -89.090,  30.368],  # Gulfport, MS (alternate)
    # --- Texas border crossings (District 23 — ves_swt_mo typically 0) ---
    "2301": [ -99.507,  27.520],  # Laredo, TX (alternate)
    "2302": [ -99.507,  27.520],  # Laredo, TX (alternate)
    "2303": [ -99.507,  27.520],  # Laredo, TX
    "2304": [ -97.494,  25.961],  # Brownsville, TX
    "2305": [ -99.834,  26.352],  # Eagle Pass, TX
    # --- El Paso area (District 24 — ves_swt_mo typically 0) ---
    "2401": [-106.489,  31.762],  # El Paso, TX
    "2402": [-106.489,  31.762],  # El Paso, TX (alternate)
    "2404": [-106.489,  31.762],  # El Paso area
    "2408": [-106.489,  31.762],  # El Paso area
    # --- Arizona border (District 25 — ves_swt_mo typically 0) ---
    "2501": [-109.540,  31.342],  # Douglas, AZ
    "2505": [-110.134,  31.560],  # Douglas/Bisbee area, AZ
    "2506": [-110.934,  31.340],  # Nogales, AZ (alternate)
    "2507": [-110.934,  31.340],  # Nogales, AZ
    # --- San Diego / Calexico border (District 26 — ves_swt_mo typically 0) ---
    "2604": [-116.966,  32.726],  # Calexico, CA (border)
    "2605": [-117.180,  32.550],  # Otay Mesa / San Ysidro, CA
    "2608": [-117.040,  32.630],  # Tecate, CA
    # --- Los Angeles / Southern California (District 27) ---
    "2704": [-118.265,  33.733],  # Los Angeles, CA
    "2707": [-118.265,  33.733],  # Los Angeles, CA (alternate terminal)
    "2709": [-118.216,  33.755],  # Long Beach, CA
    "2720": [-117.170,  32.706],  # San Diego, CA (10th Ave Marine Terminal)
    "2721": [-118.255,  33.743],  # Terminal Island, CA
    "2722": [-118.200,  33.770],  # Los Angeles, CA (alternate terminal)
    # --- San Francisco Bay (District 28) ---
    "2801": [-122.390,  37.800],  # San Francisco, CA (Pier 80)
    "2809": [-122.395,  37.795],  # San Francisco, CA (main terminal)
    "2810": [-122.350,  37.830],  # Richmond, CA (SF Bay)
    "2811": [-122.290,  37.795],  # Oakland, CA
    "2834": [-122.300,  37.910],  # Benicia / Richmond, CA
    "2835": [-122.280,  38.050],  # Benicia, CA (Carquinez Strait)
    # --- Portland, OR / Columbia River (District 29) ---
    "2904": [-122.755,  45.585],  # Portland, OR
    "2910": [-122.755,  45.585],  # Portland, OR (alternate)
    # --- Seattle / Puget Sound (District 30) ---
    "3001": [-122.330,  47.610],  # Seattle, WA
    "3002": [-122.430,  47.275],  # Tacoma, WA
    "3003": [-122.450,  48.750],  # Bellingham, WA
    "3004": [-123.434,  48.118],  # Port Angeles, WA
    "3009": [-122.200,  47.980],  # Everett, WA
    "3019": [-122.910,  47.040],  # Olympia, WA
    "3020": [-122.200,  47.980],  # Everett, WA (alternate)
    "3029": [-122.430,  47.275],  # Tacoma, WA (alternate)
    # --- Alaska (District 31) ---
    "3105": [-134.420,  58.305],  # Sitka, AK
    "3126": [-149.890,  61.235],  # Anchorage, AK
    # --- Hawaii (District 32) ---
    "3201": [-157.870,  21.310],  # Honolulu, HI
    "3205": [-155.090,  19.720],  # Hilo, HI
    "3279": [-157.870,  21.310],  # Honolulu, HI (residual code)
    # --- Pacific territories (District 33) ---
    "3302": [-170.693, -14.279],  # Pago Pago, American Samoa
    "3303": [ 144.794,  13.444],  # Apra Harbor, Guam
    "3307": [ 171.380,   7.090],  # Kwajalein, Marshall Islands (approx)
    "3310": [ 145.745,  15.188],  # Saipan, CNMI
    # --- Chicago / Great Lakes interior (District 34 — ves_swt_mo typically 0) ---
    "3401": [ -87.630,  41.850],  # Interior customs office (approx)
    "3403": [ -87.630,  41.850],  # Chicago area (alternate)
    "3411": [ -87.630,  41.850],  # Chicago area
    "3422": [ -87.630,  41.850],  # Chicago area
    # --- Duluth / Minneapolis (District 35) ---
    "3501": [ -93.265,  44.977],  # Minneapolis, MN (Mississippi River port)
    "3502": [ -92.101,  46.780],  # Duluth area
    "3512": [ -93.265,  44.977],  # Minneapolis area (alternate)
    # --- Port Hueneme / Ventura County (District 36) ---
    "3604": [-119.213,  34.151],  # Port Hueneme, CA (Channel Islands Harbor)
    "3613": [-119.213,  34.151],  # Ventura County area (near Port Hueneme)
    # --- Great Lakes upper / Lake Michigan (District 38) ---
    "3801": [ -92.101,  46.780],  # Duluth-Superior, MN/WI
    "3802": [ -87.447,  41.663],  # Indiana Harbor, IN (Lake Michigan)
    "3803": [ -87.600,  45.100],  # Escanaba, MI (Lake Michigan)
    "3807": [ -87.447,  41.663],  # Indiana Harbor area (alternate)
    # --- Detroit / Great Lakes Michigan (District 39) ---
    "3901": [ -87.620,  41.880],  # Chicago, IL (Great Lakes / inland)
    "3909": [ -83.050,  42.330],  # Detroit, MI area
    # --- Great Lakes (Lake Erie / Ohio, District 41) ---
    "4101": [ -81.700,  41.500],  # Cleveland, OH
    "4102": [ -83.540,  41.663],  # Toledo, OH (Lake Erie)
    "4103": [ -82.706,  41.449],  # Sandusky, OH (Lake Erie)
    "4110": [ -80.799,  41.865],  # Ashtabula, OH (Lake Erie)
    "4115": [ -80.554,  41.966],  # Conneaut, OH (Lake Erie)
    # --- Interior / inland (District 45 — ves_swt_mo typically 0) ---
    "4501": [ -80.020,  40.440],  # Pittsburgh, PA area (approx)
    "4503": [ -80.020,  40.440],  # Pittsburgh area (approx)
    # --- Caribbean (District 49) ---
    "4901": [ -66.617,  18.011],  # Ponce, PR
    "4909": [ -66.100,  18.450],  # San Juan, PR
    "4913": [ -67.150,  18.200],  # Mayaguez, PR
    # --- Gulf Florida (District 51) ---
    "5101": [ -82.576,  27.634],  # Port Manatee, FL
    # --- South Florida (District 52) ---
    "5201": [ -80.165,  25.778],  # Miami, FL (PortMiami)
    "5203": [ -80.116,  26.090],  # Port Everglades, FL
    "5204": [ -80.165,  25.778],  # Miami area (alternate)
    "5206": [ -80.290,  25.796],  # Miami International AIRPORT — exclude from sea analysis
    "5210": [ -80.165,  25.778],  # Miami area (alternate)
    # --- Houston / Gulf Texas (District 53) ---
    "5301": [ -95.020,  29.733],  # Houston, TX (main)
    "5309": [ -95.020,  29.733],  # Houston, TX (alternate terminal)
    "5310": [ -95.015,  29.620],  # Barbours Cut Container Terminal, TX
    # --- Corpus Christi / South Texas (District 54 — ves_swt_mo typically 0) ---
    "5401": [ -97.407,  27.800],  # Corpus Christi, TX (approx)
    # --- Dallas / Interior Texas (District 55 — ves_swt_mo typically 0) ---
    "5501": [ -96.797,  32.776],  # Dallas, TX (inland, air/land)
    "5506": [ -96.797,  32.776],  # Dallas area (inland)
    "5507": [ -96.797,  32.776],  # Dallas area (inland)
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