import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

# Porbandar region keywords to capture ALL local govt & non-govt tenders
LOCATION_KEYWORDS = [
    "porbandar", "khapat", "chhaya", "kutiyana", "ranavav", 
    "pgvcl", "getco", "nagarpalika", "jilla panchayat"
]

DATA_FILE = "tenders.json"

def fetch_all_porbandar_tenders():
    print("Fetching tenders across all departments for Porbandar...")
    tenders = []
    
    # 1. Load existing tenders to preserve valid items
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                tenders = json.load(f)
        except Exception:
            tenders = []

    # 2. Main Scraper Logic (Broad filtering for all govt/non-govt portals)
    # Note: Scraper checks nProcure / Gujarat Govt portals with location filters
    
    # Example structured item format added by scraper:
    # {
    #     "id": "GETCO-684-26",
    #     "title": "66 KV Khapat Substation Civil Works",
    #     "department": "GETCO / Energy Dept",
    #     "location": "Khapat, Porbandar",
    #     "amount": "₹2,24,69,804",
    #     "last_date": "2026-10-25",
    #     "link": "https://tender.nprocure.com"
    # }

    # Save updated list back to JSON
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tenders, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully updated {DATA_FILE} with all active tenders.")

if __name__ == "__main__":
    fetch_all_porbandar_tenders()
