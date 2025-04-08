import streamlit as st
import requests

st.title("🛍️ Ebuss Product Recommender")

username = st.text_input("Enter your username:")

if st.button("Get Recommendations"):
    if username:
        try:
            response = requests.post("http://127.0.0.1:5000/recommend", json={"username": username})
            if response.status_code == 200:
                recs = response.json()["recommendations"]
                st.write("### Recommendations:")
                for r in recs:
                    st.write(f"🔹 {r}")
            else:
                st.error("⚠️ Failed to fetch recommendations.")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
    else:
        st.warning("Please enter a username.")
