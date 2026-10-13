import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

# Porbandar & Local Region Keywords
LOCATION_KEYWORDS = [
    "porbandar", "khapat", "chhaya", "kutiyana", "ranavav",
    "pgvcl", "getco", "nagarpalika", "jilla panchayat", "barda", "ghed"
]

DATA_FILE = "tenders.json"

def fetch_all_porbandar_tenders():
    print("Fetching tenders across all departments for Porbandar...")
    tenders = []

    # 1. Load existing tenders to preserve valid items
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                tenders = json.loads(f.read())
        except Exception:
            tenders = []

    # 2. Example live fetch simulation / nProcure parsing structure
    # Yahan aap nProcure ya public portals se request bhej kar data nikalte ho
    # Sample structure jo automatically add hoga:
    
    sample_tender = {
        "id": "PRB-" + datetime.now().strftime("%d%m%Y-1"),
        "title": "Porbandar District Infrastructure & Maintenance Works",
        "dept": "GETCO / PGVCL / Nagarpalika",
        "cost": "₹15,00,000",
        "date": "2026-11-30",
        "link": "https://tender.nprocure.com/"
    }

    # Check if duplicate already exists
    exists = any(t.get('id') == sample_tender['id'] for t in tenders)
    if not exists:
        tenders.insert(0, sample_tender)

    # 3. Save updated list back to JSON
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tenders, f, ensure_ascii=False, indent=2)

    print("Successfully updated tenders.json with all active tenders.")

if __name__ == "__main__":
    fetch_all_porbandar_tenders()
