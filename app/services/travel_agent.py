from app.services.apify_service import fetch_accommodations
from app.services.gemini_service import ask_gemini

def run_travel_agent(data):
    accommodations = fetch_accommodations(
        data.location,
        data.check_in,
        data.check_out,
        data.guests
    )

    summarized = []
    for item in accommodations:
        summarized.append(
            f"{item.get('name')} - {item.get('price')} - Nota {item.get('rating')}"
        )

    prompt = f"""
Você é um agente de viagens inteligente.
Preferências do usuário: {data.preferences}

Opções encontradas:
{chr(10).join(summarized)}

Explique quais são as 3 melhores opções e o motivo.
"""

    recommendation = ask_gemini(prompt)

    return recommendation, accommodations
