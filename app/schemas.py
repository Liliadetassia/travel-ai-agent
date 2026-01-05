from pydantic import BaseModel
from typing import List

class TravelRequest(BaseModel):
    location: str
    check_in: str
    check_out: str
    guests: int
    preferences: str

class Accommodation(BaseModel):
    name: str
    price: str
    rating: float
    url: str

class TravelResponse(BaseModel):
    recommendations: str
    accommodations: List[Accommodation]
