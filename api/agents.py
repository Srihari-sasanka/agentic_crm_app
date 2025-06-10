from data import TECHNICIANS, TICKET
from utils import skill_match_score

def skill_match_agent(state):
    ticket = state["ticket"]
    from data import TECHNICIANS
    from utils import skill_match_score

    eligible = [
        tech for tech in TECHNICIANS
        if skill_match_score(ticket["required_skills"], tech["skills"]) >= 0.67
    ]
    state["eligible"] = eligible
    return state  # ✅ This is required



def mode_location_agent(state):
    ticket = state["ticket"]
    filtered = []
    for tech in state["eligible"]:
        if tech["status"] != "available":
            continue
        if ticket["mode"] == "remote" and tech["mode"] == "remote":
            filtered.append(tech)
        elif ticket["mode"] == "on-site" and tech["mode"] == "on-site" and tech["location"].lower() == ticket["client_location"].lower():
            filtered.append(tech)
    state["filtered"] = filtered
    return state  # ✅ Return updated state


def rating_agent(state):
    if state["filtered"]:
        state["selected"] = sorted(state["filtered"], key=lambda x: x["rating"], reverse=True)[0]
    else:
        state["selected"] = None
    return state  # ✅ Always return state

