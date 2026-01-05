from fastapi import FastAPI
from app.schemas import TravelRequest, TravelResponse
from app.services.travel_agent import run_travel_agent

app = FastAPI(title="AI Travel Agent")

@app.post("/travel", response_model=TravelResponse)
def travel_agent(request: TravelRequest):
    recommendation, accommodations = run_travel_agent(request)

    formatted = []
    for a in accommodations:
        formatted.append({
            "name": a.get("name"),
            "price": str(a.get("price")),
            "rating": float(a.get("rating", 0)),
            "url": a.get("url")
        })

    return {
        "recommendations": recommendation,
        "accommodations": formatted
    }

