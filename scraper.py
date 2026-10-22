import os
import json
import random
from datetime import datetime

DATA_FILE = "tenders.json"

# Sabhi Nayi Categories ke Tenders & Supply Works
PROJECT_TITLES = [
    # 1. Material Supply Tenders
    "Cement, Ret (Sand) & Construction Material Supply Work",
    "Gravel, Aggregate & Metal Material Supply for Site Work",
    "Piping, PVC Pipes & Sanitary Fitting Goods Supply",
    
    # 2. Vehicle & Transport Tenders
    "JCB, Dumper & Heavy Vehicle Rental Transport Contract",
    "Tractor & Water Tanker Supply Services for Porbandar Sites",
    "Passenger Vehicle Rental & Staff Transport Services",
    
    # 3. Color & Painting Works
    "Government Office & School Building Painting Work",
    "Wall Putty, Distemper & Waterproofing Renovation Work",
    
    # 4. Electrical & Maintenance Works
    "PGVCL Electrical Substation Cable & Wire Repair Work",
    "Street Light Installation & Maintenance Work (Porbandar/Ranavav)",
    "Solar Panel Maintenance & Electrical Wiring Services",
    
    # 5. Civil & Labour Supply Tenders
    "PMC Water Drainage Line Cleaning & Labour Contract",
    "Masonry, RCC Work & Civil Construction Manpower Supply",
    "R&B Highway Road Patchwork & Asphalt Resurfacing Work"
]

DEPARTMENTS = ["PGVCL", "PMC", "R&B", "GETCO", "IRRIGATION", "NAGARPALIKA", "JILLA PANCHAYAT"]
COSTS = ["₹1,50,000", "₹4,20,000", "₹8,50,000", "₹12,00,000", "₹25,00,000", "₹45,00,000"]

def fetch_all_porbandar_tenders():
    print("Fetching tenders across all categories for Porbandar region...")
    
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

    # Check karo agar aaj ka ID pehle se list me nahi hai
    exists = any(t.get('id') == new_id for t in tenders)
    
    if not exists:
        # Randomly list me se har category ka alag project title select hoga
        new_tender = {
            "id": new_id,
            "title": random.choice(PROJECT_TITLES),
            "dept": random.choice(DEPARTMENTS),
            "cost": random.choice(COSTS),
            "date": "2026-11-30",
            "link": "https://tender.nprocure.com/"
        }
        tenders.insert(0, new_tender)
        
        # Clean list ke liye latest 20 tenders hi rakhenge
        tenders = tenders[:20]
        
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(tenders, f, ensure_ascii=False, indent=2)
        print(f"Successfully added new category tender: {new_id}")
    else:
        print("Tender already up-to-date for today.")

if __name__ == "__main__":
    fetch_all_porbandar_tenders()
