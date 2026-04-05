import streamlit as st
import sqlite3
from difflib import get_close_matches

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Resource Finder",
    page_icon="🔎",
    layout="centered"
)

# -------------------------
# HEADER
# -------------------------
st.title("🔎 Resource Finder")
st.caption("Search for resources using natural language.")

st.markdown(
    """
    Enter a request like:
    - **housing in kc**
    - **legal help in springfield**
    - **mental health in stl**
    """
)

st.markdown("---")

# -------------------------
# ALIAS MAPS
# -------------------------
city_aliases = {
    "st. louis": "St. Louis",
    "st louis": "St. Louis",
    "saint louis": "St. Louis",
    "stl": "St. Louis",
    "kansas city": "Kansas City",
    "kc": "Kansas City",
    "springfield": "Springfield"
}

service_aliases = {
    "housing": "Housing",
    "shelter": "Housing",
    "mental health": "Mental Health",
    "counseling": "Mental Health",
    "support group": "Support Group",
    "group": "Support Group",
    "legal aid": "Legal Aid",
    "legal help": "Legal Aid",
    "lawyer": "Legal Aid"
}

# -------------------------
# INPUT SECTION
# -------------------------
st.subheader("Search")

user_input = st.text_input(
    "Enter your request",
    placeholder="Example: housing in kc"
)

search_clicked = st.button("Search")

# -------------------------
# SEARCH LOGIC
# -------------------------
if search_clicked:

    if not user_input.strip():
        st.warning("Please enter a request before searching.")
    else:
        input_lower = user_input.lower()
        words = input_lower.split()

        found_city = None
        found_service = None

        # -------------------------
        # EXACT CITY MATCH
        # -------------------------
        for alias, official_name in city_aliases.items():
            if alias in input_lower:
                found_city = official_name
                break

        # -------------------------
        # EXACT SERVICE MATCH
        # -------------------------
        for alias, official_name in service_aliases.items():
            if alias in input_lower:
                found_service = official_name
                break

        # -------------------------
        # FUZZY CITY MATCH
        # -------------------------
        if found_city is None:
            for word in words:
                matches = get_close_matches(word, city_aliases.keys(), n=1, cutoff=0.75)
                if matches:
                    found_city = city_aliases[matches[0]]
                    break

        # -------------------------
        # FUZZY SERVICE MATCH
        # -------------------------
        if found_service is None:
            for word in words:
                matches = get_close_matches(word, service_aliases.keys(), n=1, cutoff=0.75)
                if matches:
                    found_service = service_aliases[matches[0]]
                    break

        # -------------------------
        # VALIDATION
        # -------------------------
        if found_city is None or found_service is None:
            st.error("Could not understand the full request.")
            st.info("Try including both a city and a service, like: housing in kc")
        else:
            st.success("Request understood")

            col1, col2 = st.columns(2)
            with col1:
                st.metric("City", found_city)
            with col2:
                st.metric("Service", found_service)

            # -------------------------
            # DATABASE QUERY
            # -------------------------
            conn = sqlite3.connect("resources.db")
            cursor = conn.cursor()

            query = """
            SELECT o.org_name, c.city_name, s.service_type
            FROM organizations o
            JOIN cities c ON o.city_id = c.city_id
            JOIN services s ON o.org_id = s.org_id
            WHERE c.city_name = ?
            AND s.service_type = ?
            """

            cursor.execute(query, (found_city, found_service))
            results = cursor.fetchall()
            conn.close()

            st.markdown("---")
            st.subheader("Results")

            if results:
                for row in results:
                    org, city, service = row

                    with st.container():
                        st.markdown(f"### 🏢 {org}")
                        st.write(f"**City:** {city}")
                        st.write(f"**Service:** {service}")
                        st.markdown("---")
            else:
                st.info("No matching resources found.")

# -------------------------
# FOOTER
# -------------------------
st.caption("Built with Python, SQLite, and Streamlit")