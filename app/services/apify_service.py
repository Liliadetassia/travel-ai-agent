import requests
from app.config import APIFY_API_TOKEN, APIFY_BASE_URL

def fetch_accommodations(location, check_in, check_out, guests):
    actor_id = "apify/booking-scraper"
    
    payload = {
        "location": location,
        "checkIn": check_in,
        "checkOut": check_out,
        "adults": guests,
        "maxItems": 10
    }

    response = requests.post(
        f"{APIFY_BASE_URL}/acts/{actor_id}/runs?token={APIFY_API_TOKEN}",
        json=payload
    )

    response.raise_for_status()
    run_id = response.json()["data"]["id"]

    dataset_url = f"{APIFY_BASE_URL}/runs/{run_id}/dataset/items?token={APIFY_API_TOKEN}"
    return requests.get(dataset_url).json()
