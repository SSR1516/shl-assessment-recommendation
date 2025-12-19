import streamlit as st
import requests

# =========================
# CONFIG
# =========================
API_URL = "https://shl-assessment-recommendation-248h.onrender.com/recommend"

st.set_page_config(
    page_title="SHL Assessment Recommender",
    layout="centered"
)

# =========================
# UI
# =========================
st.title("🔍 SHL Assessment Recommendation System")
st.write(
    "Enter a hiring requirement or job description to get relevant SHL assessments."
)

query = st.text_area(
    "Hiring requirement / Job description:",
    placeholder="e.g. Looking for Java developers with teamwork and communication skills"
)

top_k = st.slider(
    "Number of recommendations",
    min_value=5,
    max_value=20,
    value=10
)

# =========================
# ACTION
# =========================
if st.button("Get Recommendations"):
    if not query.strip():
        st.warning("⚠️ Please enter a valid query.")
    else:
        with st.spinner("🔄 Fetching recommendations..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"query": query, "k": top_k},
                    timeout=30
                )

                if response.status_code != 200:
                    st.error(
                        f"❌ Backend error ({response.status_code}). Please try again."
                    )
                else:
                    data = response.json()

                    if not isinstance(data, list) or len(data) == 0:
                        st.warning("No recommendations found.")
                    else:
                        st.success("✅ Recommended SHL Assessments")

                        for idx, rec in enumerate(data, start=1):
                            st.markdown(f"### {idx}. {rec.get('name', 'N/A')}")
                            st.markdown(f"[🔗 Open Assessment]({rec.get('url', '#')})")

                            if rec.get("test_type"):
                                st.markdown(
                                    f"**Test Type:** {', '.join(rec['test_type'])}"
                                )

                            if rec.get("duration"):
                                st.markdown(
                                    f"**Duration:** {rec['duration']} minutes"
                                )

                            st.markdown(
                                f"**Remote Support:** {rec.get('remote_support', 'N/A')}"
                            )
                            st.markdown(
                                f"**Adaptive Support:** {rec.get('adaptive_support', 'N/A')}"
                            )

                            st.markdown("---")

            except requests.exceptions.RequestException as e:
                st.error(f"❌ Connection error: {e}")
