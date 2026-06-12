# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Goal

Analyze the impact of US tariffs on CO2 emissions for washing machine imports (HS codes 845011, 845020) using the Difference-in-Differences method and a Carbon Rerouting Index. Countries studied: China (5700), South Korea (5800), Vietnam (5520), India (5330), Mexico (2010).

## Running the Notebook

```bash
pip install -r requirements.txt
jupyter notebook main.ipynb
```

`main.py` is currently empty; all active work is in `main.ipynb`.

## Architecture

### Module layout

- `coordinates.py` — all lookup dictionaries: `ton_km` (gCO₂/ton-km by country code), `asian_origins`, `us_ports`, `mexico_start`, `state_centroids`. Coordinates are always `[longitude, latitude]`.
- `core_modules/core_modules.py` — two functions used via `from core_modules import core_modules as core`:
  - `compute_distance(row, departure_coords, destination_coords, by_sea, departure_code, destination_code)` — accepts either a dict (keyed by a row column) or a single coordinate pair for each endpoint.
  - `compute_co2(row, transportation_type)` — multiplies weight × distance × `coord.ton_km[cty_code]`.

### Data pipelines

Two fixed-width ASCII datasets from [census.gov](https://www.census.gov/foreign-trade/):

| File | DataFrame | Routes | Key weight columns |
|---|---|---|---|
| `data/original/PORTHS6MM2501.txt` | `df_ocean_routes` / `df_asian_routes_wash_v1` | Asia → US seaports | `ves_swt_mo` (kg) |
| `data/original/isthsm2501.txt` | `df_land_imports` / `df_land_imports_mex_wash_v1` | Mexico → US states (land) | `gen_val_mo` converted via `washing_machine_price_coeff` |

Both FWF files are expensive to parse. After first parse, the notebook saves them to `data/intermediate/` as CSVs and reloads from there on subsequent runs — do not delete those intermediate files.

A third source, `data/original/State Imports by HS Commodities_v4.csv` (USA Trade Census), provides vessel/air shipping weight as a sanity check.

### Key conventions

- **Coordinates**: always `[lon, lat]`. `great_circle` from geopy expects `(lat, lon)`, so `core_modules` reverses them with `[::-1]`.
- **Country codes**: Census Schedule C 4-digit strings (e.g. `"5700"` = China). Defined in `coordinates.py` and must match between `ton_km`, `asian_origins`, and `cty_code` column values.
- **Port codes**: Schedule D 4-digit strings built as `dist_unlade + port_unlade` → stored in `port_full`. Must be present in `coord.us_ports` to compute distance.
- **Land distance multiplier**: `great_circle` result is multiplied by `1.3` to account for road detours.
- **Mexico weight**: The ISTHS6M dataset has no land shipping weight, so weight is back-calculated from `gen_val_mo / washing_machine_price_coeff` (derived from the ocean dataset's value/weight ratio ≈ 3.91 $/kg).

### Data sources (require manual download)

- `data/original/*.txt` files are git-ignored and must be downloaded from census.gov.
- Country code reference: `https://www.census.gov/foreign-trade/schedules/c/country.txt`
- Ton-km emission factors sourced from US EPA SmartWay, UNCTAD 2024, and Notteboom & Rodrigue (2009).

### Planned but missing module

The notebook references `from diff_diff import DifferenceInDifferences` — this module does not yet exist and needs to be implemented for the statistical analysis stage.
