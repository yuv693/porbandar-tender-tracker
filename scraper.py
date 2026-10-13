import json
import os
import re
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# Files Path
JSON_FILE = "tenders.json"

# Search Target Keywords for Porbandar District
LOCATION_KEYWORDS = ["porbandar", "પોરબંદર", "pgvcl"]

def load_existing_tenders():
    """Pehle se saved tenders ko JSON file se load karta hai."""
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading existing JSON: {e}")
            return []
    return []

def save_tenders(tenders_list):
    """Updated tenders list ko JSON file mein write karta hai."""
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(tenders_list, f, ensure_ascii=False, indent=2)
    print(f"Successfully saved {len(tenders_list)} tenders to {JSON_FILE}")

def is_porbandar_tender(title, dept):
    """Check karta hai ki tender Porbandar District ya PGVCL ka hai ya nahi."""
    combined_text = f"{title} {dept}".lower()
    return any(keyword in combined_text for keyword in LOCATION_KEYWORDS)

def fetch_live_tenders():
    """
    Government Tender Portal Scraper Engine
    Porbandar District aur PGVCL ke open tenders extract karega.
    """
    print("Scanning for active Porbandar District tenders...")
    
    existing_tenders = load_existing_tenders()
    existing_ids = {str(t.get("id")) for t in existing_tenders}
    
    new_tenders_found = []

    # Example Mock / Scraped Data Processing Structure
    # Web scraping requests portal response parse kar ke naye items build karta hai
    
    # Check duplicate and filter location
    for tender in new_tenders_found:
        tender_id = str(tender.get("id"))
        title = tender.get("title", "")
        dept = tender.get("dept", "")
        
        if tender_id not in existing_ids and is_porbandar_tender(title, dept):
            existing_tenders.insert(0, tender)
            existing_ids.add(tender_id)
            print(f"New Porbandar Tender Added: {tender_id} - {title}")

    # Final list save karein
    save_tenders(existing_tenders)

if __name__ == "__main__":
    fetch_live_tenders()
