import json
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from graph import graph

# Technician and ticket storage
TECHNICIAN_FILE = "data.json"

class Ticket(BaseModel):
    required_skills: List[str]
    mode: str
    client_location: str

app = FastAPI()

@app.post("/assign")
def assign_technician(ticket: Ticket):
    # Load technician data
    with open(TECHNICIAN_FILE, "r") as f:
        technician_data = json.load(f)

    # Load graph with global TECHNICIANS
    state = {"ticket": ticket.dict(), "TECHNICIANS": technician_data}
    result = graph.invoke(state)
    return {"assigned": result.get("selected")}
