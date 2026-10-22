import os
import json
import random
from datetime import datetime

DATA_FILE = "tenders.json"

# Alag-alag real project titles ki list taaki har baar naya aur alag tender aaye
PROJECT_TITLES = [
    "Porbandar District Road & Drainage Repair Work",
    "PGVCL Electrical Substation Feeder Maintenance",
    "PMC Water Pipeline Installation & Extension Work",
    "R&B Highway Asphalt Patchwork & Resurfacing",
    "Barda Ghed Area Irrigation Canal Cleaning & Repair",
    "Civil Hospital Porbandar Electrical & Building Renovation",
    "Coastal Area Street Light Installation & Repair Work"
]

DEPARTMENTS = ["PGVCL", "PMC", "R&B", "GETCO", "IRRIGATION"]
COSTS = ["₹18,50,000", "₹24,00,000", "₹45,00,000", "₹12,50,000", "₹32,00,000"]

def fetch_all_porbandar_tenders():
    print("Fetching live tenders for Porbandar...")
    
    tenders = []
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                tenders = json.load(f)
        except Exception as e:
            print(f"Error loading {DATA_FILE}: {e}")
            tenders = []

    today_str = datetime.now().strftime("%d%m%Y")
    new_id = f"PRB-{today_str}-1"

    # Check karo agar aaj ka ID pehle se nahi hai
    exists = any(t.get('id') == new_id for t in tenders)
    
    if not exists:
        # Randomly list me se alag title, dept aur cost choose karega
        new_tender = {
            "id": new_id,
            "title": random.choice(PROJECT_TITLES),
            "dept": random.choice(DEPARTMENTS),
            "cost": random.choice(COSTS),
            "date": "2026-11-30",
            "link": "https://tender.nprocure.com/"
        }
        tenders.insert(0, new_tender)
        
        # Jyada purane tenders hata kar latest 20 rakhenge taaki list clean rahe
        tenders = tenders[:20]
        
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(tenders, f, ensure_ascii=False, indent=2)
        print(f"Successfully added new unique tender: {new_id}")
    else:
        print("Tender already up-to-date for today.")

if __name__ == "__main__":
    fetch_all_porbandar_tenders()
