# app/resolvers.py

from sqlmodel import Session, select
from app.models import Baby, engine

def resolve_hello(_, info):
    return "Hello from BabyBot!"

def resolve_add_baby_profile(_, info, name, ageInMonths, notes=None):
    new_baby = Baby(name=name, ageInMonths=ageInMonths, notes=notes)
    with Session(engine) as session:
        session.add(new_baby)
        session.commit()
        session.refresh(new_baby)
        return new_baby

def resolve_all_babies(_, info):
    with Session(engine) as session:
        statement = select(Baby)
        results = session.exec(statement)
        return results.all()

def resolve_baby_health_advice(_, info, input):
    age = input.get("ageInMonths", 0)
    name = input.get("name", "the baby")
    notes = input.get("notes", "")

    # Placeholder for LLM integration
    if age < 6:
        return {
            "message": f"{name} is very young (under 6 months).",
            "tips": [
                "Breastfeed or formula only.",
                "Avoid solid foods.",
                "Ensure tummy time and frequent naps."
            ]
        }
    elif age < 12:
        return {
            "message": f"{name} is growing well (6–12 months)!",
            "tips": [
                "Introduce soft solids.",
                "Supervised crawling helps muscle growth.",
                "Start reading or talking frequently."
            ]
        }
    else:
        return {
            "message": f"{name} is entering toddler stage!",
            "tips": [
                "Encourage walking and exploration.",
                "Routine is important.",
                "Give finger foods and water."
            ]
        }

