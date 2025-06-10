import streamlit as st
import requests
import json

st.title("🧾 Technician Request Form")

skills = st.text_input("Required Skills (comma separated)")
mode = st.radio("Mode", ["remote", "on-site"])
location = st.text_input("Client Location")

if st.button("Submit Ticket"):
    ticket = {
        "required_skills": [s.strip() for s in skills.split(",")],
        "mode": mode,
        "client_location": location
    }

    # Save ticket locally (in shared folder)
    with open("../shared/tickets.json", "w") as f:
        json.dump(ticket, f)

    # Call FastAPI to assign technician
    res = requests.post("https://your-fastapi-url.onrender.com/assign", json=ticket)
    assigned = res.json()

    # Save result
    with open("../shared/assigned.json", "w") as f:
        json.dump(assigned, f)

    st.success("Technician Assigned:")
    st.json(assigned)

