"""
Download raw PORTHS6MM ZIP files from the US Census Bureau.

Usage:
    python download_data.py

Files are saved to data/original/. Already-present files are skipped.
The Census Bureau publishes files at:
  https://www.census.gov/foreign-trade/data/PORTHS6MM.html
Direct ZIP URL pattern (confirmed working for recent months):
  https://www.census.gov/trade/downloads/{4-digit-year}/Port/im_hs6_m/PORTHS6MM{2-digit-year}{2-digit-month}.ZIP
"""

import sys
from pathlib import Path
import urllib.request
import urllib.error

DEST = Path("data/original")
DEST.mkdir(parents=True, exist_ok=True)

# (year, month) tuples needed for the pipeline
PERIODS = [
    (2022, 12),  # 2212 — parallel trends pre-period
    (2023, 12),  # 2312 — parallel trends pre-period
    (2024, 12),  # 2412 — pre-tariff baseline
    (2025, 12),  # 2512 — post-tariff period
]

def url_for(year, month):
    yy = str(year)[2:]
    mm = f"{month:02d}"
    return (
        f"https://www.census.gov/trade/downloads/{year}"
        f"/Port/im_hs6_m/PORTHS6MM{yy}{mm}.ZIP"
    )

def filename_for(year, month):
    yy = str(year)[2:]
    mm = f"{month:02d}"
    return f"PORTHS6MM{yy}{mm}.ZIP"

def download(year, month):
    fname = filename_for(year, month)
    out = DEST / fname
    if out.exists():
        print(f"  already present: {fname}")
        return True
    u = url_for(year, month)
    print(f"  downloading {fname} from {u} ...", end=" ", flush=True)
    try:
        urllib.request.urlretrieve(u, out)
        size_mb = out.stat().st_size / 1_048_576
        print(f"done ({size_mb:.1f} MB)")
        return True
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} — file may not yet be released or URL has changed")
        return False
    except Exception as e:
        print(f"failed: {e}")
        return False

if __name__ == "__main__":
    print("Downloading PORTHS6MM data files to data/original/\n")
    ok = all(download(y, m) for y, m in PERIODS)
    if ok:
        print("\nAll files present. Run main.ipynb to execute the pipeline.")
    else:
        print(
            "\nSome files could not be downloaded automatically.\n"
            "If the URL pattern has changed, visit:\n"
            "  https://www.census.gov/foreign-trade/data/PORTHS6MM.html\n"
            "and download the missing ZIPs manually into data/original/."
        )
        sys.exit(1)
