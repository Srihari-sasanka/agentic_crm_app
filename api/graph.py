from langgraph.graph import StateGraph
from agents import skill_match_agent, mode_location_agent, rating_agent
from typing import Dict, Any

builder = StateGraph(Dict[str, Any])

builder.add_node("skill_match", skill_match_agent)
builder.add_node("mode_location_check", mode_location_agent)
builder.add_node("rate_select", rating_agent)

builder.set_entry_point("skill_match")
builder.add_edge("skill_match", "mode_location_check")
builder.add_edge("mode_location_check", "rate_select")

# ✅ Declare the end node
builder.set_finish_point("rate_select")

graph = builder.compile()
