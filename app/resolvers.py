# app/resolvers.py

from sqlmodel import Session, select
from app.models import Baby, engine

from app.simulate_llm import simulate_llm_response  # 👈 ADD THIS



USE_LLM = True  # 🔁 Switch here


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
    
def resolve_delete_baby_profile(_, info, name):
    from sqlmodel import select
    with Session(engine) as session:
        statement = select(Baby).where(Baby.name == name)
        baby = session.exec(statement).first()
        if not baby:
            return False
        session.delete(baby)
        session.commit()
        return True


def resolve_baby_health_advice(_, info, ageInMonths):
    if USE_LLM:
        prompt = f"What should I do to keep a baby healthy at {ageInMonths} months?"

        # Simulated LLM logic
        response = simulate_llm_response(prompt)

        return {
            "message": response["summary"],
            "tips": response["tips"]
        }

    # ✅ Original logic (rule-based)
    if ageInMonths < 6:
        return {
            "message": "Your baby is very young.",
            "tips": [
                "Breastfeed or formula only",
                "No solid food yet",
                "Sleep often, tummy time daily"
            ]
        }
    elif ageInMonths < 12:
        return {
            "message": "Baby is growing fast!",
            "tips": [
                "Introduce soft solids",
                "Lots of supervised crawling",
                "Read and talk often"
            ]
        }
    else:
        return {
            "message": "Your toddler is exploring the world.",
            "tips": [
                "Finger foods and water",
                "Encourage walking and playing",
                "Stick to a daily routine"
            ]
        }

def resolve_baby_llm_advice(_, info, ageInMonths):
    prompt = f"What should I do to keep a baby healthy at {ageInMonths} months?"
    return simulate_llm_response(prompt)

    

