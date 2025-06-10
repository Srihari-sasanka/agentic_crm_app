from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from graph import graph  # This is your LangGraph pipeline

# Define the structure of the incoming JSON
class Ticket(BaseModel):
    required_skills: List[str]
    mode: str
    client_location: str

# Initialize the FastAPI app
app = FastAPI(title="Agentic Technician Assignment API")

# Define a POST endpoint that uses the Ticket model directly
@app.post("/assign")
def assign_technician(ticket: Ticket):
    # Directly use ticket.dict() instead of manually parsing JSON
    state = {"ticket": ticket.dict()}

    result = graph.invoke(state)

    if result.get("selected"):
        return {"assigned": result["selected"]}
    else:
        return {"assigned": None}

# Optional welcome route
@app.get("/")
def root():
    return {"message": "✅ Agentic Technician Assignment API is running! Visit /docs to test."}
