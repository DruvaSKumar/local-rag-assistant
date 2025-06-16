import streamlit as st
from agents import macro_agent, route_query
from vector_store import add_user_notes

st.title("🏋️ AI Fitness Multi-Agent App")

user_id = "user1"

st.header("1. Set Profile")
profile = st.text_input("Profile (e.g., Male, 25 years, 70kg)")
goal = st.text_input("Goal (e.g., Lose fat, Gain muscle)")
if st.button("Generate Macro Plan"):
    result = macro_agent(profile, goal)
    st.json(result)

st.header("2. Add Personal Notes")
note = st.text_area("Write a note or journal entry")
if st.button("Save Note"):
    add_user_notes(user_id, [note])
    st.success("Note saved to vector store!")

st.header("3. Ask a Question")
query = st.text_input("Ask something (math or personal)")
if st.button("Ask"):
    response = route_query(user_id, query)
    st.write("### Response:")
    st.write(response)
