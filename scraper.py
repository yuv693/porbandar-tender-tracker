import json
import re
import requests

# Live Government Scraper Script for Porbandar
DATA_URL = "https://raw.githubusercontent.com/yuv693/porbandar-tender-tracker/main/tenders.json"

# Naye Tenders Fetch karna (Sample Automation Feed)
new_tenders = [
    {
        "id": "PGVCL-AUTO-01",
        "dept": "PGVCL",
        "title": "Porbandar Rural Feeder Line Cable & Transformer Maintenance",
        "cost": "₹8,50,000",
        "date": "29-Oct-2026",
        "link": "https://tender.nprocure.com",
    },
    {
        "id": "IRR-AUTO-02",
        "dept": "IRRIGATION",
        "title": "Barda Wild Life Sanctuary Canal Desilting Works Phase-2",
        "cost": "₹42.50 Lakh",
        "date": "05-Nov-2026",
        "link": "https://tender.nprocure.com",
    },
]

# JSON File Update karna
with open("tenders.json", "w", encoding="utf-8") as f:
  json.dump(new_tenders, f, indent=4)

print("Tenders Updated Successfully!")
